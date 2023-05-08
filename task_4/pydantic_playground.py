# Pydantic task
# Task: Create a Python script
# that takes a JSON file with user data,
# validates and processes the data using Pydantic,
# and prints the valid users and their details in a formatted output.
import json
from pydantic import BaseModel, validator
from typing import Optional

json_file = open("users.json")

data = json.load(json_file)


class User(BaseModel):
    name: str
    email: str
    age: int
    city: Optional[str]

    @validator("name")
    @classmethod
    def validate_name(cls, name):
        if name.islower():
            raise ValueError(f"The name needs to start with a capital letter, name given: {name}")
        else:
            return name

    @validator("age")
    @classmethod
    def validate_age(cls, age):
        if age <= 0:
            raise ValueError(f"The age needs to be higher than 0, age given: {age}")
        else:
            return age


def validator(data):
    for entry in data:
        
        User(
            name=entry["name"],
            email=entry["email"],
            age=entry["age"],
            city=entry["city"],
        )

    print("EVERYTHING IS VALID")


if __name__ == "__main__":
    validator(data)
