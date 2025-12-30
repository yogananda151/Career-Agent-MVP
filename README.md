🚀 CareerFlow.ai - The Agentic Career Co-Pilot

Team Name: Tech Stars
Track: Agentic AI
Focus: AI-Driven Career Development & Feedback Loops

📖 Project Overview

CareerFlow.ai is an Autonomous Agentic AI System designed to solve the "Translation Gap" students face between raw skills and market employability.

Unlike static job boards, this system acts as a proactive career co-pilot that:

Reasons over real-time market data.

Plans personalized learning roadmaps (Micro-Sprints).

Acts by autonomously drafting emails and applications.

Learns from user failures (Interview Post-Mortems).

🛠 Key Features (MVP)

📄 AI Profiler Agent: Parses PDF resumes, extracts skills, and calculates a "Match Score" against target roles.

🌍 Real-Time Market Scout: Scans for Jobs, Internships, and Hackathons that match the user's current skill level.

✉️ Action Agent: Autonomously drafts high-impact cold emails and cover letters tailored to recruiters.

🔄 Active Feedback Loop: A unique module that analyzes failed interview questions to instantly update the user's learning roadmap.

🎤 Mock Interview Simulator: An AI-driven chat interface for practicing technical questions before the real interview.

📂 Project Structure

CareerFlow-AI/
├── app.py                # The main application file containing all Agent logic
├── requirements.txt      # List of all Python libraries used
├── README.md             # Project documentation
└── .gitignore            # Security file to protect API keys


⚙️ Tech Stack

Frontend: Streamlit (Python)

AI Engine: Google Gemini 1.5 Flash

Orchestration: Python-based Agentic Workflow

Data Processing: pypdf (Resume Parsing), Vector Memory concepts.

🚀 How to Run Locally

Clone the Repository

git clone [https://github.com/techstars/careerflow.git](https://github.com/techstars/careerflow.git)
cd careerflow


Install Dependencies

pip install streamlit google-generativeai pypdf


Add API Key

Open app.py.

Paste your Google Gemini API Key where indicated: GOOGLE_API_KEY = "YOUR_KEY_HERE".

Run the App

streamlit run app.py


🔮 Future Roadmap

Phase 2: LinkedIn Integration & Alumni Connector Agent.

Phase 3: Video Analysis for Soft-Skills Coaching (Eye contact & confidence scoring).

Submitted for AI-Verse Hackathon 2025
