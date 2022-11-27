#!/usr/bin/python3
""" User module which inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """defines a class User, a subclass of BaseModel
    Attr:
        email: (string) email of the user
        password: (string) password of the user
        first_name: (string) the user's first name
        last_name: (string) the user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
