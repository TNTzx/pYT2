"""UI for editing a specific task."""


import threading as thr
import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmsg
import pytube as yt

import layers.display.utils as ul
import layers.display.widgets.tasks.loading_url as l_u
import layers.library.task as tsk
import layers.library.convert_forms as c_f
import layers.library.yt_other as yt_o


def spawn_window():
    """Spawns the window then returns the Task."""
    window = MainWindow()
    window.wait_window()
    return window.task


class MainWindow(tk.Toplevel, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.g_u.set_weights(self)
        self.geometry("1000x600")
        self.wm_title("Task Manager")
        ul.w_u.center_window(self)

        self.w_frame = self.MainFrame(self)
        self.w_frame.w_url.w_set.configure(command=self.set_url)
        self.w_frame.w_path.w_set.configure(command=self.browse_for_output_path)
        self.w_frame.w_save.w_confirm.configure(command=self.confirm)

        self.task = tsk.Task(yt.YouTube(yt_o.DEFAULT_URL))
        self.streams_info_list: list[yt_o.StreamInfo] = None

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """The main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 1, 1, 1, 1))

            self.w_title = self.Title(self)
            self.w_url = self.URL(self)
            self.w_options = self.Options(self)
            self.w_path = self.Path(self)
            self.w_save = self.SaveControl(self)

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

                        ul.l_u.update_listbox(self, c_f.convert_formats)

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
        w_loading = l_u.Loading()
        def task():
            self.task.yt_obj = yt.YouTube(
                self.w_frame.w_url.w_input.get()
            )

            streams: list[yt.Stream] = self.task.yt_obj.streams.filter(progressive=True)
            self.update_streams_info_list(streams)

            w_loading.destroy()

        thr.Thread(target=task).start()

    def update_streams_info_list(self, streams: list[yt.Stream]):
        """Updates stream_info_dict."""
        self.streams_info_list = [yt_o.StreamInfo(stream) for stream in reversed(streams)]
        ul.l_u.update_listbox(self.w_frame.w_options.w_convert.w_list, self.streams_info_list)


    def get_selected_stream(self) -> yt.Stream:
        """Gets the selected stream_info."""
        return ul.l_u.get_selected(self.w_frame.w_options.w_stream.w_list, self.streams_info_list)

    def get_selected_format(self) -> c_f.ConvertFormat:
        """Gets the selected format."""
        return ul.l_u.get_selected(self.w_frame.w_options.w_convert.w_list, c_f.convert_formats)


    def browse_for_output_path(self):
        """Opens a file dialog to get a path store the output file."""
        title = self.task.yt_obj.title
        default_file_name = f"{title}.{self.get_selected_format().file_ext}"
        file_path = tkfd.asksaveasfilename(
            initialfile = default_file_name,
            filetypes = [("All Files", ".*")] + [
                (convert_format.type, convert_format.file_ext)
                for convert_format in c_f.convert_formats
            ]
        )

        self.w_frame.w_path.w_input.variable.set(file_path)

    def confirm(self):
        """Confirm the inputs."""
        confirm = tkmsg.askokcancel("Confirm", "Confirm these options for the current task?")
        if confirm:
            self.task.selected_stream = self.get_selected_stream()
            self.task.selected_convert_form = self.get_selected_format()
            self.task.output_path = self.w_frame.w_path.w_input.variable.get()

            self.destroy()

    def cancel(self):
        """Cancel the inputs."""
        cancel = tkmsg.askokcancel("Cancel", "Cancel the current task?")
        if cancel:
            self.task = None
            self.destroy()
