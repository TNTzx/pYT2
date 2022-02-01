"""Download widget."""


import tkinter as tk

import backend.display.utils as ul


class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
    """Main frame for the title."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **ul.df.FRAME)
        ul.g_u.place_on_grid(self, coords=(0, 2))
        ul.g_u.set_weights(self, _x=(1, 1))

        self.w_title = self.Title(self)
        self.w_download = self.Download(self)

    class Title(tk.Label, ul.w_i.WidgetInherit):
        """Title label."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, text="Download:")
            ul.g_u.place_on_grid(self)
            ul.f_u.set_font(self, size_mult=2, bold=True)

    class Download(tk.Button, ul.w_i.WidgetInherit):
        """Download button."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent)
            ul.g_u.place_on_grid(self, coords=(1, 0))
            ul.f_u.set_font(self, underline=True)
