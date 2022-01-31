"""Main."""

import tkinter as tk

import backend.display.utils.defaults as df
import backend.display.utils.widget_inherit as w_i
import backend.display.utils.grid_utils as g_u
import backend.display.widgets as wg


class FrameMain(tk.Frame, w_i.WidgetInherit):
    """Main frame."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **df.FRAME)
        self.title = wg.title.MainFrame(self)

        g_u.place_on_grid(self)


if __name__ == "__main__":
    main = tk.Tk()
    frame_main = FrameMain(main)
    main.mainloop()
