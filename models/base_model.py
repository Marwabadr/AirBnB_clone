#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add this line to register the new instance

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()  # Add this line to save the updated state

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

    def __eq__(self, other):
        """
        Compare two BaseModel instances for equality

        Args:
            other: Another BaseModel instance

        Returns:
            bool: True if the instances are equal, False otherwise
        """
        return isinstance(
            other, BaseModel) and self.to_dict() == other.to_dict()
