from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class NodeState(BaseModel):
    user_input: str
    user_id: str
    history: Optional[List[Dict[str, Any]]] = []
    agent_response: Optional[str] = None
    agent_called: Optional[str] = None
