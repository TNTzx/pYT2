"""Main."""

# pylint: disable=unused-import
# pylint: disable=too-many-ancestors


import tkinter as tk

import backend.display.main_classes.widget_inherit as w_i
import backend.display.widgets as wg


class FrameMain(tk.Frame, w_i.WidgetInherit):
    """Main frame."""
    def __init__(self, parent: tk.Widget, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        wg.title.MainFrame(self)


if __name__ == "__main__":
    main = tk.Tk()
    frame_main = FrameMain(main)
    main.mainloop()
