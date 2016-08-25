"""Provides functionality for basic tags"""

class BaseTag:
    """Class that represent a basic tag"""

    def __init__(self, name=None, tag=None):
        self.name = name
        self.tag = tag


TAGS = {}
TAGS["ALBUMARTIST"] = BaseTag("Album Artist", "ALBUMARTIST")
TAGS["TRACKNUMBER"] = BaseTag("#", "TRACKNUMBER")
TAGS["TOTALTRACKS"] = BaseTag("TT", "TOTALTRACKS")
TAGS["TRACKTOTAL"] = BaseTag("TT", "TRACKTOTAL")
TAGS["DISCNUMBER"] = BaseTag("$", "DISCNUMBER")
TAGS["DISCTOTAL"] = BaseTag("DT", "DISCTOTAL")
TAGS["TOTALDISCS"] = BaseTag("DT", "TOTALDISCS")
TAGS["ORGANIZATION"] = BaseTag("Label", "ORGANIZATION")
TAGS["CONTENTGROUP"] = BaseTag("Type", "CONTENTGROUP")
TAGS["RATING"] = BaseTag("R#", "RATING")
TAGS["ALBUM RATING"] = BaseTag("AR#", "ALBUM RATING")


def get_tag(name):
    """Get Tag by name"""
    name = name.upper()
    if not name in TAGS:
        create_tag(name)

    return TAGS[name]


def create_tag(tag):
    """Create new base tag with committed tag name"""
    name = tag.lower()
    nameli = list(name)
    nameli[0] = name[0].upper()
    name = ''.join(nameli)

    TAGS[tag] = BaseTag(name, tag)

