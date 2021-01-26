from math import floor


def str_to_int(string, round_down=True):
    """
    parses a string number into an integer, optionally converting to a float
    and rounding down.
    """
    error_msg = "Unable to convert to integer '%s'" % str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        raise RuntimeError(error_msg)

    if round_down:
        integer = floor(integer)
    else:
        integer = round(integer)
    return int(integer)
