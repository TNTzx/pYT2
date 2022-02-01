"""UI for editing a specific task."""


import tkinter as tk
import pytube as yt

import layers.display.utils as ul
import layers.library.yt_other as yt_o


class MainWindow(tk.Toplevel, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.g_u.set_weights(self)

        self.w_frame = self.MainFrame(self)

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """The main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, _y=(1, 1, 1, 1, 1))

            self.w_title = self.Title(self)
            self.w_url = self.URL(self)
            self.w_options = self.Options(self)
            self.w_path = self.Path(self)
            self.w_save = self.SaveControl(self)

            self.yt_obj = yt.YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
            self.streams_list = None

        class Title(tk.Label, ul.w_i.WidgetInherit):
            """The title."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Add / Edit Task")
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self, size_mult=3, bold=True)

        class URL(tk.Frame, ul.w_i.WidgetInherit):
            """Contains widgets for inputting the URL."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 1))
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

        class Options(tk.Frame, ul.w_i.WidgetInherit):
            """Contains options for the selected URL."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 2))
                ul.g_u.set_weights(self, _x=(4, 1))

                self.w_stream = self.StreamSelect(self)
                self.w_convert = self.Convert(self)

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
                    super().__init__(parent, **ul.df.FRAME)
                    ul.g_u.place_on_grid(self, coords=(1, 1))
                    ul.g_u.set_weights(self, _x=(1, 1))

                    self.w_title = self.Title(self)
                    self.w_list = self.List(self)

                class Title(tk.Label, ul.w_i.WidgetInherit):
                    """The title."""
                    def __init__(self, parent: tk.Widget):
                        super().__init__(parent, text="Convert to:")
                        ul.g_u.place_on_grid(self)
                        ul.f_u.set_font(self, bold=True)

                class List(tk.Listbox, ul.w_i.WidgetInherit):
                    """List of formats to convert to."""
                    def __init__(self, parent: tk.Widget):
                        super().__init__(parent)
                        ul.g_u.place_on_grid(self, coords=(1, 0))
                        ul.f_u.set_font(self)

        class Path(tk.Frame, ul.w_i.WidgetInherit):
            """UI to get the file path."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 3))
                ul.g_u.set_weights(self, _x=(1, 3, 1))

                self.w_title = self.Title(self)
                self.w_input = self.Input(self)
                self.w_set = self.Browse(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """The title."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Output to:")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=2, bold=True)

            class Input(tk.Entry, ul.w_i.WidgetInherit):
                """The input field."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent)
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self)

            class Browse(tk.Button, ul.w_i.WidgetInherit):
                """A button that browses the user's directory."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Browse...")
                    ul.g_u.place_on_grid(self, coords=(2, 0))
                    ul.f_u.set_font(self)

        class SaveControl(tk.Frame, ul.w_i.WidgetInherit):
            """Contains buttons for confirming the data inputted."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 4))
                ul.g_u.set_weights(self, _x=(1, 1))

                self.w_confirm = self.Confirm(self)
                self.w_cancel = self.Cancel(self)

            class Confirm(tk.Button, ul.w_i.WidgetInherit):
                """A button that confirms the data inputted."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Confirm")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self)

            class Cancel(tk.Button, ul.w_i.WidgetInherit):
                """A button that cancels the data inputted."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Cancel")
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self)


        def set_url(self):
            """Sets the URL and changes the UI."""
            self.yt_obj = yt.YouTube(
                self.w_url.w_input.get()
            )

            streams: list[yt.Stream] = self.yt_obj.streams.filter(progressive=True)
            self.update_streams_list(streams)

        def update_streams_list(self, streams: list[yt.Stream]):
            self.streams_list = [yt_o.StreamInfo(stream) for stream in streams]
