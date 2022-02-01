"""Title widget."""


import tkinter as tk

import layers.display.utils as ul


class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
    """Main frame for the title."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **ul.df.FRAME)
        ul.g_u.place_on_grid(self)
        ul.g_u.set_weights(self)

        self.w_title = self.Title(self)

    class Title(tk.Label, ul.w_i.WidgetInherit):
        """Title label."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, text="YOUTUBE DOWNLOADER")
            ul.g_u.place_on_grid(self)
            ul.f_u.set_font(self, size_mult=3, bold=True)
