"""Grid utilities."""

import tkinter as tk

import backend.display.utils.defaults as df


def place_on_grid(widget: tk.Widget,
        coords = (0, 0),
        span_set = (1, 1),
        ipad_set = (0, 0),
        pad_set = df.PAD_SET,
        sticks = ("N", "S", "E", "W")
    ):
    """Places a widget on a grid."""
    widget.grid(
        row = coords[0],
        column = coords[1],
        rowspan = span_set[0],
        columnspan = span_set[1],
        ipadx = ipad_set[0],
        ipady = ipad_set[1],
        padx = pad_set[0],
        pady = pad_set[1],
        sticky = "".join(sticks)
    )

def set_weights(widget: tk.Widget, _x=(1,), _y=(1,)):
    """Sets the weights for a widget, usually a Frame or a LabelFrame goes here."""
    for idx, weight in enumerate(_x):
        widget.rowconfigure(idx, weight=weight)
    for idx, weight in enumerate(_y):
        widget.columnconfigure(idx, weight=weight)
