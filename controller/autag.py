"""Provides basic auto tag class"""

from abc import abstractmethod
from controller.filereader import list_files, MUSICFLAGS

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


    def multiset_auto_value(self, directory=None):
        """Generates automatic values for all files in given directory"""
        if directory is None:
            return

        files = list_files(directory, MUSICFLAGS)
        for file in files:
            self.set_auto_value(file)
