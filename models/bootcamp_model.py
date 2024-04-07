from pydantic import BaseModel


class Bootcamp(BaseModel):
    id: str
    name: str
