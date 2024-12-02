from pydantic import BaseModel


class RemoveImageByIdRequestSchema(BaseModel):
    id: int
