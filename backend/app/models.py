from pydantic import BaseModel

class Player(BaseModel):
    id: str
    name: str
    score: int = 0
    position: int = 0  # Simple 1D position for demo

class GameState(BaseModel):
    players: dict = {}
    max_position: int = 10  # Example end of game
