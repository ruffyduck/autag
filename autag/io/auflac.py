"""Module that provides flac file functionality"""

from mutagen.flac import FLAC
from mutagen.flac import Picture
from autag.io.aufile import AuFile


class AuFlac(AuFile):
    """Class that represents music files in FLAC format"""

    def __init__(self, filename = None):
        super().__init__(filename, FLAC(filename))

    def _write_audio_tag(self, tag, value):
        self.audio[tag] = value

    def update_filepath(self, filepath):
        self.filename = filepath
        self.audio = FLAC(filepath)

    def get_images(self):
        return self.audio.pictures

    def add_image(self, imagefile, covertype = 3):
        image = Picture()
        image.type = covertype

        with open(imagefile, 'rb') as fstream:
            image.data = fstream.read()

        self.audio.add_picture(image)
        self.audio.save()

    def remove_images(self):
        self.audio.clear_pictures()

    def get_file_extension(self):
        return ".flac"
