#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes
    """

    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(s):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(s.__class__.__name__, s.id, s.__dict__)

    def save(self):
        """Update attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return all keys/values of __dict__ of the instance

        Returns:
            dict: Dictionary representation of the instance
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
