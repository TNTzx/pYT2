"""Module for class for widget classes to inherit to."""

import tkinter as tk


def func_caller(*funcs):
    """Returns a function that runs multiple functions."""
    def wrap(*args, **kwargs):
        for func in funcs:
            func(*args, **kwargs)

    return wrap


class WidgetInherit(tk.Widget):
    """Class for widget classes to inherit to."""
    def __init_subclass__(cls) -> None:
        def end_init(self: tk.Widget, *args, **kwargs):
            pass

        cls.__init__ = func_caller(cls.__init__, end_init)

    def enable(self, state: bool = True):
        """Enables or disables the widget."""
        if state:
            self.grid()
        else:
            self.grid_forget()
