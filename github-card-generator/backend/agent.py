from google.adk import Agent, GoogleGenerativeAI
import os

# Initialize LLM (Gemini 2.5 Flash)
# Note: "gemini-2.0-flash" or similar depending on exact SDK availability/version
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

# Define the GitHub Dev Card Agent
github_agent = Agent(
    name="GitHubDevCardAgent",
    instruction="You are an expert at creating visual GitHub developer cards based on user data.",
    llm=llm
)

# TODO: Register MCP tools once the connection is established in main.py
