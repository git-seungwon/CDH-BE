from pydantic import BaseModel
from typing import Optional, List
import datetime

class TeamspaceChangeValue(BaseModel):
    user_id: int
    nickname: str
    email: str
    joinedat: datetime.datetime

class TeamspaceChange(BaseModel):
    user_id: int
    teamspace_id: int
    members: List[TeamspaceChangeValue]

class TeamspaceChangeResponse(BaseModel):
    user_id: int
    group_id: int
    
    