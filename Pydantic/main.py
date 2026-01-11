# Pydantic is a data validation library in python
from pydantic import BaseModel, EmailStr, field_validator, validate_email


class User(BaseModel):
    name: str
    email: str
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value



user = User(
    name="jack",
    email="archit@gmail.com",
    account_id=1234
)


user_data = {
    'name': "architect",
    'email': "aa3014@srmist.edu.in",
    'account_id': "123456"
#     It will not only validate your data but it will also try to convert your data to the correct data type.
}

user2 = User(**user_data)

# You will get tying hints in your IDE
print(user.name,user.email,user.account_id)

print(user)
# Pydantic comes with validation right out of the box it means that if your data has to fail then it will fail as early as possible.
print(user2)

# Pydantic provides builtin support for JSON validation.

user_json_str = user.model_dump_json()
print(user_json_str)

print(user2.model_dump_json())

# You can also get a Python Dictionary Object
user_dict = user.model_dump()
print(user_dict)

# If you have a JSON String that you want to convert back into a Pydantic model, you can use the parse_raw method.
json_str = '{"name": "jack", "email": "architarora70@gmail.com", "account_id": 12345456789}'
user = User.model_validate_json(json_str)

# Many of the old models are deprecated.
# ? As well as Pydantic sounds, the python comes with its own data modelling and type hinting capabilities on its own.

from dataclasses import dataclass

@dataclass
class Userdata:
    name: str
    email: str
    account_id: int
# It is very similar to pydantic, except instead of extending from base model class, you are using "@dataclass" decorator instead. but it does not do any data Validation or JSON serialization

