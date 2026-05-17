import os
import json
import httpx
from mcp.server.fastmcp import FastMCP
from jinja2 import Template
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("GithubCardTools")

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


@mcp.tool()
async def scrape_github(username: str) -> dict:
    """Fetch GitHub statistics for a given user using REST API."""

    async with httpx.AsyncClient() as client:

        # Fetch user profile
        user_res = await client.get(
            f"https://api.github.com/users/{username}"
        )

        if user_res.status_code != 200:
            return {"error": f"User {username} not found"}

        user_data = user_res.json()

        # Fetch repositories
        repos_res = await client.get(
            f"https://api.github.com/users/{username}/repos?sort=updated&per_page=30"
        )

        repos_data = repos_res.json() if repos_res.status_code == 200 else []

        # Sort top repos
        sorted_repos = sorted(
            repos_data,
            key=lambda x: x.get("stargazers_count", 0),
            reverse=True
        )[:6]

        top_repos = []

        for r in sorted_repos:

            top_repos.append({
                "name": r.get("name"),
                "stars": r.get("stargazers_count", 0),
                "language": r.get("language") or "Unknown",
                "description": r.get("description") or "No description available"
            })

        # Aggregate languages
        languages = {}

        for r in repos_data:

            lang = r.get("language")

            if lang:
                languages[lang] = languages.get(lang, 0) + 1

        return {
            "name": user_data.get("name") or username,
            "bio": user_data.get("bio") or "No bio available",
            "location": user_data.get("location") or "Unknown",
            "public_repos": user_data.get("public_repos", 0),
            "followers": user_data.get("followers", 0),
            "avatar_url": user_data.get("avatar_url"),
            "top_repos": top_repos,
            "languages": sorted(
                languages.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }


@mcp.tool()
async def analyze_profile(github_data: dict) -> dict:
    """Analyze GitHub profile using Gemini."""

    prompt = f"""
    Analyze this GitHub profile data and return JSON only:

    {json.dumps(github_data)}

    {{
        "developer_vibe": "1 sentence personality",
        "top_skills": ["skill1", "skill2", "skill3"],
        "fun_fact": "interesting fact",
        "card_theme": "hacker"
    }}
    """

    response = model.generate_content(prompt)

    try:

        text = response.text.strip()

        if text.startswith("```json"):
            text = text[7:-3].strip()

        return json.loads(text)

    except Exception:

        return {
            "developer_vibe": "A passionate developer.",
            "top_skills": ["Python", "JavaScript", "GitHub"],
            "fun_fact": "Loves building cool projects.",
            "card_theme": "hacker"
        }


@mcp.tool()
async def generate_card_html(
    username: str,
    github_data: dict,
    analysis: dict
) -> str:

    """Generate HTML developer card."""

    themes = {

        "hacker":
            "background:#0d1117;color:#58a6ff;border:1px solid #30363d;",

        "builder":
            "background:#f6f8fa;color:#24292f;border:1px solid #d0d7de;",

        "researcher":
            "background:#030637;color:#917fb3;border:1px solid #3c0753;",

        "designer":
            "background:#fff5e0;color:#ff6969;border:1px solid #c70039;",

        "open-source-hero":
            "background:#f0fff4;color:#22863a;border:1px solid #28a745;"
    }

    theme_style = themes.get(
        analysis.get("card_theme"),
        themes["hacker"]
    )

    html_template = """

    <div style="{{ style }} padding:20px;border-radius:12px;
    font-family:Arial;max-width:450px;">

        <div style="display:flex;align-items:center;margin-bottom:20px;">

            <img
                src="{{ data.avatar_url }}"
                style="width:80px;height:80px;border-radius:50%;
                margin-right:15px;border:2px solid currentColor;"
            >

            <div>
                <h2 style="margin:0;">{{ data.name }}</h2>

                <p style="margin:5px 0;font-size:0.9em;opacity:0.8;">
                    @{{ username }}
                </p>
            </div>

        </div>

        <p style="font-style:italic;margin-bottom:15px;">
            "{{ analysis.developer_vibe }}"
        </p>

        <div style="margin-bottom:15px;">

            {% for skill in analysis.top_skills %}

            <span style="
                display:inline-block;
                padding:2px 10px;
                border-radius:20px;
                background:rgba(128,128,128,0.1);
                font-size:0.8em;
                margin-right:5px;
                border:1px solid currentColor;
            ">
                {{ skill }}
            </span>

            {% endfor %}

        </div>

        <div style="
            display:flex;
            gap:20px;
            font-size:0.9em;
            margin-bottom:15px;
        ">

            <span>
                <strong>{{ data.public_repos }}</strong> Repos
            </span>

            <span>
                <strong>{{ data.followers }}</strong> Followers
            </span>

        </div>

        <div style="
            border-top:1px solid rgba(128,128,128,0.2);
            padding-top:15px;
        ">

            <h4 style="margin:10px 0 5px 0;">
                Top Repositories
            </h4>

            {% for repo in data.top_repos[:3] %}

            <div style="margin-bottom:10px;">

                <div style="font-weight:bold;font-size:0.9em;">
                    {{ repo.name }} ⭐ {{ repo.stars }}
                </div>

                <div style="font-size:0.8em;opacity:0.7;">

                    {{ repo.language or "Unknown" }} -

                    {{ (repo.description or
                    "No description available")[:60] }}

                    {% if repo.description and
                    repo.description|length > 60 %}
                    ...
                    {% endif %}

                </div>

            </div>

            {% endfor %}

        </div>

        <div style="
            font-size:0.7em;
            margin-top:15px;
            text-align:right;
            opacity:0.5;
        ">
            {{ analysis.fun_fact }}
        </div>

    </div>
    """

    template = Template(html_template)

    return template.render(
        username=username,
        data=github_data,
        analysis=analysis,
        style=theme_style
    )


@mcp.tool()
async def save_card(username: str, html: str) -> str:
    """Save generated card."""

    dir_path = "static/cards"

    os.makedirs(dir_path, exist_ok=True)

    file_path = f"{dir_path}/{username}.html"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    return f"/static/cards/{username}.html"


if __name__ == "__main__":
    mcp.run()