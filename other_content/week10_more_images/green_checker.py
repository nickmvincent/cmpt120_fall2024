def is_green(pixel):
    """
    Returns True if the RGB values of pixel combine to green.
    Assume "green" within 30 of 0,255,0 respectively
    Input: a 3–valued list representing a pixel
    Output: True if green, False otherwise
    """
    r, g, b = pixel
    return r < 120 and g > 170 and b < 120

