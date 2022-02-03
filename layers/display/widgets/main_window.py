"""Main window."""


import threading as thr
import tkinter as tk

import layers.display.utils as ul
import layers.display.utils.widgets.messagebox as msgbox

import layers.library.task as tsk

import layers.display.widgets.tasks.tasks as tsks
import layers.display.widgets.tasks.edit as tske
import layers.display.widgets.download.download as dl

import layers.library.other_functions as o_f


class MainWindow(tk.Tk, ul.w_i.WidgetInherit):
    """The main window."""
    def __init__(self):
        super().__init__()
        ul.g_u.set_weights(self)
        ul.w_u.set_size(self, ul.w_u.Dimension(1000, 600))
        ul.w_u.center_window(self)

        self.w_frame = self.FrameMain(self)

        self.w_frame.w_tasks.w_control.w_controls.w_add.configure(command=self.add_task)
        self.w_frame.w_tasks.w_control.w_controls.w_edit.configure(command=self.edit_task)
        self.w_frame.w_tasks.w_control.w_controls.w_remove.configure(command=self.remove_task)
        self.w_frame.w_download.w_button.configure(command=self.download)

        self.tasks: list[tsk.Task] = []
        self.tasks.append(tsk.DEFAULT_TASK)
        self.update_listbox()


        self.mainloop()


    class FrameMain(tk.Frame, ul.w_i.WidgetInherit):
        """Main frame."""
        def __init__(self, parent: ul.w_i.WidgetInherit):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self)
            ul.g_u.set_weights(self, y=(1, 3, 1))

            self.w_title = self.TitleFrame(self)
            self.w_tasks = tsks.MainFrame(self)
            self.w_download = self.DownloadFrame(self)

        class TitleFrame(tk.Frame, ul.w_i.WidgetInherit):
            """Main frame for the title."""
            def __init__(self, parent: ul.w_i.WidgetInherit):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self)
                ul.g_u.set_weights(self)

                self.w_title = self.Title(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """Title label."""
                def __init__(self, parent: ul.w_i.WidgetInherit):
                    super().__init__(parent, text="YOUTUBE DOWNLOADER")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=3, bold=True)

        class DownloadFrame(tk.Frame, ul.w_i.WidgetInherit):
            """Main frame for the title."""
            def __init__(self, parent: ul.w_i.WidgetInherit):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(0, 2))
                ul.g_u.set_weights(self, x=(1, 4))

                self.w_title = self.Title(self)
                self.w_button = self.Download(self)

            class Title(tk.Label, ul.w_i.WidgetInherit):
                """Title label."""
                def __init__(self, parent: ul.w_i.WidgetInherit):
                    super().__init__(parent, text="Download:")
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self, size_mult=2, bold=True)

            class Download(tk.Button, ul.w_i.WidgetInherit):
                """Download button."""
                def __init__(self, parent: ul.w_i.WidgetInherit):
                    super().__init__(parent, text="Download!")
                    ul.g_u.place_on_grid(self, coords=(1, 0))
                    ul.f_u.set_font(self, underline=True)


    def update_listbox(self):
        """Updates the list of tasks using self.tasks."""
        ul.l_u.update_listbox(self.w_frame.w_tasks.w_control.w_list.w_list, self.tasks)


    def add_task(self):
        """Add a task."""
        task = tske.spawn_window(self)
        if task is None:
            return

        self.tasks.append(task)
        self.update_listbox()

    def edit_task(self):
        """Edit the selected task."""
        task = ul.l_u.get_selected(self.w_frame.w_tasks.w_control.w_list.w_list, self.tasks)[0]
        new_task = tske.spawn_window(self, task)

        if new_task is not None:
            o_f.replace_item_in_list(self.tasks, task, new_task)
        self.update_listbox()

    def remove_task(self):
        """Removes the selected tasks."""
        remove = msgbox.messagebox(
            self, "Remove Confirmation", "Are you sure you want to remove the following tasks? This cannot be undone!",
            (msgbox.Options.yes, msgbox.Options.no)
        )
        if remove == msgbox.Options.yes:
            to_be_deleted_tasks = ul.l_u.get_selected(self.w_frame.w_tasks.w_control.w_list.w_list, self.tasks)
            self.tasks = o_f.subtract_lists(self.tasks, to_be_deleted_tasks)
        self.update_listbox()

    def download(self):
        """Downloads the current tasks."""
        will_download = msgbox.messagebox(
            self, "Download confirmation",
            f"Are you sure you want to download {len(self.tasks)} {'task' if len(self.tasks) == 1 else 'tasks'}?",
            (msgbox.Options.yes, msgbox.Options.no)
        )

        if will_download == msgbox.Options.yes:
            def download_thread():
                dl.download(self, self.tasks)

            thr.Thread(target=download_thread).start()
