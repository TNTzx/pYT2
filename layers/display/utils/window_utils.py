"""Module for window utilities."""

import tkinter as tk


class Dimension():
    """Stores a set of x and y values."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_x_code(self):
        """Gets the x * y code."""
        return f"{self.x}x{self.y}"


def set_size(window: tk.Tk | tk.Toplevel, size: Dimension):
    """Set size of the window."""
    window.geometry(size.get_x_code())

def center_window(window: tk.Tk | tk.Toplevel):
    """Center the window to the screen."""
    window.update_idletasks()

    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width

    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = window.winfo_screenwidth() / 2 - win_width / 2
    y = window.winfo_screenheight() / 2 - win_height / 2
    window.geometry(f"{width}x{height}+{x}+{y}")
