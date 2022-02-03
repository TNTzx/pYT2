"""Other functions!"""


import unicodedata as ud
import re


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

def get_percent(percent_of_total: int | float, total: int | float, dec_places: int = 2):
    """Returns the %. percent_of_total / total."""
    if percent_of_total > total:
        raise ValueError("percent_of_total cannot be larger than total.")
    return round((percent_of_total / total) * 100, dec_places)

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = ud.normalize('NFKC', value)
    else:
        value = ud.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')
