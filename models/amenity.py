#!/usr/bin/python3
""" Amenity module which inherits from BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines a class Amenity, a subclass of BaseModel
    Attr:
        name: (string) amenity name
    """

    name = ""
