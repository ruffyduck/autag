"""Provides class for basic music files"""

from abc import abstractmethod
from model.basetag import get_tag

class AuFile:
    """Class that represents music files"""

    def __init__(self, fileName=None, audio=None):
        self.filename = fileName
        self.audio = audio
        self.__tags = {}

        self.read_tags()


    def read_tags(self):
        """Read and import all tags for file"""
        if self.audio.tags is None:
            return

        for tag in self.audio.tags:
            basetag = get_tag(tag[0])
            self.__tags[basetag] = tag[1]


    def get_tag_value(self, basetag):
        """Get value of commited base tag"""
        if not basetag in self.__tags:
            self.__tags[basetag] = None

        return self.__tags[basetag]


    def get_tag_value_by_name(self, tagname):
        """Get value by tags name"""
        basetag = get_tag(tagname)
        return self.get_tag_value(basetag)


    def tag_iterator(self):
        """Returns an iterator of the file's tags"""
        return iter(self.__tags)


    def write_tag(self, basetag, value):
        """Write value of tag"""
        self.__tags[basetag] = value
        self.audio[basetag.tag] = value


    def delete_tag(self, basetag):
        """Deletes tag from file"""
        if basetag in self.__tags:
            del self.__tags[basetag]


    def save_changes(self):
        """Save all additions/deletions to file"""
        self.audio.delete()

        for tag in self.__tags:
            if not self.__tags[tag] is None:
                self.audio[tag.tag] = self.__tags[tag]

        self.audio.save()


    def print_tags(self):
        """Output all tags of file"""
        print(self.audio.tags)


    @abstractmethod
    def update_filepath(self, filepath):
        """Updates file path of this file"""
        pass


    @abstractmethod
    def get_images(self):
        """Get a list of all embedded images"""
        pass


    @abstractmethod
    def add_image(self, imagefile, covertype=3):
        """Adds album art to the file depending on type
        e.g. type 3 means front cover"""
        pass


    @abstractmethod
    def remove_images(self):
        """Removes all images from file"""
        pass

    @abstractmethod
    def get_file_extension(self):
        """Returns extension of file"""
        pass   
