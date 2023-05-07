# Pydantic task
# Task: Create a Python script 
# that takes a JSON file with user data, 
# validates and processes the data using Pydantic, 
# and prints the valid users and their details in a formatted output.
import json
from pydantic import BaseModel
from typing import Optional
json_file = open("users.json")

data = json.load(json_file)
print(data)

class Users(BaseModel):
    name: str
    email: str
    age: int
    city: Optional[str]
    