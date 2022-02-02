"""Custom messagebox."""


import typing as typ
import tkinter as tk

import layers.display.utils as ul


class Messagebox(tk.Toplevel, ul.w_i.WidgetInherit):
    """Represents a message box."""
    def __init__(self, parent: tk.Widget, title: str, description: str):
        super().__init__(parent)
        self.title(title)
        ul.g_u.set_weights(self, y=(1, 1))
        ul.w_u.set_size(self, ul.w_u.Dimension(len(description) * ul.df.FONT_SIZE_BASE, ul.df.FONT_SIZE_BASE * 5 * 2))
        ul.w_u.center_window(self)

        self.w_description = self.Description(self, description)
        self.w_button_frame = self.ButtonFrame(self)

        self.buttons = []
        self.value: str = None

    class Description(tk.Label, ul.w_i.WidgetInherit):
        """The description."""
        def __init__(self, parent: tk.Widget, description: str):
            super().__init__(parent, text=description)
            ul.g_u.place_on_grid(self)
            ul.f_u.set_font(self, bold=True)

    class ButtonFrame(tk.Frame, ul.w_i.WidgetInherit):
        """Frame for buttons."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent,**ul.df.FRAME)
            ul.g_u.place_on_grid(self, coords=(0, 1))


    class Button(tk.Button, ul.w_i.WidgetInherit):
        """Button."""
        def __init__(self, parent: tk.Widget, text: str, command: typ.Callable = None):
            super().__init__(parent, text=text, command=command)
            ul.f_u.set_font(self)
            self.text = text

    def set_value(self, value: str):
        """Set the value of self.value."""
        self.value = value
        self.destroy()

    def add_button(self, text: str):
        """Adds a button to the message box."""
        button = self.Button(self.w_button_frame, text, command=lambda: self.set_value(text))
        self.buttons.append(button)


    def show(self):
        """Shows the message box and waits for input. Returns the selected option."""
        for idx, button in enumerate(self.buttons):
            ul.g_u.place_on_grid(button, coords=(idx, 0))

        ul.g_u.set_weights(self.w_button_frame, x=[1 for _ in self.buttons])

        self.wait_window()

        return self.value


class Options():
    """Contains the options available."""
    ok = "OK"
    exit = "Exit"

    yes = "Yes"
    no = "No"

    submit = "Submit"
    cancel = "Cancel"


def messagebox(parent: tk.Widget, title: str, description: str, options: tuple[str] = ()):
    """Shows a messagebox then returns the option."""
    msgbox = Messagebox(parent, title, description)
    for option in options:
        msgbox.add_button(option)

    return msgbox.show()
