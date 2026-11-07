def reverse_str(s):
    """Returns a reversed version of 's'"""
    return s[::-1]

def is_even(i):
    """
    Returns True if the given number is even,
    otherwise returns False.
    """
    return i % 2 == 0


print(reverse_str("abc hello"))
print(is_even(3))