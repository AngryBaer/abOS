"""
    Color Utilities.
"""

# ----------------------------------------------------------------------------------------------- #
def rgb_to_float(rgb: list | tuple) -> tuple:
    """ Converts an RGB sequence to float. """
    return (
        value_to_float(rgb[0]),
        value_to_float(rgb[1]),
        value_to_float(rgb[2])
    )


def float_to_rgb(rgb: list | tuple) -> tuple:
    """ Converts a float sequence to RGB. """
    return (
        value_to_rgb(rgb[0]),
        value_to_rgb(rgb[1]),
        value_to_rgb(rgb[2])
    )
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def value_to_float(value):
    """ Converts a single RGB value to float. """
    return float(f'{int(value) / 255:.3f}')


def value_to_rgb(value: float):
    """ Converts a single float to rgb. """
    return int(value * 255)
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    assert value_to_float(255) == 1
    assert value_to_rgb(1) == 255
# ----------------------------------------------------------------------------------------------- #
