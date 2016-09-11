"""Module provides functionality for replacement tags"""

from controller.autag import AutoTag


class ReplaceTag(AutoTag):
    """Auto tag that replaces values in files depending
    on commited dictionary"""

    def __init__(self, dictionary=None, tag=None):
        super().__init__()
        self.tag = tag
        self.dictionary = dictionary

    def set_auto_value(self, file=None):
        if file is None:
            return

        if self.dictionary.partial:
            self.__replace_partial(file)
        else:
            self.__replace_complete(file)

    def __replace_partial(self, file):
        """Replaces only relevant portion of the tag"""
        value = file.get_tag_value(self.tag)

        if value is None:
            return

        for entry in self.dictionary:
            if (entry + ' ') in value:
                newval = value.replace(entry, self.dictionary[entry])
                file.write_tag(self.tag, newval)
                break

    def __replace_complete(self, file):
        """Replace the whole tag with value from dictionary"""
        value = file.get_tag_value(self.tag)

        if value in self.dictionary:
            newval = self.dictionary[value]
            file.write_tag(self.tag, newval)
