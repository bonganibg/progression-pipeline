from pydantic import BaseModel


class BootcampTask(BaseModel):
    id: int
    bootcamp_id: int
    task_id: int
    is_mandetory: bool
    number: int