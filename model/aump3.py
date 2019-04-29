"""Module that provides mp3 file functionality"""

from mutagen.mp3 import EasyMP3, MP3
from mutagen.id3 import APIC
from autag.model.basetag import get_tag
from autag.model.aufile import AuFile


class AuMP3(AuFile):
    """Class that represents music files in mp3 format"""

    def __init__(self, filename=None):
        super().__init__(filename, EasyMP3(filename))
        self.__mp3 = MP3(filename)
        self.__valid_keys = ["title", "artist", "albumartist", "album",
                             "genre", "date", "organization",
                             "tracknumber", "discnumber"]

    def read_tags(self):
        if self.audio.tags is None:
            return

        for tag in self.audio.tags:
            basetag = get_tag(tag)
            self._tags[basetag] = self.audio[tag][0]

    def _write_audio_tag(self, tag, value):
        tag = tag.lower()

        if tag in self.__valid_keys:
            self.audio[tag.lower()] = value

    def update_filepath(self, filepath):
        self.filename = filepath
        self.audio = EasyMP3(filepath)

    def get_images(self):
        images = [tag for tag in self.__mp3.keys() if 'APIC' in tag]
        return images

    def add_image(self, imagefile, covertype=3):
        image = APIC()
        image.type = covertype

        with open(imagefile, 'rb') as fstream:
            image.data = fstream.read()

        self.__mp3.tags.add(image)
        self.__mp3.save()

    def remove_images(self):
        images = [tag for tag in self.__mp3.keys() if 'APIC' in tag]
        for image in images:
            del self.__mp3[image]

        self.__mp3.save()

    def get_file_extension(self):
        return ".mp3"
