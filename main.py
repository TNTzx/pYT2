"""Main."""

import tkinter as tk

import backend.display.utils as ul
import backend.display.widgets as wg


class FrameMain(tk.Frame, ul.w_i.WidgetInherit):
    """Main frame."""
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, **ul.df.FRAME)
        ul.g_u.place_on_grid(self)
        ul.g_u.set_weights(self)

        self.w_title = wg.title.MainFrame(self)
        self.w_tasks = wg.tasks.tasks.MainFrame(self)



if __name__ == "__main__":
    main = tk.Tk()
    ul.g_u.set_weights(main)
    frame_main = FrameMain(main)
    main.mainloop()
