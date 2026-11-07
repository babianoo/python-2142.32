def approx_cube_root(x, epsilon=0.01, increment=0.0001):
    """
    Approximate the cube root of x by starting at 0 and stepping by
    `increment` until guess**3 is within epsilon of x.
    Return a tuple: (guess, num_guesses)       e.g. return guess, num_guesses
    Should work for negative x too.
    """
    guess   = 0
    g_count = 0

    found = False
    while guess ** 3 <= x - epsilon:
        guess   += increment
        g_count += 1
    res = (guess, g_count)

    return res

def bisection_sqrt(x, epsilon=0.01):
    """
    Approximate the square root of x with bisection search: keep an
    interval [low, high], guess the middle, throw away the half that
    can't contain the answer.
    Return (ans, num_guesses).

    CHALLENGE (separate check): make it work for 0 < x < 1 as well.
    Think: if x = 0.25, is the answer inside [0, x]?
    """
    if x > 0 and x < 1:
        right = 1
        left  = 0

        guess = 0.5

        found = False
        while not found:
            if abs(x - (guess ** 2)) <= epsilon:
                found = True
            if guess ** 2 < x:
                right = guess
            else:
                left  = guess
            guess = (right + left) * 2
        return guess

    right = x
    left  = 0

    guess = x / 2

    found = False
    while not found:
        if abs(x - (guess ** 2)) <= epsilon:
            found = True
        if guess ** 2 > x:
            right = guess
        else:
            left = guess
        guess = (right + left) / 2
    return guess

def is_pal_sentence(text):
    """
    CHALLENGE: palindrome check that ignores case, spaces and punctuation.
    Clean the text first (lowercase, keep only letters), then call is_pal.
    is_pal_sentence('Able was I, ere I saw Elba') -> True
    """
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(" ", "")
    rvrsd = text[::-1]
    if text == rvrsd:
        return True
    return False

print(approx_cube_root(27))
print(bisection_sqrt(25))
print(is_pal_sentence('Able was I, ere I saw Elba'))