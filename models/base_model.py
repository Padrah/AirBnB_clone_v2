#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    value = datetime.strptime(value, dtime_format)
                if key == 'updated_at':
                    value = datetime.strptime(value, dtime_format)
                setattr(self, key, value)
        else:
            models.storage.new(self)  # as instructed also in task 5 for new instance

    def __str__(self):
        """Returns a readable string representation
        of BaseModel instances"""

        clsName = self.__class__.__name__
        return "[%s] (%s) %s" % (clsName, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all
        keys/values of the instance"""

        clsName = self.__class__.__name__
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = clsName

        return my_dict
