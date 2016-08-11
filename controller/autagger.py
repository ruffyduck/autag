"""Module that provides auto tagging functionality"""

from controller.filereader import list_files, MUSICFLAGS

class AutoTagger:
    """Class for tagging  files automatically"""

    def __init__(self):
        self.autags = []


    def add_auto_tag(self, autag):
        """Add single auto tag that should be executed by the auto tagger"""
        self.autags.append(autag)


    def add_auto_tags(self, autags):
        """Add an array of auto tags that should be executed by the auto tagger"""
        self.autags.extend(autags)


    def auto_tag_file(self, file):
        """Tag a file with all the comprised auto tags"""
        for autag in self.autags:
            autag.set_auto_value(file)

        file.save_changes()


    def auto_tag_files(self, files):
        """Tag an array of files with all the comprised auto tags"""
        for file in files:
            self.auto_tag_file(file)


    def auto_tag_directory(self, directory):
        """Tag all music files in given directory"""
        for autag in self.autags:
            autag.multiset_auto_value(directory)

        files = list_files(directory, MUSICFLAGS)
        for file in files:
            file.save_changes()
