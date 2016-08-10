"""Provides basic auto tag class"""

from abc import abstractmethod

class AutoTag:
    """Abstract base class for auto tags"""

    def __init__(self, tag=None):
        self.tag = tag


    def set_base_tag(self, basetag):
        """Set underlying base tag"""
        self.tag = basetag


    @abstractmethod
    def set_auto_value(self, file):
        """Generates an automatic value for given file/tag"""
        pass
