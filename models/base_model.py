#!/usr/bin/python3
""" defines the BaseModel Class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines a class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Instantializes the class BaseModel
        Args:
            args: arfg no to be used
            kwargs: key/value arg (dictionary) to instantiate the class
        Attr:
            id: (str) unique ID
            created_at: date and time of creation
            updated_at: update time
        """

        if kwargs != {}:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or val == 'updated_at':
                        value = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    else:
                        setattr(self, key, val)
                """if key == 'created_at' or val == 'updated_at':
                    value = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue
                if key != "__class__":
                    setattr(self, key, val)"""
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string documentation of an instance"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the current time into the attr updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values\
                (__dict__ of an instance)"""

        dic = dict(self.__dict__)
        dic['__class__'] = type(self).__name__
        dic['id'] = self.id
        if type(self.updated_at) is str:
            dic['updated_at'] = self.updated_at
        else:
            dic['updated_at'] = self.updated_at.isoformat()
        if type(self.created_at) is str:
            dic['created_at'] = dic['created_at']
        else:
            dic['created_at'] = dic['created_at'].isoformat()

        return dic
