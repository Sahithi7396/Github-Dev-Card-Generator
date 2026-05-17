# 🚀 GitHub Dev Card Generator

<img width="400" height="500" alt="image"  src="https://github.com/user-attachments/assets/bd99b1c0-89d1-4380-8b85-31c511264ef0" />


Generate beautiful, shareable developer profile cards from any GitHub username — instantly.

---
## 🌐 Live Deployment

🔗 Frontend Web App  
https://github-card-frontend-164750172990.us-central1.run.app/

⚙️ Backend API Service  
https://github-card-backend-164750172990.us-central1.run.app/

---

## 📖 Overview

A full-stack web app that fetches a GitHub user's public profile data and renders it as a styled HTML developer card.

Cards are:
- generated dynamically
- displayed inside the browser
- shareable via direct link
- accessible using QR code

The project also integrates:
- Google ADK
- Gemini AI
- MCP tools

for AI-powered developer profile analysis.

---

## ✨ Features

- ⚡ Instant profile card generation
- 🤖 AI-powered profile analysis
- 🎨 Dynamic themed developer cards
- 📊 GitHub statistics visualization
- 🔗 Shareable card links
- 📱 QR code support
- 🧠 MCP tool integration
- 🚀 FastAPI backend
- 💻 Modern frontend UI

---

## ⚡ Workflow

1. User enters GitHub username
2. Frontend sends request to FastAPI backend
3. Backend fetches GitHub profile data
4. Gemini AI analyzes developer profile
5. MCP tools generate styled HTML card
6. Card gets saved and served dynamically

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JS, Nginx |
| Backend | Python, FastAPI, Uvicorn |
| AI/Agent | Google ADK, Gemini 1.5 Flash |
| MCP | MCP SDK (mcp[fastmcp]) |
| HTTP | httpx, requests |
| Infra | Docker, Docker Compose |

---

## 📂 Project Structure

```bash
github-card-generator/
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── mcp_server.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
└── preview.html
```

---

## 🚀 Getting Started

### 📌 Prerequisites

- Docker & Docker Compose
- GitHub Personal Access Token (optional)
- Google API Key

---

## ⚙️ Setup

### 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd github-card-generator
```

---

### 2️⃣ Configure Environment Variables

```bash
cp .env.example .env
```

Add:

```env
GITHUB_TOKEN=<your_github_token>

GOOGLE_API_KEY=<your_google_api_key>

GEMINI_MODEL=gemini-2.5-flash
```

---

### 3️⃣ Start Services

```bash
docker compose up --build
```

Open browser:

```bash
http://localhost
```

---

## 🖥 Running Backend Locally

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload --port 8080
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Health check |
| POST | /generate | Generate developer card |
| GET | /card/{username} | Serve generated card |

---

## 📬 Example API Request

### POST `/generate`

Request:

```json
{
  "username": "torvalds"
}
```

Response:

```json
{
  "status": "success",
  "card_url": "/card/torvalds",
  "card_html": "...",
  "profile_url": "https://github.com/torvalds"
}
```

---

## 🧠 MCP Server Tools

| Tool | Description |
|---|---|
| scrape_github | Fetch GitHub profile data |
| analyze_profile | AI-based developer analysis |
| generate_card_html | Generate styled HTML card |
| save_card | Save generated card |

---

## 🌱 Environment Variables

| Variable | Description |
|---|---|
| GITHUB_TOKEN | GitHub PAT for higher rate limits |
| GOOGLE_API_KEY | Google Gemini API key |
| GEMINI_MODEL | Gemini model name |
| BACKEND_URL | Backend service URL |

---

## 🚀 Future Improvements

- PNG card export
- Multiple themes
- Authentication
- GitHub OAuth
- Public card gallery
- Advanced analytics
- Social sharing integrations

---

## 👩‍💻 Author

Built with ❤️ by Sahithi7396

GitHub:
https://github.com/Sahithi7396

---

## ⭐ Support

If you like this project:

- Star the repository ⭐
- Fork the project 🍴
- Share it 🚀

---

## 📜 License

This project is open-source and free to use.
