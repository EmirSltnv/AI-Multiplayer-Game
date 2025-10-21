# AI Multiplayer Game

A real-time multiplayer game with AI bots, built with **FastAPI** (backend) and **React** (frontend).  
Features:
- WebSocket real-time communication
- Simple AI bot moves
- Game state management
- Expandable architecture for reinforcement learning, matchmaking, and leaderboards

## Installation

### Backend
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r app\requirements.txt
uvicorn app.main:app --reload
