from pydantic import (
    BaseModel,
    Field,
    EmailStr
)

class UserBase(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        example="John"
    )
    lastname: str = Field(
        min_length=3,
        max_length=50,
        example="Snow"
    )
    email: EmailStr = Field(
        example="johnsnow@start.com"
    )

    @property
    def get_fullname(self):
        return f"{self.name.capitalize} {self.lastname.capitalize}"

class User(UserBase):
    password: str = Field(
        min_length=8,
        max_length=64
    )

class UserRegistered(User):
    id: str = Field(
        min_length=12,
        max_length=24
    )

