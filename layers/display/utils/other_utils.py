"""Other utilities."""


import tkinter as tk


def get_str_of_selected(listbox: tk.Listbox):
    """Gets the strings of the selected items of the listbox."""
    return [listbox.get(idx) for idx in listbox.curselection()]
