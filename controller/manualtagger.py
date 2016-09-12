"""Module that provides manual tagging functionality"""


class ManualTagger:
    """Class that allows easy manual tagging of files"""

    def __init__(self):
        self._taggedfiles = set()

    def tag_file(self, file, tag, value):
        """Tag single file with single value"""
        file.write_tag(tag, value)
        self._taggedfiles.add(file)

    def clear_file(self, file, tag):
        """Remove tag from single file"""
        file.delete_tag(tag)
        self._taggedfiles.add(file)

    def multitag_file(self, file, tags):
        """Tag single file with multiple values
        tags elements should have form {tag:, value:}"""
        for element in tags:
            self.tag_file(element.tag, element.value)

    def multiclear_file(self, file, tags):
        """Remove multiple tags from single file"""
        for tag in tags:
            self.tag_remove(file, tag)

    def tag_files(self, files, tag, value):
        """Tag multiple file with single value"""
        for file in files:
            self.tag_file(file, tag, value)

    def multiclear_files(self, files, tag):
        """Remove single tag from multiple files"""
        for file in files:
            self.clear_file(file, tag)

    def multitag_files(self, files, tags):
        """Tag multiple file with multiple values
        tags elements should have form {tag:, value:}"""
        for file in files:
            self.multitag_file(file, tags)

    def multiclear_tags_files(self, files, tags):
        """Removes multiple tags from multiple files"""
        for file in files:
            self.multiclear_file(file, tags)

    def save_changes(self):
        """Save changes in all the tagged files"""
        for file in self._taggedfiles:
            file.save_changes()
