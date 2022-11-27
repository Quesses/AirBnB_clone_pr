#!/usr/bin/python3
""" State module which inherits from BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """defines a class State, a subclass of BaseModel
    Attr:
        name: (string) state name
    """

    name = ""
