from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field()
    password: str = Field()
    city: str = Field()
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    age: int = Field()
    country: str = Field()
    join_time: str = Field()
