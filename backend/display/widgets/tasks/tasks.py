"""Tasks widgets."""

import tkinter as tk

import backend.display.utils as ul
import backend.display.widgets.tasks.task_manager.task_list as t_l


class Title(tk.Label, ul.w_i.WidgetInherit):
    """Title."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, text="TASKS")
        ul.g_u.place_on_grid(self)
        ul.f_u.set_font(self, size_mult=2, bold=True)


class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
    """Main frame for the tasks menu."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **ul.df.FRAME)
        ul.g_u.place_on_grid(self, coords=(0, 1))
        ul.g_u.set_weights(self)

        self.w_title = Title(self)
        self.w_manager = t_l.MainFrame(self)
