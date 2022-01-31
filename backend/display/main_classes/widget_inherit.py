"""Module for class for widget classes to inherit to."""

# pylint: disable=unused-argument

class WidgetInherit():
    """Class for widget classes to inherit to."""
    def __init_subclass__(cls) -> None:
        def end_init(self, *args, **kwargs):
            pass

        def wrap(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            end_init(self, *args, **kwargs)

        cls.__init__ = wrap
