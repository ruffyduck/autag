"""Helper module that provides functionality for file and directory management"""

from os import listdir, remove, path, rmdir
from shutil import rmtree, move
from fnmatch import fnmatch
from model.auflac import AuFlac
from model.aump3 import AuMP3

MUSICFLAGS = [".flac", ".mp3"]
IMAGEFLAGS = [".png", ".jpg"]
AUFILES = {}


def get_aufile(filepath):
    """Returns an AuFile from given filepath"""

    aufile = AUFILES.get(filepath)
    if not aufile is None:
        return aufile

    if filepath.endswith(".flac"):
        aufile =  AuFlac(filepath)
    elif filepath.endswith(".mp3"):
        aufile = AuMP3(filepath)
        
    if not aufile is None:
        AUFILES[aufile.filename] = aufile
        
    return aufile


def get_aufiles(directory):
    """Returns AuFiles from music files in given directory"""
    aufiles = []
    musicfiles = list_files(directory, MUSICFLAGS)

    for musicfile in musicfiles:
        aufile = get_aufile(musicfile)

        if not aufile is None:
            aufiles.append(aufile)

    return aufiles


def move_aufile(filesrc, filetarget):
    """Moves AuFile to target directory and updates file paths internally.
    Directory must exist"""
    file = get_aufile(filesrc)

    if not file is None:
        move(filesrc, filetarget)
        file.filename = filetarget
        AUFILES[filetarget] = file

        if not AUFILES.get(filesrc) is None:
            del[AUFILES[filesrc]]


def list_files(directory, flags=None, reverse_flags=False):
    """Lists all files in committed path"""
    filelist = []

    for file in listdir(directory):
        if check_flags(file, flags) != reverse_flags:
            filelist.append(directory + "/" + file)

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


def delete_empty_directories(directory, child=None):
    """Deletes given directory and its parent directories if they are empty"""
    if not path.exists(directory):
        return
    
    files = list_files(directory)
    #Delete folder if it is empty
    if len(files) is 0:
        rmdir(directory)
        delete_empty_directories(get_directory(directory), directory)
    #Delete folder if the only content is the previously deleted folder.
    #This is necessary because that folder might not be deleted in time.
    elif len(files) is 1 and files[0] == child:
        rmtree(diretory)
        delete_empty_directories(get_directory(directory), directory)


def delete_file(file, del_children=False):
    """Delete commited file or directory"""
    try:
        remove(file)
    except OSError:
        if del_children:
            rmtree(file)
