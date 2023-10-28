from typing import Optional

from pydantic import BaseModel, validator


class CreateUser(BaseModel):
    name: str
    password: str

    @validator("password")
    def secure_password(cls, value):
        if len(value) <= 8:
            raise ValueError("Password is short")
        return value


class UpdateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]
    token: str

    @validator("password")
    def secure_password(cls, value):
        if len(value) <= 8:
            raise ValueError("Password is short")
        return value


class CreateAnno(BaseModel):
    header: str
    description: str
    user_id: int
    token: str

    @validator("header")
    def len_header(cls, value):
        if len(value.split(" ")) > 5:
            raise ValueError("Header too long")
        return value

    @validator("description")
    def len_description(cls, value):
        if len(value) > 100:
            raise ValueError("Description too long")
        return value


class UpdateAnno(BaseModel):
    header: Optional[str]
    description: Optional[str]
    token: str

    @validator("header")
    def len_header(cls, value):
        if len(value.split(" ")) > 5:
            raise ValueError("Header too long")
        return value

    @validator("description")
    def len_description(cls, value):
        if len(value) > 100:
            raise ValueError("Description too long")
        return value


class DeleteAnnoUser(BaseModel):
    name: Optional[str]
    password: Optional[str]
    header: Optional[str]
    description: Optional[str]
    token: str
