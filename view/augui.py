"""Module that provides the main entry point for the GUI"""

from tkinter import *
import tkinter.filedialog
from view.tagentry import TagEntry, SingleTagEntry
from view.gridmanager import GridManager
from model.basetag import BaseTag, get_tag
from controller.filereader import list_files, get_aufiles, MUSICFLAGS


class AuGUI:
    """Serves as main entry point for the GUI. Autotaggers can be comitted that 
    control automatic tagging on tags(will be called on open) and on files(will be called 
    on write)"""

    def __init__(self, tagactions, fileactions):
        self.tagactions = tagactions
        self.fileactions = fileactions
        self.master = Tk()
        self.master.wm_title("AuTag")
        self.master.iconbitmap(default="resources/img.ico")

        self.manager = GridManager()
        self.musicfiles = []
        self.entries = []
        self.curr_directories = []

        self.__build_entries([["TRACKNUMBER", 2], ["DISCNUMBER", 2], ["TITLE", 30],
                              ["artist", 20], ["ALBUM", 20], ["GENRE", 10], ["DATE", 5],
                              ["ORGANIZATION", 15], ["CONTENTGROUP", 5], ["QUALITY", 10],
                              ["COMMENT", 10], ["RATING", 3]])

        self.__build_single_entries([["TRACKTOTAL", 0, 2], ["DISCTOTAL", 1, 2],
                                     ["ALBUMARTIST", 3, 20], ["ALBUM", 4, 20],
                                     ["GENRE", 5, 10], ["DATE", 6, 5],
                                     ["ORGANIZATION", 7, 15],
                                     ["CONTENTGROUP", 8, 5],
                                     ["QUALITY", 9, 10], ["COMMENT", 10, 10],
                                     ["ALBUM RATING", 11, 3]])

        opend = Button(self.master, text="open", width=10,
                       command=self.__open_callback)
        opend.grid(row=0, column=3)

        nextd = Button(self.master, text="next", width=10,
                       command=self.__next_callback)
        nextd.grid(row=0, column=4)

        writed = Button(self.master, text="write", width=10,
                        command=self.__write_callback)
        writed.grid(row=0, column=5)

        for entry in self.entries:
            entry.draw()

    def __build_entries(self, tagpairs):
        counter = -1
        for pair in tagpairs:
            counter += 1
            name = pair[0]
            width = pair[1]

            self.entries.append(TagEntry(get_tag(name),
                                         self.master, self.manager,
                                         counter, width))

    def __build_single_entries(self, entryinfos):

        for info in entryinfos:
            name = info[0]
            row = info[1]
            width = info[2]

            self.entries.append(SingleTagEntry(get_tag(name),
                                               self.master,
                                               self.manager, row, width))

    def __tag_new_entries(self):
        self.manager.reset()
        curr_dir = tkinter.filedialog.askdirectory()
        self.curr_directories.append(curr_dir)
        self.musicfiles = get_aufiles(curr_dir)

        if self.tagactions is not None:
            self.tagactions.auto_tag_directory(curr_dir)

            for entry in self.entries:
                entry.fill_entries(self.musicfiles)

    def __open_callback(self):
        self.curr_directories = []
        self.__tag_new_entries()

    def __next_callback(self):
        for entry in self.entries:
            entry.write_files()

        for file in self.musicfiles:
            file.save_changes()

        self.__tag_new_entries()

    def __write_callback(self):
        self.manager.reset()

        for entry in self.entries:
            entry.write_files()

        for file in self.musicfiles:
            file.save_changes()

        if self.fileactions is not None and len(self.curr_directories) > 0:
            for directory in self.curr_directories:
                self.fileactions.auto_tag_directory(directory)

        self.curr_directories = []

    def draw(self):
        """Draw entire GUI"""
        mainloop()
