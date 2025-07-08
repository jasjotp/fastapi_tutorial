from pydantic import BaseModel # pydantic helps with data validation - we can declare the shape of our data with classes with attributes and pydantic can validate that schema
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum 

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    # list out attributes for each user 
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str 
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

# class to update user 
class updateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    roles: Optional[List[Role]] = None