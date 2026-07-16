from fastapi import FastAPI, Path, Header, Depends
from pydantic import BaseModel, Field, field_validator

from api.routes import user
from dependencies.page import common

app = FastAPI() 

app.include_router(user.router)


class LoginSchema(BaseModel):
    username: str = Field(..., description="用户名", min_length=6)
    password: str = Field(..., description="密码", min_length=6, max_length=20)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("密码长度不能小于6")
        return v


@app.get("/", summary="首页")
async def read_root():
    return {"Hello": "World"}


@app.get("/item/{item_id}")
async def item_detail(item_id: int = Path(gt=2, description="测试")):
    return {"item_id": item_id}


@app.post("/login")
async def login(login_schema: LoginSchema):
    return {"username": login_schema.username, "password": login_schema.password}


@app.get("/userinfo")
async def userinfo(authorization: str = Header()):
    return {"authorization": authorization}


@app.get("/page")
async def page(common_data: dict = Depends(common)):
    return {"common_data": common_data}
