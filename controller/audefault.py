"""Module for default tagging values"""

import json
from autag.controller.autag import AutoTag
from autag.model.basetag import get_tag


class AutoDefault(AutoTag):
    """Class that enables user-defined default values for specific tags"""

    def __init__(self, scheme):
        super().__init__()

        self.dict = {}
        with open(scheme, "r") as jsondata:
            data = json.load(jsondata)

            for defaultdat in data:
                defaultdata = data[defaultdat]
                for tags in defaultdata:
                    for tag in tags:
                        self.dict[get_tag(tag)] = tags[tag]

    def set_auto_value(self, file=None):
        if file is None:
            return

        for tag in self.dict:
            file.write_tag(tag, self.dict[tag])
