"""Module that provides the main entry point for the GUI"""

from tkinter import *
import tkinter.filedialog
from view.tagentry import TagEntry
from view.gridmanager import GridManager
from model.basetag import BaseTag, get_tag
from controller.filereader import list_files, get_aufiles, MUSICFLAGS

class AuGUI:
    """Serves as main entry point for the GUI"""

    def __init__(self):
        self.master = Tk()
        self.master.wm_title("AuTag")
        self.master.iconbitmap(default="resources/img.ico")

        self.manager = GridManager()
        self.musicfiles = []
        self.entries = {}
        
        self.__build_entries([["TRACKNUMBER", 2], ["DISCNUMBER", 2], ["TITLE", 30],
                              ["ARTIST", 20], ["ALBUM", 20], ["GENRE", 10], ["DATE", 5],
                              ["ORGANIZATION", 12], ["CONTENTGROUP", 5], ["QUALITY", 8],
                              ["COMMENT", 10]])

        opend = Button(self.master, text="open", width=10, command=self.__open_callback)
        opend.grid(row=0, column=2)
        writed = Button(self.master, text="write", width=10, command=self.__write_callback)
        writed.grid(row=0, column=3)

        for entry in self.entries:
            self.entries[entry].draw()
        

    def __build_entries(self, tagpairs):
        counter = -1
        for pair in tagpairs:
            counter += 1
            name = pair[0]
            width = pair[1]

            self.entries[name] = TagEntry(get_tag(name), self.master, self.manager,
                                          counter, width)


    def __open_callback(self):
        directory = tkinter.filedialog.askdirectory()
        self.musicfiles = get_aufiles(directory)
    
        for entry in self.entries:
            self.entries[entry].fill_entries(self.musicfiles)


    def __write_callback(self):
        for entry in self.entries:
            self.entries[entry].write_files()

        for file in self.musicfiles:
            file.save_changes()
        

    def draw(self):
        """Draw entire GUI"""
        mainloop()

