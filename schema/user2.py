from datetime import date

from pydantic import BaseModel, EmailStr, PositiveInt, Field


class UserSchema(BaseModel):
    # ... 代表必填
    id: int = Field(..., description="用户Id")
    name: str = Field(..., description="用户名称")
    email: EmailStr = Field(..., description="用户邮箱")
    date_joined: date | None = Field(None, description="用户加入日期")
    tastes: dict[str, PositiveInt] = Field(..., description="用户口味")


user_dict = {
    "id": "123",
    "name": "张三",
    "email": "john@qq.com",
    "tastes": {"pizza": 5, "ice cream": 4, " burgers": 3},
}

user_schema = UserSchema(**user_dict)
