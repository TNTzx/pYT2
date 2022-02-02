"""Other utilities."""


import tkinter as tk


def get_selected(listbox: tk.Listbox, _list: list):
    """Gets the selected items of the listbox. listbox and list must be synced."""
    str_items = [listbox.get(idx) for idx in listbox.curselection()]
    obj_items = [item for item in _list if item.__repr__() in str_items]
    return obj_items


def update_listbox(listbox: tk.Listbox, _list: list):
    """Update contents of a listbox using a list."""
    listbox.delete(0, tk.END)
    for item in _list:
        listbox.insert(tk.END, item.__repr__())
