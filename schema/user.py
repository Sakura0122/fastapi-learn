from datetime import date

from pydantic import BaseModel, EmailStr, PositiveInt


class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    date_joined: date | None
    tastes: dict[str, PositiveInt]

user_dict = {
    "id": '123',
    "name": "张三",
    "email": "john@qq.com",
    "date_joined": "2023-01-01",
    "tastes": {"pizza": 5, "ice cream": 4, " burgers": 3}
}

user_schema = UserSchema(**user_dict)

print(user_schema)

print(user_schema.model_dump())
print(user_schema.model_dump_json())