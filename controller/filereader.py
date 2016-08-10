"""Module provides functionality for file management"""

from os import listdir, remove, path
from shutil import rmtree
from fnmatch import fnmatch
from model.auflac import AuFlac

MUSICFLAGS = [".flac"]
IMAGEFLAGS = [".png", ".jpg"]


def build_aufile(filepath):
    """Create an AuFile from given filepath"""
    if filepath.endswith(".flac"):
        return AuFlac(filepath)

    return None


def build_aufiles(directory):
    """Create AuFiles from music files in given directory"""
    aufiles = []
    musicfiles = list_files(directory, MUSICFLAGS)

    for musicfile in musicfiles:
        aufile = build_aufile(musicfile)

        if not aufile is None:
            aufiles.append(aufile)

    return aufiles


def list_files(filepath, flags=None):
    """Lists all files in committed path"""
    filelist = []

    for file in listdir(filepath):
        if check_flags(file, flags):
            filelist.append(filepath + "/" + file)

    return filelist


def count_files(filepath, flags):
    """Count files in committed path"""
    counter = 0

    for file in listdir(filepath):
        if check_flags(file, flags):
            counter += 1

    return counter


def clean_directory(filepath, flags=None):
    """Remove all files in committed path depending on commited flags"""
    for file in listdir(filepath):
        if not check_flags(file, flags):
            delete_file(filepath + "/" + file)


def check_flags(file, flags):
    """Check file for committed flags"""
    if flags is None:
        return True

    for flag in flags:
        wildcard = "*" + flag
        if fnmatch(file, wildcard):
            return True

    return False

def get_directory(file):
    """Returns the diretory of given file"""
    return path.dirname(file)


def delete_file(file):
    """Delete commited file or directory"""
    try:
        remove(file)
    except OSError:
        rmtree(file)
