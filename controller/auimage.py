"""Module that provides the auto image tagging class"""

from autag.controller.autag import AutoTag
from autag.controller.filereader import get_directory, delete_file, list_files


class AutoImage(AutoTag):
    """Class for automatically assigning images in the same directory
    as album art to files. Images will be picked in alphabetical order"""

    def __init__(self, flags=[".png", ".jpg"]):
        super().__init__()
        self.flags = flags


    def set_auto_value(self, file=None):
        if file is None:
            return
        
        directory = get_directory(file.filename)
        imagefiles = list_files(directory, self.flags)

        if len(imagefiles) > 0:
            imagefile = imagefiles[0]

            file.remove_images()
            file.add_image(imagefile, 3)
