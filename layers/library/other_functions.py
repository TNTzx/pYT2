"""Other functions!"""

class Unique:
    """Unique object."""

def bytes_to_mb(_bytes: int):
    """Returns MB of bytes."""
    return round(_bytes / 1048576, 2)

def replace_item_in_list(_list: list, to_replace: object, will_replace: object):
    """Replaces an item in a list given original item."""
    _list[_list.index(to_replace)] = will_replace

def subtract_lists(minuend: list, subtrahend: list):
    """Subtracts two lists together."""
    return [item for item in minuend if item not in subtrahend]
