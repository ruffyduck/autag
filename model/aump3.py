"""Module that provides mp3 file functionality"""

from mutagen.id3 import ID3
#from mutagen.flac import Picture
from model.aufile import AuFile

class AuMP3(AuFile):
    """Class that represents music files in mp3 format"""

    def __init__(self, filename=None):
        super().__init__(filename, ID3(filename))


    def get_images(self):
        pass


    def add_image(self, imagefile, covertype=3):
        pass


    def remove_images(self):
        pass


    def get_file_extension(self):
        return ".mp3"
