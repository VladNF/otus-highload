# generated by fastapi-codegen:
#   filename:  api/http.yaml
#   timestamp: 2023-02-04T16:29:18+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, EmailStr, Field, SecretStr


class User(BaseModel):
    user_id: Optional[str] = Field(None, description='Идентификатор пользователя')
    email: EmailStr = Field(
        ..., description='Адрес электронной почты', example='ivan@email.com'
    )
    first_name: str = Field(..., description='Имя', example='Иван')
    last_name: str = Field(..., description='Фамилия', example='Иванов')
    age: Optional[int] = Field(None, description='Возраст', example=18)
    bio: Optional[str] = Field(
        None, description='Интересы', example='Хобби, интересы и т.п.'
    )
    city: Optional[str] = Field(None, description='Город', example='Москва')


class SignUpRequest(User):
    password: Optional[SecretStr] = Field(None, example='qwerty')


class ListUsersRequest(BaseModel):
    first_name: Optional[str] = Field(
        None, description='Условие поиска по имени', example='Конст'
    )
    last_name: Optional[str] = Field(
        None, description='Условие поиска по фамилии', example='Оси'
    )
    offset: Optional[int] = Field(0, description='Начало страницы результата')
    limit: Optional[int] = Field(20, description='Размер страницы результата')


class LoginRequest(BaseModel):
    email: Optional[str] = Field(None, example='ivan@email.com')
    password: Optional[SecretStr] = Field(None, example='qwerty')


class LoginResponse(BaseModel):
    token: Optional[str] = Field(None, example='e4d2e6b0cde242c5aac30b8316f21e58')
