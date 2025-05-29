from dataclasses import dataclass
from app.models.receipt import Receipt

@dataclass(slots=True)
class User:
    session_id : str
    receipt : Receipt = None
    points : int = 0