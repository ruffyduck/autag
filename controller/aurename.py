"""Module for renaming files depending on user-defined patterns"""

import re
from os import rename
from controller.autag import AutoTag
from controller.filereader import get_directory

class AutoRename(AutoTag):
    """Class that allows user-defined file renaming with tags in file
    Example: '$ARTIST% - $TITLE%' would produce 'The Beatles - Yesterday'""" 

    def __init__(self, scheme="$TRACKNUMBER% $ARTIST% - $TITLE%"):
        super().__init__()
        
        self.scheme = scheme.replace("$", "[T]").replace("%", "[/T]")
        regex = r"\[T[^\]]*\](.*?)\[/T\]"
        self.tags = set()
        for tag in re.findall(regex, self.scheme):
            self.tags.add(tag)


    def set_auto_value(self, file=None):
        if file is None:
            return

        name = self.scheme
        for tag in self.tags:
            value = file.get_tag_value_by_name(tag)
            
            if not value is None:
                name = name.replace("[T]" + tag + "[/T]", value)
            else:
                name = name.replace("[T]" + tag + "[/T]", "")
                
        directory = get_directory(file.filename)
        newfilename = directory + '/' + name + file.get_file_extension()
        rename(file.filename, newfilename)
        file.update_filepath(newfilename)
