"""Module for management of all GUI elements"""

from tkinter import *


class GridManager:
    """Class that controls all GUI elements in a basic grid layout"""

    def __init__(self):
        self.columns = {}


    def add_element(self, element, ccolumn):
        """Adds new element to given line"""
        
        if not ccolumn in self.columns.keys():
            self.columns[ccolumn] = 1
            
        element.grid(row=self.columns[ccolumn], column=ccolumn)
        self.columns[ccolumn] += 1
        
    
        
