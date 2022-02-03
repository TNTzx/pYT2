"""Font utilities."""

import tkinter as tk
import tkinter.font as tkf

import layers.display.utils as ul


def set_font(
        widget: ul.w_i.WidgetInherit, family=ul.df.FONT_FAMILY,
        size_mult=1, bold=False, italic=False, underline=False, overline=False
    ):
    """Sets the font of a widget."""
    widget.configure(
        font = tkf.Font(
            family = family,
            size = ul.df.FONT_SIZE_BASE * size_mult,
            weight = "bold" if bold else "normal",
            slant = "italic" if italic else "roman",
            underline = underline,
            overstrike = overline
        )
    )
