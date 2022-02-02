"""Main window."""


import tkinter as tk

import layers.display.utils as ul
import layers.display.widgets.tasks.tasks as tsks


class MainWindow(tk.Tk):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.g_u.set_weights(self)
        ul.w_u.set_size(self, ul.w_u.Dimension(1000, 600))
        ul.w_u.center_window(self)

        self.mainloop()

        self.w_frame = self.FrameMain(self)


    class FrameMain(tk.Frame, ul.w_i.WidgetInherit):
        """Main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 3, 1))

            self.w_title = self.TitleFrame(self)
            self.w_tasks = tsks.MainFrame(self)
            self.w_download = self.DownloadFrame(self)

        class TitleFrame(tk.Frame, ul.w_i.WidgetInherit):
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

        class DownloadFrame(tk.Frame, ul.w_i.WidgetInherit):
            """Main frame for the title."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 2))
                ul.g_u.set_weights(self, x=(1, 4))

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
                    super().__init__(parent, text="Download!")
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self, underline=True)
