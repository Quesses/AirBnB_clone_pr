#!/usr/bin/python3
""" Review module which inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """defines a class Review, a subclass of BaseModel
    Attr:
        place_id: (string) place id of an instance (Place.id)
        user_id: (string) user id of an instance (User.id)
        text: (string)
    """

    place_id = ""
    user_id = ""
    text = ""
