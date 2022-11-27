#!/usr/bin/python3
""" Place module that inherits from BaseModel """

from models.base_model import BaseModel


class Place(BaseModel):
    """defines a class Place, a subclass of BaseModel
    Attr:
        city_id: string - City.id
        user_id: string - User.id
        name: string - name
        description: string - description
        number_rooms: integer - number of rooms (default=0)
        number_bathrooms: integer - number of bathrooms (default=0)
        max_guest: integer - total number of guests (default=0)
        price_by_night: integer - price for the night
        latitude: float - latitude (default=0.0)
        longitude: float - logitude (default=0.0)
        amenity_ids: list of string - a list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
