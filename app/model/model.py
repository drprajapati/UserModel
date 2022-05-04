from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

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