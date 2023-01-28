# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2023-01-28T19:34:24+00:00

from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI

from . import services
from .models import AuthLoginPostRequest, AuthLoginPostResponse, ListUsersRequest, User

app = FastAPI(
    title="Highload Research Project -- Social Network",
    version="0.1.0",
    servers=[
        {
            'url': 'https://{hostname}/',
            'variables': {'hostname': {'default': 'localhost'}},
        }
    ],
)


@app.post('/auth/login', response_model=AuthLoginPostResponse)
def user_login(body: AuthLoginPostRequest = None) -> AuthLoginPostResponse:
    return services.user_login(
        body,
    )


@app.post('/auth/signup', response_model=User)
def user_sign_up(body: User = None) -> User:
    return services.user_sign_up(
        body,
    )


@app.get('/users/', response_model=List[User])
def list_users(filters: Optional[ListUsersRequest] = None) -> List[User]:
    return services.list_users(
        filters,
    )


@app.get('/users/{id}', response_model=User)
def get_user(id: str) -> User:
    return services.get_user(
        id,
    )