"""UI for editing a specific task."""


import tkinter as tk
import tkinter.filedialog as tkfd
import pytube as yt

import layers.display.utils as ul
import layers.library.task as tsk
import layers.library.convert_forms as c_f
import layers.library.yt_other as yt_o


class MainWindow(tk.Toplevel, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.g_u.set_weights(self)
        self.geometry("1000x600")
        self.wm_title("Task Manager")

        self.w_frame = self.MainFrame(self)

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """The main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 1, 1, 1, 1))

            self.w_title = self.Title(self)

            self.w_url = self.URL(self)
            self.w_url.w_set.configure(command=self.set_url)

            self.w_options = self.Options(self)

            self.w_path = self.Path(self)
            self.w_path.w_set.configure(command=self.browse_for_output_path)

            self.w_save = self.SaveControl(self)


            self.task = tsk.Task(yt.YouTube(yt_o.DEFAULT_URL))
            self.streams_info_dict: dict[str, yt_o.StreamInfo] = None

        class Title(tk.Label, ul.w_i.WidgetInherit):
            """The title."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Task Manager")
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self, size_mult=3, bold=True)

        class URL(tk.Frame, ul.w_i.WidgetInherit):
            """Contains widgets for inputting the URL."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 1))
                ul.g_u.set_weights(self, x=(1, 3, 1))

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
                    ul.g_u.place_on_grid(self, coords=(1, 0), ipad_set=(5, 0))
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
                ul.g_u.set_weights(self, x=(4, 1))

                self.w_stream = self.StreamSelect(self)
                self.w_convert = self.Convert(self)

            class StreamSelect(tk.Frame, ul.w_i.WidgetInherit):
                """UI for selecting the stream."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, **ul.df.FRAME)
                    ul.g_u.place_on_grid(self, coords=(0, 1))
                    ul.g_u.set_weights(self, y=(1, 3))

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
                        super().__init__(parent, exportselection=False)
                        ul.g_u.place_on_grid(self, coords=(0, 1))
                        ul.f_u.set_font(self)

            class Convert(tk.Frame, ul.w_i.WidgetInherit):
                """UI for converting the stream into a format."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, **ul.df.FRAME)
                    ul.g_u.place_on_grid(self, coords=(1, 1))
                    ul.g_u.set_weights(self, x=(1, 1))

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
                        super().__init__(parent, exportselection=False)
                        ul.g_u.place_on_grid(self, coords=(1, 0))
                        ul.f_u.set_font(self)

                        for convert_format in c_f.convert_formats:
                            self.insert(tk.END, c_f.convert_format_to_str(convert_format))

        class Path(tk.Frame, ul.w_i.WidgetInherit):
            """UI to get the file path."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 3), ipad_set=(5, 0))
                ul.g_u.set_weights(self, x=(1, 3, 1))

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
                    self.variable = tk.StringVar()
                    super().__init__(parent, textvariable=self.variable)
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
                ul.g_u.set_weights(self, x=(1, 1))

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
            self.task.yt_obj = yt.YouTube(
                self.w_url.w_input.get()
            )

            streams: list[yt.Stream] = self.task.yt_obj.streams.filter(progressive=True)
            self.update_streams_info_dict(streams)

        def update_streams_info_dict(self, streams: list[yt.Stream]):
            """Updates stream_info_dict."""
            self.streams_info_dict = {
                yt_o.stream_to_str(stream): yt_o.StreamInfo(stream)
                for stream in reversed(streams)
            }
            for stream_info in self.streams_info_dict:
                self.w_options.w_stream.w_list.insert(tk.END, stream_info)


        def get_selected_stream(self):
            """Gets the selected stream_info."""
            return self.streams_info_dict[
                ul.o_u.get_str_of_selected(self.w_options.w_stream.w_list)[0]
            ]
        
        def get_selected_format(self):
            """Gets the selected format."""
            return 


        def browse_for_output_path(self):
            """Opens a file dialog to get a path store the output file."""
            title = self.task.yt_obj.title
            default_file_name = f"{title}.{self.get_selected_stream().stream.subtype}"
            file_path = tkfd.asksaveasfilename(
                initialfile = default_file_name,
                filetypes = [
                    (convert_format.type, convert_format.file_ext)
                    for convert_format in c_f.convert_formats
                ] + [("All Files", ".*")]
            )

            self.w_path.w_input.variable.set(file_path)
