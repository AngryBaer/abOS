# abColor
Common tools related to digital color operations

## utils
Helper functions for converting and modifying color values

### rgb_to_float(rgb)
Convert a sequence of 256 color rgb values to float. Takes tuples and lists as input.

``
e.g. (0, 105, 255) -> (0.000, 0.412, 1.000)
``

### float_to_rgb(rgb)
Convert a sequence of floats to 256 color rgb values. Takes tuples and lists as input.

``
e.g. (0.000, 0.412, 1.000) -> (0, 105, 255)
``

### value_to_float(value)
Convert a single 256 color rgb value to float.

``
e.g. 105 -> 0.412
``

### value_to_rgb(value)
Convert a single float to a 256 color rgb value.

``
e.g. 0.412 -> 105
``
