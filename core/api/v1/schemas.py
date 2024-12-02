from pydantic import BaseModel, Field


class ApiResponse(BaseModel):
    data: dict = Field(default_factory=dict)
