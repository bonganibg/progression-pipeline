from pydantic import BaseModel


class Submission(BaseModel):
    id: int
    bootcamp_task_id: int 
    score: int
    date: str
    status: str