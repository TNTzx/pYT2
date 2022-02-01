"""UI for editing a specific task."""

import tkinter as tk

import backend.display.utils as ul


class MainWindow(tk.Toplevel, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()

        self.w_frame = self.MainFrame(self)

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """The main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, _y=(1, 1, 1))

            self.w_url = self.URL(self)
            self.w_stream = self.StreamSelect(self)
            self.w_convert = self.Convert(self)

        class URL(tk.Frame, ul.w_i.WidgetInherit):
            """Contains widgets for inputting the URL."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, span_set=(2, 1))
                ul.g_u.set_weights(self, _x=(1, 3, 1))

                self.w_title = self.Title(self)
                self.w_input = self.Input(self)
                self.w_set = self.Set(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """The title."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Set URL")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=2, bold=True)

            class Input(tk.Entry, ul.w_i.WidgetInherit):
                """The input field."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent)
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self)

            class Set(tk.Button, ul.w_i.WidgetInherit):
                """A button that sets the current URL from the entry box."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Set URL")
                    ul.g_u.place_on_grid(self, coords=(2, 0))
                    ul.f_u.set_font(self)

        class StreamSelect(tk.Frame, ul.w_i.WidgetInherit):
            """UI for selecting the stream."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 1))
                ul.g_u.set_weights(self, _y=(1, 3))

                self.w_title = self.Title(self)
                self.w_list = self.Listbox(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """The title."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Select Stream")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=2, bold=True)

            class Listbox(tk.Listbox, ul.w_i.WidgetInherit):
                """The list of streams."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent)
                    ul.g_u.place_on_grid(self, coords=(0, 1))
                    ul.f_u.set_font(self)

        class Convert(tk.Frame, ul.w_i.WidgetInherit):
            """UI for converting the stream into a format."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent)
                ul.g_u.place_on_grid(self, coords=(1, 1))
                ul.g_u.set_weights(self, _x=(1, 3))

                self.w_title = self.Title(self)
                self.w_list = self.List(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """The title."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Convert to:")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=2, bold=True)

            class List(tk.Listbox, ul.w_i.WidgetInherit):
                """List of formats to convert to."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent)
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self)
