# tests/simpleDocTest.py
# Shows a simple Example of doctest in Python

"""
Outside of a function
>>> area(5,5)
25
"""

def area(x,y):
    """Inside of a function
    Return the area of an recangle.

    >>> area(1,2)
    2
    >>> area(0,2)
    Traceback (most recent call last):
        ...
    ValueError: x must be > 0
    >>> area(2,0)
    Traceback (most recent call last):
        ...
    ValueError: y must be > 0
    """    
    if not x > 0:
        raise ValueError("x must be > 0")
    if not y > 0:
        raise ValueError("y must be > 0")    
    return x*y


if __name__ == "__main__":
    import doctest
    doctest.testmod()