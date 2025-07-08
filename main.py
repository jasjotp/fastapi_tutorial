from fastapi import FastAPI, HTTPException
from typing import List 
from models import User, Gender, Role, updateUser
from uuid import uuid4, UUID
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
import json 

# create an intstance of the application 
app = FastAPI()

# initialize the database 
db: List[User] = [
    User(
        id = UUID('99b194eb-d2e7-483b-94a8-a175b6ca5f32'), 
        first_name = 'Jamila',
        last_name = 'Ahmed',
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(  
        id = UUID('5b7f9e88-d695-4a23-b731-7dd365d5ba36'), 
        first_name = 'Alex',
        last_name = 'Jones',
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

# open a route for a GET request
@app.get("/")
# async / await = non-blocking I/O:
# while this coroutine waits on a slow task (HTTP call, SQL query, file read, etc.)
# the event loop can switch to other requests, so one worker handles many connections at once
async def root():
    return {"Hello: Jasjot"}

# GET request to get the list of users 
@app.get("/api/v1/users")
async def fetch_users():
    pretty_json = json.dumps(jsonable_encoder(db, exclude_none = True), indent = 2)
    return Response(content = pretty_json, media_type = "application/json")  

# POST request to add a new user to the list of users 
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}  

# DELETE request to be able to delete users 
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    # if the user is not in the database (if that user was deleted, raise an Exception and 404 error)
    raise HTTPException(
        status_code = 404, # status code client should see 
        detail = f'user with id: {user_id} does not exist' # message client should see 
    )

# PUT request method to be able to update an exisiing user in our database
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: updateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return 
    raise HTTPException(
        status_code = 404,
        detail = f'user with id: {user_id} does not exist'
    )

