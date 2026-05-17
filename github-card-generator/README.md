# 🚀 GitHub Dev Card Generator

An AI-powered GitHub Dev Card Generator that analyzes public GitHub profiles and creates beautiful developer cards automatically.

Built using:

- FastAPI
- React
- Tailwind CSS
- Gemini AI
- MCP Tools
- Google ADK

---

# ✨ Features

- 🔍 Fetch public GitHub profile data
- 🤖 AI-generated developer analysis
- 🎨 Beautiful developer cards
- 📊 Top repositories display
- 🧠 Skill detection
- 🌙 Modern dark UI
- ⚡ FastAPI backend
- 💻 React frontend

---

# 📂 Project Structure

```bash
github-card-generator/
│
├── backend/
│   ├── main.py
│   ├── mcp_server.py
│   ├── agent.py
│   ├── requirements.txt
│   ├── static/
│   │   └── cards/
│   └── .venv/
│
├── frontend/
│   └── index.html
│
├── docker-compose.yml
└── README.md
⚙️ Backend Setup
1️⃣ Open terminal

Go to backend folder:
cd backend
2️⃣ Create virtual environment
python -m venv .venv
3️⃣ Activate virtual environment
Windows
.venv\Scripts\activate
4️⃣ Install dependencies
pip install -r requirements.txt
5️⃣ Run FastAPI backend
uvicorn main:app --reload --port 8080

Backend runs at:

http://127.0.0.1:8080

Swagger API docs:

http://127.0.0.1:8080/docs
🎨 Frontend Setup

Open frontend using VS Code Live Server.

Frontend URL:

http://127.0.0.1:5500/frontend/index.html
🔥 How It Works
User enters GitHub username
Frontend sends request to backend
Backend fetches GitHub profile data
Gemini AI analyzes profile
MCP generates developer card
Card gets saved inside:
backend/static/cards/
Generated card becomes accessible through:
http://localhost:8080/static/cards/<username>.html

Example:

http://localhost:8080/static/cards/Sahithi7396.html
📡 API Endpoint
Generate Card
POST
/generate?username=<github_username>

Example:

http://localhost:8080/generate?username=torvalds
🧠 Tech Stack
Technology	Purpose
FastAPI	Backend API
React	Frontend UI
Tailwind CSS	Styling
Gemini AI	Profile Analysis
MCP	Tool orchestration
Google ADK	Agent workflow
GitHub API	Profile data
🖼 Generated Card Includes
GitHub avatar
Developer vibe
Skills
Repo statistics
Top repositories
Dynamic themes
🚀 Future Improvements
Download card as PNG
Multiple themes
GitHub OAuth
Shareable links
Cloud deployment
Persistent AI memory
👩‍💻 Author

Built by Sahithi7396 💙

GitHub:
https://github.com/Sahithi7396

⭐ Support

If you like this project:

Star the repository ⭐
Fork the project 🍴
Share it 🚀
📜 License

This project is open-source and free to use.