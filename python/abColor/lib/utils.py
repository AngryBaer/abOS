"""
    Color Utilities
"""

# ----------------------------------------------------------------------------------------------- #
def rgb_to_float(rgb):
    """
    Converts an RGB sequence to float.

    :param rgb:      rgb sequence to convert
                      - list [int, int, int]
                      - tuple (int, int, int)

    :return values:  converted sequence
                      - tuple (float, float, float)
    """
    assert isinstance(rgb, (list, tuple)), 'takes tuple or list, given: {}'.format(type(rgb))
    assert len(rgb) == 3, 'takes sequence of 3, given: {}'.format(len(rgb))
    values = (
        value_to_float(rgb[0]),
        value_to_float(rgb[1]),
        value_to_float(rgb[2])
    )
    return values


def float_to_rgb(rgb):
    """
    Converts an float sequence to RGB.

    :param rgb:      float sequence to convert
                      - list [float, float, float]
                      - tuple (float, float, float)

    :return values:  converted sequence
                      - tuple (int, int, int)
    """
    assert isinstance(rgb, (list, tuple)), 'takes tuple or list, given: {}'.format(type(rgb))
    assert len(rgb) == 3, 'takes sequence of 3, given: {}'.format(len(rgb))
    values = (
        value_to_rgb(rgb[0]),
        value_to_rgb(rgb[1]),
        value_to_rgb(rgb[2])
    )
    return values
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def value_to_float(value):
    """
    Converts a single RGB value to float

    :param value:  rgb value to convert
                    - int

    :return value: rgb value as float
                    - float
    """
    assert isinstance(value, int), 'takes int, given: {}'.format(type(value))
    assert 0 <= value <=255, 'takes value between 0 and 255, given: {}'.format(value)
    return float('{:.3f}'.format(int(value)/255))


def value_to_rgb(value):
    """
    Converts a single float to rgb

    :param value:  float to convert
                    - float

    :return value: float as rgb value
                    - int
    """
    assert isinstance(value, float), 'takes float, given: {}'.format(type(value))
    assert 0 <= value <=1, 'takes value between 0.0 and 1.0, given: {}'.format(value)
    return int(value*255)
# ----------------------------------------------------------------------------------------------- #
