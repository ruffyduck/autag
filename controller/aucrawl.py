"""Module that provides auto tagging via crawling the music library Discogs"""

import discogs_client
from controller.autag import AutoTag
from controller.filereader import get_aufiles
from model.basetag import get_tag

class AutoCrawler(AutoTag):
    """Class that can tag via crawling Discogs. Artist and album tags have to be available
    to produce the results in the database. Tags that can be crawled currently: 
    Genre, Label, Year"""

    def __init__(self, token, tags, filtermask={}):
        self.tags = tags
        self.client = discogs_client.Client("AuTag", user_token=token)
        self.filtermask = filtermask

    def __get_tag_value(self, master, tag):
        if tag.tag in self.filtermask:
            mask = self.filtermask[tag.tag]
        else:
            mask = None

        if tag is get_tag("GENRE"):
            if not master.styles is None:
                for genre in master.styles:
                    if not mask is None and genre in mask:
                        return mask[genre]
        elif tag is get_tag("ORGANIZATION"):
            release = master.main_release
            if not release.labels is None:
                return release.labels[0].name
        elif tag is get_tag("DATE"):
            release = master.main_release
            return release.year

        return None

    def __get_master(self, file):
        artist = file.get_tag_value_by_name("ARTIST")
        album = file.get_tag_value_by_name("ALBUM")

        if artist is None or album is None:
            return

        results = self.client.search(artist + ' ' + album, type='master')

        if len(results) is 0:
            return None

        return results[0]

    def set_auto_value(self, file=None):
        if file is None:
            return

        master = self.__get_master(file)

        if master is not None:
            for tag in self.tags:
                value = self.__get_tag_value(master, tag)
                if value is not None:
                    file.write_tag(tag, value)

    def multiset_auto_value(self, files=None):
        if files is None or len(files) is 0:
            return

        protofile = files[0]
        master = self.__get_master(protofile)

        if master is not None:
            for tag in self.tags:
                value = self.__get_tag_value(master, tag)
                if value is not None:
                    for file in files:
                        file.write_tag(tag, value)

    def directory_auto_value(self, directory=None):
        if directory is None:
            return

        files = get_aufiles(directory)
        self.multiset_auto_value(files)
