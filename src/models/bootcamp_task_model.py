from pydantic import BaseModel


class BootcampTask(BaseModel):
    id: int = None
    bootcamp_id: int
    task_id: int
    is_mandetory: bool = True
    number: int