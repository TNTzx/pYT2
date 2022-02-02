"""Tasks widgets."""

import tkinter as tk

import layers.display.utils as ul
import layers.display.widgets.tasks.edit as ed

class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
    """Main frame for the tasks menu."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **ul.df.FRAME)
        ul.g_u.place_on_grid(self, coords=(0, 1))
        ul.g_u.set_weights(self)

        self.w_title = self.Title(self)
        self.w_control = self.TaskControl(self)


    class Title(tk.Label, ul.w_i.WidgetInherit):
        """Title."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, text="TASKS")
            ul.g_u.place_on_grid(self)
            ul.f_u.set_font(self, size_mult=2, bold=True)

    class TaskControl(tk.Frame, ul.w_i.WidgetInherit):
        """Main frame for the tasks menu."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, **ul.df.FRAME)
            ul.g_u.place_on_grid(self, coords=(0, 1))
            ul.g_u.set_weights(self)

            self.w_list = self.List(self)
            self.w_controls = self.Controls(self)


        class List(tk.Frame):
            """Task list and scrollbar."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self)
                ul.g_u.set_weights(self)

                self.w_hor_scrollbar = self.XScroll(self)
                self.w_vert_scrollbar = self.YScroll(self)
                self.w_list = self.List(self)

                self.w_hor_scrollbar.configure(command=self.w_list.xview)
                self.w_vert_scrollbar.configure(command=self.w_list.yview)
                self.w_list.configure(
                    xscrollcommand=self.w_hor_scrollbar.set,
                    yscrollcommand=self.w_vert_scrollbar.set
                )


            class List(tk.Listbox, ul.w_i.WidgetInherit):
                """List of tasks."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, exportselection=False)
                    ul.g_u.place_on_grid(self)
                    ul.f_u.set_font(self)

            class XScroll(tk.Scrollbar, ul.w_i.WidgetInherit):
                """Horizontal Scrollbar."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, orient=tk.HORIZONTAL)
                    ul.g_u.place_on_grid(self, coords=(0, 1))

            class YScroll(tk.Scrollbar, ul.w_i.WidgetInherit):
                """Vertical Scrollbar."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent)
                    ul.g_u.place_on_grid(self, coords=(1, 0))


        class Controls(tk.Frame, ul.w_i.WidgetInherit):
            """Controls for the lists."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, **ul.df.FRAME)
                ul.g_u.place_on_grid(self, coords=(1, 0))
                ul.g_u.set_weights(self, y=(1, 1, 1))

                self.w_add = self.AddTask(self)
                self.w_edit = self.EditTask(self)
                self.w_remove = self.RemoveTask(self)

            class TaskButton(tk.Button, ul.w_i.WidgetInherit):
                """Base button class."""
                def __init__(self, parent: tk.Widget, text: str, underline=False, coords=(0, 0)):
                    super().__init__(parent, text=text)
                    ul.g_u.place_on_grid(self, coords=coords)
                    ul.f_u.set_font(self, underline=underline)

            class AddTask(TaskButton):
                """Add a task."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Add Task", underline=True)


            class EditTask(TaskButton):
                """Add a task."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Edit Task", coords=(0, 1))


            class RemoveTask(TaskButton):
                """Add a task."""
                def __init__(self, parent: tk.Widget):
                    super().__init__(parent, text="Remove Task", coords=(0, 2))
    

    def add_task(self):
        """Adds a task."""
