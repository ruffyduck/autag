"""Module for automatic folder organization of music files"""

import os
import re
import shutil
from autag.tagging.autag import AutoTag
from autag.io.filereader import get_directory, delete_empty_directories
from autag.io.filereader import list_files
from autag.io.filereader import get_aufile, move_aufile, MUSICFLAGS


class AutoMove(AutoTag):
    """Class that allows automatic moving of files into
    user-defined folder structures"""

    def __init__(self, parentdirectory = "",
                 scheme = "$GENRE%/$ARTIST%/$DATE% - $ALBUM%/",
                 keepfiles = [".log", ".m3u"]):
        super().__init__()

        self.keepfiles = keepfiles
        self.scheme = scheme
        if not self.scheme.endswith('/'):
            self.scheme = self.scheme + '/'
        if parentdirectory != "":
            self.scheme = parentdirectory + '/' + self.scheme

        self.scheme = self.scheme.replace("$", "[T]").replace("%", "[/T]")
        regex = r"\[T[^\]]*\](.*?)\[/T\]"
        self.tags = set()
        for tag in re.findall(regex, self.scheme):
            self.tags.add(tag)

    def __build_scheme_path(self, file):
        """Builds and returns file path for given file with the
        defined scheme"""
        fpath = self.scheme
        for tag in self.tags:
            value = file.get_tag_value_by_name(tag)

            if value is not None:
                fpath = fpath.replace("[T]" + tag + "[/T]", value)
            else:
                fpath = fpath.replace("[T]" + tag + "[/T]", "_")

        if not os.path.exists(fpath):
            os.makedirs(fpath)

        return fpath

    def __move_other_files(self, directory, targetdir):
        otherfiles = list_files(directory, self.keepfiles)

        for file in otherfiles:
            pair = os.path.split(file)
            filename = pair[1]
            filesrc = targetdir + filename
            shutil.move(file, filesrc)

    def set_auto_value(self, file = None):
        if file is None:
            return

        fpath = self.__build_scheme_path(file)
        filedir, filename = os.path.split(file.filename)
        filesrc = fpath + filename

        if self.keepfiles is not None:
            self.__move_other_files(get_directory(file.filename), fpath)

        move_aufile(file.filename, filesrc)
        delete_empty_directories(filedir)

    def directory_auto_value(self, directory = None):
        if directory is None:
            return

        musicfiles = list_files(directory, MUSICFLAGS)
        if len(musicfiles) is 0:
            return

#       Choose one of the music files to determine the
#       moving scheme for all of them
        mfile = get_aufile(musicfiles[0])
        fpath = self.__build_scheme_path(mfile)

        for filename in musicfiles:
            filedir, only_filename = os.path.split(filename)
            filesrc = fpath + only_filename

            move_aufile(filename, filesrc)

        self.__move_other_files(directory, fpath)
        delete_empty_directories(filedir)
