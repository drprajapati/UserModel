from enum import Enum
from typing import List, Optional
from uuid import uuid4, UUID

from fastapi import FastAPI
from typing import List
from uuid import uuid4

from pydantic import BaseModel


class Gender(Enum):
    male = "male"
    female = "female"


class Role(Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    gender: Gender
    middle_name: Optional[str]
    last_name: str
    roles: List[Role]


api = FastAPI()

db: List[User] = [
    User(id=UUID("73c7b692-3742-4039-bcc4-22028d419d1b"),
         first_name="Darshan",
         last_name="Prajapati",
         roles=[Role.admin, Role.student],
         gender=Gender.male),

    User(id=UUID("64bc46d3-8e43-4037-943c-0157269a7e7c"),
         first_name="Deval",
         last_name="Prajapati",
         roles=[Role.user, Role.student],
         gender=Gender.female)
]


@api.get("/")
async def get_response():
    return {"message": "Student"}


@api.get("/users/")
async def get_users():
    return db


@api.post("/users/")
async def post_users(user: User):
    db.append(user)
    return {"id": user.id}


@api.delete("/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
