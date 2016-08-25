"""Module that provides mp3 file functionality"""

from mutagen.mp3 import EasyMP3 as MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from model.basetag import get_tag
from model.aufile import AuFile

class AuMP3(AuFile):
    """Class that represents music files in mp3 format"""

    def __init__(self, filename=None):
        super().__init__(filename, MP3(filename))
        self.__valid_keys = ["title", "artist", "albumartist", "album", "genre",
                             "date", "organization", "tracknumber", "discnumber"]


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
        else:
            print("Tag '" + tag + "' not supported in mp3")


    def update_filepath(self, filepath):
        self.filename = filepath
        self.audio = MP3(filepath)

        
    def get_images(self):
        pass


    def add_image(self, imagefile, covertype=3):
        pass


    def remove_images(self):
        pass


    def get_file_extension(self):
        return ".mp3"
