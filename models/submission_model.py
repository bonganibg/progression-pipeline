from pydantic import BaseModel
from typing import Optional


class Submission(BaseModel):
    id: int = None
    bootcamp_task_id: int 
    score: Optional[int]
    date: str
    status: str