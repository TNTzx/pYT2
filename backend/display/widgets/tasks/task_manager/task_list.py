"""Task manager."""

import tkinter as tk

import backend.display.utils as ul


class MainFrame(tk.Frame, ul.w_i.WidgetInherit):
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
            ul.g_u.set_weights(self, (1, 1))

            self.w_hor_scrollbar = self.XScroll(self)
            self.w_vert_scrollbar = self.YScroll(self)
            self.w_list = self.List(self)

            self.w_hor_scrollbar.configure(command=self.w_list.xview)
            self.w_vert_scrollbar.configure(command=self.w_list.yview)
            self.w_list.configure(
                xscrollcommand=self.w_hor_scrollbar,
                yscrollcommand=self.w_vert_scrollbar.set
            )


        class List(tk.Listbox, ul.w_i.WidgetInherit):
            """List of tasks."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent)
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self)

                for i in range(100):
                    self.insert(tk.END, list(range(i, 100)))

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

            self.w_add = self.AddTask(self)
            self.w_edit = self.EditTask(self)
            self.w_remove = self.RemoveTask(self)

        class AddTask(tk.Button, ul.w_i.WidgetInherit):
            """Add a task."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Add Task", command=self.click)
                ul.g_u.place_on_grid(self)
                ul.f_u.set_font(self, underline=True)

            def click(self):
                """Click!"""


        class EditTask(tk.Button, ul.w_i.WidgetInherit):
            """Edit a task."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Edit Task", command=self.click)
                ul.g_u.place_on_grid(self, coords=(0, 1))
                ul.f_u.set_font(self)

            def click(self):
                """Click!"""


        class RemoveTask(tk.Button, ul.w_i.WidgetInherit):
            """Remove a task."""
            def __init__(self, parent: tk.Widget):
                super().__init__(parent, text="Remove Task", command=self.click)
                ul.g_u.place_on_grid(self, coords=(0, 2))
                ul.f_u.set_font(self)

            def click(self):
                """Click!"""
