"""Download widgets."""


import threading as thr
import tkinter as tk
import tkinter.ttk as ttk
import pytube as yt

import layers.display.utils as ul

import layers.library.task as tsk
import layers.library.other_functions as o_f


class MainWindow(tk.Toplevel, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.w_u.set_size(self, ul.w_u.Dimension(600, 300))
        ul.w_u.center_window(self)
        ul.g_u.set_weights(self)

        self.w_frame = self.MainFrame(self)

    class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
        """Main frame."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 1))

            self.w_title = self.Title(self)
            self.w_progressbars = self.Progressbars(self)

        class Title(tk.Label, ul.w_i.WidgetInherit):
            """Title."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Downloading...")
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self, size_mult=2, bold=True)

        class Progressbars(tk.Frame, ul.w_i.WidgetInherit):
            """Progressbars."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 1))
                ul.g_u.set_weights(self, y=(1, 1))

                self.w_total_tasks = self.TotalTasksProgress(self)
                self.w_task = self.TaskProgress(self)

            class TotalTasksProgress(tk.Frame, ul.w_i.WidgetInherit):
                """Contains widgets for the total tasks finished."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, **ul.df.FRAME)
                    ul.g_u.place_on_grid(self)
                    ul.g_u.set_weights(self, y=(1, 1))

                    self.w_label = self.Label(self)
                    self.w_progress = self.Progressbar(self)

                class Label(tk.Label, ul.w_i.WidgetInherit):
                    """Label text."""
                    def __init__(self, parent: tk.Widget):
                        self.variable = tk.StringVar()
                        super().__init__(parent, textvariable=self.variable)
                        ul.g_u.place_on_grid(self)
                        ul.f_u.set_font(self)

                class Progressbar(ttk.Progressbar, ul.w_i.WidgetInherit):
                    """The progressbar."""
                    def __init__(self, parent: tk.Widget):
                        self.variable = tk.DoubleVar()
                        super().__init__(parent, maximum=100, variable=self.variable)
                        ul.g_u.place_on_grid(self, coords=(0, 1))

            class TaskProgress(tk.Frame, ul.w_i.WidgetInherit):
                """Total progress for one task."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, **ul.df.FRAME)
                    ul.g_u.place_on_grid(self, coords=(0, 1))
                    ul.g_u.set_weights(self, y=(1, 1))

                    self.w_label = self.Label(self)
                    self.w_progress = self.Progressbar(self)

                class Label(tk.Label, ul.w_i.WidgetInherit):
                    """Label text."""
                    def __init__(self, parent: tk.Widget):
                        self.variable = tk.StringVar()
                        super().__init__(parent, textvariable=self.variable)
                        ul.g_u.place_on_grid(self)
                        ul.f_u.set_font(self)

                class Progressbar(ttk.Progressbar, ul.w_i.WidgetInherit):
                    """The progressbar."""
                    def __init__(self, parent: tk.Widget):
                        self.variable = tk.DoubleVar()
                        super().__init__(parent, maximum=100, variable=self.variable)
                        ul.g_u.place_on_grid(self, coords=(0, 1))


def download(tasks: list[tsk.Task]):
    """Downloads a list of tasks."""
    window = MainWindow()
    w_progressbars = window.w_frame.w_progressbars
    total_tasks = len(tasks)


    def update_tasks_progress(task: tsk.Task, task_idx: int, total_tasks: int):
        task_no = task_idx + 1
        w_progressbars.w_total_tasks.w_label.variable.set((
            f"Tasks Download Progress: \n"
            f"Downloading task {task_no} of {total_tasks}\n"
            f"( {round((task_no - 1 / total_tasks) * 100, 2)}% )\n"
            f"{task.__repr__()}"
        ))

    def update_task_progress(stream: yt.Stream, chunk: bytes, bytes_remaining: int):
        total_bytes = stream.filesize
        bytes_downloaded = total_bytes - bytes_remaining
        bytes_downloaded_display = f"{o_f.bytes_to_mb(bytes_downloaded)} / {o_f.bytes_to_mb(total_bytes)}"
        percent = round((bytes_downloaded / total_bytes) * 100, 2)

        w_task = window.w_frame.w_progressbars.w_task
        w_task.w_label.variable.set((
            "Task Download Progress:\n"
            f"{bytes_downloaded_display} ( {percent} )"
        ))
        w_task.w_progress.variable.set(percent)


    for idx, task in enumerate(tasks):
        update_tasks_progress(task, idx, total_tasks)
        task.callbacks.youtube.on_progress = update_task_progress

        def download_task(task: tsk.Task = task):
            task.download()

        thr.Thread(target=download_task).start()
