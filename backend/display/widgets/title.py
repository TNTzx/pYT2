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
        super().__init__(parent, text="YOUTUBE DOWNLOADER")
        g_u.place_on_grid(self)
        f_u.set_font(self, size_mult=3, bold=True)


class MainFrame(tk.Frame, w_i.WidgetInherit):
    """Main frame for the title."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **df.FRAME)
        g_u.place_on_grid(self)
        g_u.set_weights(self)

        self.title = Title(self)
