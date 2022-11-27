#!/usr/bin/python3
""" City module which inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """defines a class City, a subclass of BaseModel
    Attr:
        state_id: (string) state id of an instance (State.id)
        name: (string) city name
    """

    state_id = ""
    name = ""
