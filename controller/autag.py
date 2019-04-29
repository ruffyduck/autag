"""Provides basic auto tag class"""

from autag.io.filereader import get_aufiles

class AutoTag:
    """Abstract base class for auto tags"""

    def __init__(self):
        pass

    def set_auto_value(self, file):
        """Generates an automatic value for given file/tag"""
        raise NotImplementedError

    def multiset_auto_value(self, files):
        """Generate automatic values for all given files"""
        for file in files:
            self.set_auto_value(file)

    def directory_auto_value(self, directory = None):
        """Generates automatic values for all files in given directory"""
        if directory is None:
            return

        files = get_aufiles(directory)
        for file in files:
            self.set_auto_value(file)
