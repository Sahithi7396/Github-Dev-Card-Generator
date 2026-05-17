import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json
import os
from dotenv import load_dotenv

load_dotenv()

async def run_test():
    # Define server parameters
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "mcp_server.py"],
        env=os.environ.copy()
    )

    print("Connecting to MCP server...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize session
            await session.initialize()
            print("Session initialized.")

            username = "torvalds"
            
            # 1. Call scrape_github
            print(f"Calling scrape_github for {username}...")
            scrape_result = await session.call_tool("scrape_github", {"username": username})
            if not scrape_result.content or getattr(scrape_result, "isError", False):
                print(f"Error in scrape_github: {scrape_result}")
                return
            
            github_data = scrape_result.content[0].text
            github_data_dict = json.loads(github_data)
            print("Scrape successful.")

            # 2. Call analyze_profile
            print("Calling analyze_profile...")
            analyze_result = await session.call_tool("analyze_profile", {"github_data": github_data_dict})
            if not analyze_result.content or getattr(analyze_result, "isError", False):
                print(f"Error in analyze_profile: {analyze_result}")
                return
            
            analysis = json.loads(analyze_result.content[0].text)
            print("Analysis successful.")

            # 3. Generate HTML card
            print("Calling generate_card_html...")
            card_result = await session.call_tool("generate_card_html", {
                "username": username,
                "github_data": github_data_dict,
                "analysis": analysis
            })
            if not card_result.content or getattr(card_result, "isError", False):
                print(f"Error in generate_card_html: {card_result}")
                return
            
            print("Card HTML generation successful.")

            # 4. Print results
            print("\n--- Test Results ---")
            print(f"Username: {username}")
            print(f"Card Theme: {analysis.get('card_theme')}")
            print(f"Developer Vibe: {analysis.get('developer_vibe')}")
            print("--------------------\n")

if __name__ == "__main__":
    asyncio.run(run_test())
