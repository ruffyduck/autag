"""Module for cleaning directories"""

from autag.controller.autag import AutoTag
from autag.controller.filereader import get_directory, delete_file
from autag.controller.filereader import list_files, MUSICFLAGS


class AutoCleanup(AutoTag):
    """Class that can cleanup music directories of unwanted files.
    Flags can be user-defined to keep certain files."""

    def __init__(self, flags = [".log", ".m3u"]):
        super().__init__()
        self.flags = flags + MUSICFLAGS

    def __remove_files(self, directory):
        files = list_files(directory, self.flags, True)
        for tfile in files:
            delete_file(tfile, True)

    def set_auto_value(self, file = None):
        if file is None:
            return

        directory = get_directory(file.filename)
        self.__remove_files(directory)

    def directory_auto_value(self, directory = None):
        if directory is None:
            return

        self.__remove_files(directory)
