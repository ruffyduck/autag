"""Module that provides auto tagging functionality"""

from controller.filereader import get_aufiles


class AutoTagger:
    """Class for tagging  files automatically"""

    def __init__(self):
        self.autags = []

    def add_auto_tag(self, autag):
        """Add single auto tag that should be executed by the auto tagger"""
        self.autags.append(autag)

    def add_auto_tags(self, autags):
        """Add an array of auto tags that should be executed
        by the auto tagger"""
        self.autags.extend(autags)

    def auto_tag_file(self, file):
        """Tag a file with all the comprised auto tags"""
        for autag in self.autags:
            autag.set_auto_value(file)

        file.save_changes()

    def auto_tag_files(self, files):
        """Tag an array of files with all the comprised auto tags"""
        for autag in self.autags:
            autag.multiset_auto_value(files)

        #for file in files:
        #    file.save_changes()

    def auto_tag_directory(self, directory):
        """Tag all music files in given directory"""
        files = get_aufiles(directory)

        for autag in self.autags:
            autag.directory_auto_value(directory)

        for file in files:
            file.save_changes()
