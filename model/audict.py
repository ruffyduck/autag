"""Module that provides functionality of automated dictionaries"""

import json
from model.basetag import get_tag


class AuDict(dict):
    """Dictionary for value correction"""

    def __init__(self, partial=False):
        super().__init__()
        self.tag = None
        self.partial = partial

    def set_base_tag(self, basetag):
        """Sets basic tag"""
        self.tag = basetag

    def add_auto_value(self, value, applicants):
        """Adds new auto value to dictionary"""
        for applicant in applicants:
            self[applicant] = value


def build_auto_dicts(jsonfile):
    """Build auto dictionaries from json"""
    dicts = {}

    with open(jsonfile, "r") as jsondata:
        data = json.load(jsondata)

    for dicti in data:
        partialstr = data[dicti]["partial"]
        partial = bool(partialstr == "True")
        dictlist = data[dicti]["list"]

        autodict = AuDict(partial)
        tag = get_tag(dicti)
        autodict.set_base_tag(tag)

        for dictdata in dictlist:
            value = dictdata["value"]
            applicants = dictdata["applicants"]
            autodict.add_auto_value(value, applicants)

        dicts[tag.tag] = autodict

    return dicts
