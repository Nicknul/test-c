from fastapi import APIRouter, HTTPException
from typing import List
from models import SearchRequest, UserDTO
from database import search_users_by_name

user_router = APIRouter()

@user_router.post("/search", response_model=List[UserDTO])
async def search_users(request: SearchRequest):
    try:
        rows = search_users_by_name(request.name)
        if not rows:
            raise HTTPException(status_code=404, detail="User not found")
        users = [UserDTO(**row) for row in rows]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
