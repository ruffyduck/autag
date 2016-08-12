"""Module that provides customizable tag entries for the GUI"""

from tkinter import *

class TagEntry:
    """Class that can music tags as entries in the GUI"""

    def __init__(self, tag, parent, gridmanager, row, width=20):
        self.tag = tag
        self.width = width
        self.gridmanager = gridmanager
        self.row = row
        self.parent = parent
        self.entries = []
        self.entries.append(Entry(parent, width=self.width))
        self.label = Label(parent, text=tag.name)
        self.currfiles = []


    def draw(self):
        self.gridmanager.add_element(self.label, self.row)

        for entry in self.entries:
            self.gridmanager.add_element(entry, self.row)


    def fill_entries(self, files):
        for entry in self.entries:
            entry.destroy()

        self.entries = []
        for file in files:
            value = file.get_tag_value(self.tag)
            newentry = Entry(self.parent, width=self.width)
        
            if not value is None:
                newentry.insert(0, value)

            self.entries.append(newentry)

        self.currfiles = files
        self.draw()


    def write_files(self):
        for file, entry in zip(self.currfiles, self.entries):
            file.write_tag(self.tag, entry.get())

        