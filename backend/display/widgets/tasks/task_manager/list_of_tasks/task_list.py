"""Task manager container."""

import tkinter as tk

import backend.display.utils.defaults as df
import backend.display.utils.widget_inherit as w_i
import backend.display.utils.grid_utils as g_u
import backend.display.utils.font_utils as f_u


class TaskListScroll(tk.Scrollbar, w_i.WidgetInherit):
    """Scrollbar."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        g_u.place_on_grid(self, coords=(1, 0))

class TaskList(tk.Listbox, w_i.WidgetInherit):
    """List of tasks."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        g_u.place_on_grid(self)
        f_u.set_font(self)


class MainFrame(tk.Frame, w_i.WidgetInherit):
    """Main frame for the tasks menu."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **df.FRAME)
        g_u.place_on_grid(self, coords=(0, 1))
        g_u.set_weights(self)
