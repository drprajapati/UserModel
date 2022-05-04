from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI
from typing import List
from uuid import uuid4
from model.model import Gender, Role, User

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
