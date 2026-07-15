from datetime import date

from pydantic import BaseModel, EmailStr, PositiveInt, Field, ConfigDict

class UserSchema(BaseModel):
    # ... 代表必填
    id: int = Field(..., description="用户Id")
    name: str = Field(..., description="用户名称")
    email: EmailStr = Field(..., description="用户邮箱")
    date_joined: date | None = Field(None, description="用户加入日期")
    tastes: dict[str, PositiveInt] = Field(..., description="用户口味")

    model_config = ConfigDict(from_attributes=True)


class UserModel:
    def __init__(
        self,
        id: int,
        name: str,
        email: EmailStr,
        date_joined: date | None = None,
        tastes: dict[str, PositiveInt] | None = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.date_joined = date_joined
        self.tastes = tastes


user_model = UserModel(id=1, name="张三", email="11@qq.com", tastes={"wine": 9})
user_schema1 = UserSchema.model_validate(user_model)
print(user_model)
print(user_schema1)
print(user_schema1.model_dump())
