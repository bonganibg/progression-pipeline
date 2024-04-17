from pydantic import BaseModel

class ScraperConfig(BaseModel):
    bootcamp: str
    students: list[str]