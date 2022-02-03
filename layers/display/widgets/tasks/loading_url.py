"""Contains widgets for the loading screen during setting the url."""


import tkinter as tk
import tkinter.ttk as ttk

import layers.display.utils as ul


class Loading(tk.Toplevel, ul.w_i.WidgetInherit):
    """Loading screen."""
    def __init__(self, parent: ul.w_i.WidgetInherit):
        super().__init__(parent)
        ul.g_u.set_weights(self)
        self.geometry("300x100")
        ul.w_u.center_window(self)
        self.overrideredirect(True)

        self.w_frame = self.MainFrame(self)

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """Frame."""
        def __init__(self, parent: ul.w_i.WidgetInherit):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 1))

            self.w_title = self.Title(self)
            self.w_loading_bar = self.LoadingBar(self)

        class Title(tk.Label, ul.w_i.WidgetInherit):
            """Title."""
            def __init__(self, parent: ul.w_i.WidgetInherit):
                super().__init__(parent, text="Loading URL...")
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self, size_mult=2, bold=True)

        class LoadingBar(ttk.Progressbar, ul.w_i.WidgetInherit):
            """The loading bar."""
            def __init__(self, parent: ul.w_i.WidgetInherit):
                super().__init__(parent, mode="indeterminate")
                ul.g_u.place_on_grid(self, (0, 1))

                self.start(2)
