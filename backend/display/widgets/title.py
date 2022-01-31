"""Title widget."""

# pylint: disable=too-many-ancestors


import tkinter as tk

import backend.display.utils.defaults as df
import backend.display.utils.widget_inherit as w_i
import backend.display.utils.grid_utils as g_u
import backend.display.utils.font_utils as f_u


class Title(tk.Label, w_i.WidgetInherit):
    """Title label."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, text="beans")
        g_u.place_on_grid(self)



class MainFrame(tk.Frame, w_i.WidgetInherit):
    """Main frame for the title."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **df.FRAME)
        self.title = Title(self)
        g_u.place_on_grid(self)
