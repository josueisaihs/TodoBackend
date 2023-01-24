from datetime import datetime
from pydantic import (
    BaseModel, 
    Field
)


class Todo(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=50
    )
    description: str = Field(
        min_length=0,
        max_length=500
    )
    active: bool = Field(
        default=False
    )
    tags: list[str] = Field(
        max_items=5
    )

    @property
    def toggle_active(self) -> bool:
        self.active = not self.active
        return self.active


class TodoRegistered(Todo):
    id: str = Field(
        min_length=12,
        max_length=24
    )