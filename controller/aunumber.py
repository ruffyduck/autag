"""Class for automatically indexing music files"""

from controller.autag import AutoTag
from controller.filereader import list_files, MUSICFLAGS
from model.basetag import get_tag

class AutoNumbers(AutoTag):
    """Class that can set track numbers automatically.
    Numbering dependings on amount of files given in corresponding method"""

    def __init__(self):
        super().__init__()
        self.numbtag = get_tag("TRACKNUMBER")
        self.totatag = get_tag("TRACKTOTAL")


    def set_auto_value(self, file=None):
        if file is None:
            return

        file.write_tag(self.numbtag, "1")
        file.write_tag(self.totatag, "1")


    def multiset_auto_value(self, files=None):
        if files is None:
            return

        total = str(len(files))
        count = 1
        for file in files:
            file.write_tag(self.numbtag, str(count))
            file.write_tag(self.totatag, total)
            count += 1


    def directory_auto_value(self, directory=None):
        if directory is None:
            return

        files = list_files(directory, MUSICFLAGS)
        self.multiset_auto_value(files)
