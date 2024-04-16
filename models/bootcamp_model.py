from pydantic import BaseModel


class Bootcamp(BaseModel):
    id: int
    name: str
