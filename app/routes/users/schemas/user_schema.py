import re

from pydantic import BaseModel, field_validator


class UserBase(BaseModel):
    email: str

    """ @field_validator('email')
    def validate_email(cls, value):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(regex, value):
            return ValueError("Email invalid") #melhorar esse return nao ta subindo pra viewe
        return value """


class UserCreate(UserBase):
    password: str
    email: str
    name: str
    document_number: str


class UserSchema(UserBase):
    id: int
    is_active: bool


class UserLogin(UserBase):
    password: str
