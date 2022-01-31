"""Title widget."""

# pylint: disable=too-many-ancestors


import tkinter as tk

import backend.display.main_classes.widget_inherit as w_i


class Title(tk.Label, w_i.WidgetInherit):
    """Title label."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, text="beans")


class MainFrame(tk.Frame, w_i.WidgetInherit):
    """Main frame for the title."""
    def __init__(self, parent: tk.Widget, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title = Title(parent)
