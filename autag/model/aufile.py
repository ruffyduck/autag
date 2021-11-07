"""Provides class for basic music files"""

from autag.model.basetag import get_tag

class AuFile:
    """Class that represents music files"""

    def __init__(self, fileName = None, audio = None):
        self.filename = fileName
        self.audio = audio
        self._tags = {}
        self.del_flag = False
        self.read_tags()

    def read_tags(self):
        """Read and import all tags for file"""
        if self.audio.tags is None:
            return

        for tag in self.audio.tags:
            basetag = get_tag(tag[0])
            self._tags[basetag] = tag[1]

    def get_tag_value(self, basetag):
        """Get value of commited base tag"""
        if basetag not in self._tags:
            self._tags[basetag] = None

        return self._tags[basetag]

    def get_tag_value_by_name(self, tagname):
        """Get value by tags name"""
        basetag = get_tag(tagname)
        return self.get_tag_value(basetag)

    def tag_iterator(self):
        """Returns an iterator of the file's tags"""
        return iter(self._tags)

    def _write_audio_tag(self, tag, value):
        """Write tag into the underlying file structure"""
        raise NotImplementedError


    def write_tag(self, basetag, value):
        """Write value of tag"""
        if value is None or len(value) is 0:
            self.delete_tag(basetag)

        oldVal = self.get_tag_value(basetag)
        if oldVal != value:
            self._tags[basetag] = value
            self._write_audio_tag(basetag.tag, value)

    def delete_tag(self, basetag):
        """Deletes tag from file"""
        value = self._tags[basetag]
        if basetag in self._tags and value is not None and not len(value) is 0:
            del self._tags[basetag]
            self.del_flag = True

    def save_changes(self):
        """Save all additions/deletions to file"""

        if self.del_flag:
            self.del_flag = False
            self.audio.delete()
            for tag in self._tags:
                if not self._tags[tag] is None:
                    self._write_audio_tag(tag.tag, self._tags[tag])

        self.audio.save()

    def print_tags(self):
        """Output all tags of file"""
        print(self.audio.tags)

    def update_filepath(self, filepath):
        """Updates file path of this file"""
        raise NotImplementedError

    def get_images(self):
        """Get a list of all embedded images"""
        raise NotImplementedError

    def add_image(self, imagefile, covertype = 3):
        """Adds album art to the file depending on type
        e.g. type 3 means front cover"""
        raise NotImplementedError

    def remove_images(self):
        """Removes all images from file"""
        raise NotImplementedError

    def get_file_extension(self):
        """Returns extension of file"""
        raise NotImplementedError
