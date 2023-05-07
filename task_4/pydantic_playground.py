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
print(data)

class User(BaseModel):
    name: str
    email: str
    age: int
    city: Optional[str]

    @validator("name")
    @classmethod
    def validate_name(cls, name):
        pass


# for entry in data:

#     try:

#     a = User(name=entry["name"],email=entry["email"], age=entry["age"], city=entry["city"] )


