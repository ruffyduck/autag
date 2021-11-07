"""Module that provides automatic tag removal functionality"""

import json
from autag.tagging.autag import AutoTag
from autag.basetag import get_tag


class AutoRemoval(AutoTag):
    """Class that can remove tags automatically dependinding on flags"""

    def __init__(self, scheme = None):
        super().__init__()
        self.flags = set()

        if scheme is not None:
            self.read_flags(scheme)

    def read_flags(self, jsonfile):
        """Read flags from json file"""
        with open(jsonfile, "r") as jsondata:
            data = json.load(jsondata)

        for flagdata in data:
            flaglist = data[flagdata]

            for flag in flaglist:
                self.flags.add(get_tag(flag))

    def set_auto_value(self, file = None):
        if file is None:
            return

        rmtags = []
        for tag in file.tag_iterator():
            if tag not in self.flags:
                rmtags.append(tag)

        for tag in rmtags:
            file.delete_tag(tag)
