"""Module for class for widget classes to inherit to."""

import tkinter as tk


def func_caller(*funcs):
    """Returns a function that runs multiple functions."""
    def wrap(*args, **kwargs):
        for func in funcs:
            func(*args, **kwargs)

    return wrap


class WidgetInherit(ul.w_i.WidgetInherit):
    """Class for widget classes to inherit to."""
    def __init_subclass__(cls) -> None:
        def end_init(self: ul.w_i.WidgetInherit, *args, **kwargs):
            pass

        cls.__init__ = func_caller(cls.__init__, end_init)

    def visible(self, state: bool = True):
        """Makes a widget visible or not."""
        if state:
            self.grid()
        else:
            self.grid_remove()

    def enable(self, state: bool = True):
        """Enables or disables the widget and its children."""
        configure = {
            "state": tk.NORMAL if state else tk.DISABLED
        }

        def edit_state(widget: ul.w_i.WidgetInherit):
            children = widget.winfo_children()
            if len(children) > 0:
                for child in children:
                    edit_state(child)
            else:
                if issubclass(widget.__class__, tk.Scrollbar):
                    pass
                else:
                    widget.configure(**configure)

        edit_state(self)
