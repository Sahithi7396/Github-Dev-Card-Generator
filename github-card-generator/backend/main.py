from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn
import os

from mcp_server import (
    scrape_github,
    analyze_profile,
    generate_card_html,
    save_card
)

app = FastAPI(title="GitHub Dev Card Generator API")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "GitHub Dev Card Generator API is running"
    }

@app.post("/generate")
async def generate_card(username: str):

    github_data = await scrape_github(username)

    profile_analysis = await analyze_profile(github_data)

    card_html = await generate_card_html(
        username,
        github_data,
        profile_analysis
    )

    card_path = await save_card(username, card_html)

    return {
        "username": username,
        "github_data": github_data,
        "analysis": profile_analysis,
        "card_path": card_path,
        "status": "success"
    }

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )