from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["用户模块"])

@router.get('/')
def get_user():
    return {"user": "user"}
