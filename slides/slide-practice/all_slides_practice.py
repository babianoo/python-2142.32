# All 4 lectures in one practice file.
#
# HOW TO USE
#   1. Pick a task, read its docstring, delete the `raise NotImplementedError`
#      line and write the function yourself (no peeking at the slides!).
#   2. Run the checker:
#          python all_slides_practice.py        -> every lecture
#          python all_slides_practice.py 3      -> only lecture 3
#          python all_slides_practice.py 2 4    -> lectures 2 and 4
#   3. Each task shows PASS / FAIL / TODO / ERROR / TIMEOUT.
#
# The slides used input() for most tasks. Here they take parameters instead
# so they can be checked automatically. "Predict the output" tasks are at
# the bottom of each lecture: fill in the PREDICTIONS dict BEFORE running.

import hashlib
import os
import sys
import webbrowser

___ = "___"  # placeholder for predictions you haven't made yet


# =============================================================================
# LECTURE 1 -- Loops & Iterative Algorithms
# =============================================================================

def count_bob(s):
    """
    Return how many times 'bob' occurs in s (overlaps count).
    count_bob('azcbobobegghakl') -> 2
    """
    res = 0
    for i in range(0, len(s)):
        if s[i:i + 3] == "bob": res += 1
    return res

def longest_alpha_substring(s):
    """
    Return the longest substring of s whose letters are in alphabetical
    order. If two are equally long, return the first one.
    longest_alpha_substring('azcbobobegghakl') -> 'beggh'
    longest_alpha_substring('abcbcd')          -> 'abc'
    """
    current = s[0]
    best    = ""
    for i in range(1, len(s)):
        if s[i - 1] >= s[i]:
            current += s[i]
        if len(current) > len(best):
            best = current
    return best

def square_by_addition(x):
    """
    Return x*x using a WHILE loop and repeated addition (no * or **).
    x is an int >= 0.
    """
    res = x
    while x > 1:
        res += x
        x   -= 1
    return res

def cube_root_while(x):
    """
    Exhaustive enumeration with a WHILE loop: count up until you reach
    the cube root. Return the integer cube root, or None if x is not a
    perfect cube. Must also work for negative x (hint: abs(), then put
    the sign back at the end).
    cube_root_while(27) -> 3,  cube_root_while(-8) -> -2,  cube_root_while(10) -> None
    """
    negative = False
    if x < 0:
        negative = True
        x = abs(x)
    i   = 0
    res = 0
    found = False
    while not found and i ** 3 < x:
        if i ** 3 == x:
            res = i
            found = True
        i += 1

    if not found:
        return None

    if negative:
        return -res

    return res

def cube_root_for(x):
    """
    Same as cube_root_while, but try every candidate with a FOR loop over
    a range. Only needs to handle x >= 0.
    """
    # Is this allowed?
    for i in range(0, x ** 1/3, 1):
        if i == x:
            return i
    return None

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
            break
        if guess ** 2 > x:
            right = guess
        else:
            left = guess
        guess = (right + left) / 2
    return guess

def bisection_cube_root(x, epsilon=0.01):
    """
    CHALLENGE from the slides: bisection search for a cube root that works
    for negative numbers AND for numbers between -1 and 1.
    Return just the answer (a float with abs(ans**3 - x) < epsilon).
    bisection_cube_root(-27) ~ -3,  bisection_cube_root(0.125) ~ 0.5
    """


def count_alerts(log, alert='FAILED'):
    """
    Given one line of an auth log, return how many words equal `alert`.
    count_alerts('OK FAILED OK OK FAILED FAILED OK FAILED') -> 4
    """
    raise NotImplementedError


def is_brute_force(log, threshold=3):
    """
    Return True if the log has `threshold` or more FAILED attempts.
    Use count_alerts -- don't repeat the loop.
    """
    raise NotImplementedError


def brute_force_pin(secret):
    """
    Try every 4-digit PIN from '0000' to '9999' in order and stop when it
    matches `secret`. Return (found_pin, guesses_needed).
    If nothing matches, return (None, 10000).
    brute_force_pin('0427') -> ('0427', 428)
    """
    raise NotImplementedError


def scope_l1_counter():
    """Given code (don't edit) -- used by the predictions below."""
    s = 'abcabc'
    i = 0
    total = 0
    while i < len(s):
        if s[i] == 'c':
            total += i
        i += 2
    return total


PREDICTIONS_L1 = {
    # Replace each ___ with what you think the expression evaluates to.
    "scope_l1_counter()": ___,
    "list(range(2, 11, 3))": ___,
    "str(7).zfill(4)": ___,
    "'a b  c'.split(' ')": ___,
}


# =============================================================================
# LECTURE 2 -- Numbers, Floats & Functions
# =============================================================================

def int_to_binary(n):
    """
    Return the binary string of an integer WITHOUT using bin() or format().
    Use % 2 to get the last bit and // 2 to shift right.
    int_to_binary(19) -> '10011',  int_to_binary(0) -> '0',  int_to_binary(-5) -> '-101'
    """
    raise NotImplementedError


def frac_to_binary(x):
    """
    0 < x < 1. Multiply x by 2**p (smallest p that gives a whole number),
    convert that to binary, then put the point back p places from the right.
    frac_to_binary(0.375) -> '0.011'
    frac_to_binary(0.5)   -> '0.1'
    What if: try 0.1 once yours works. Why is p so large?
    """
    raise NotImplementedError


def newton_sqrt(k, epsilon=0.01):
    """
    Newton-Raphson for the square root of k: start with guess = k/2 and
    improve it with   g - (g**2 - k) / (2*g)   until abs(g*g - k) < epsilon.
    Return (guess, num_guesses).
    """
    raise NotImplementedError


def is_even(i):
    """Return True if i is even, otherwise False."""
    raise NotImplementedError


def full_name(name, last_name, reverse=False):
    """
    Default arguments. Return the tuple (name, last_name), or
    (last_name, name) when reverse is True.
    full_name('Maksim', 'Iavich')       -> ('Maksim', 'Iavich')
    full_name('Maksim', 'Iavich', True) -> ('Iavich', 'Maksim')
    """
    raise NotImplementedError


def hash_password(pw):
    """
    Return the SHA-256 hex digest (a 64-char string) of the password.
    Strings must be turned into bytes before hashing.
    """
    raise NotImplementedError


def make_qr(url, filename):
    """
    Save a QR code PNG for `url` at `filename` using the qrcode library.
    (pip install qrcode[pil])  -- this one gets skipped if qrcode isn't installed.
    """
    raise NotImplementedError


def mystery_l2(i):
    """Given code (don't edit) -- used by the predictions below."""
    print("hi")
    i % 2 == 0


PREDICTIONS_L2 = {
    "mystery_l2(4)": ___,          # careful -- look at the last line
    "0.1 + 0.2 == 0.3": ___,
    "7 // 2": ___,
    "-7 // 2": ___,
    "int('101', 2)": ___,
}


# =============================================================================
# LECTURE 3 -- Scope & Recursion
# =============================================================================

def mult_recur(a, b):
    """a * b for int b >= 1, using RECURSION: a*b = a + a*(b-1). No * allowed."""
    raise NotImplementedError


def mult_iter(a, b):
    """a * b for int b >= 0, using a WHILE loop. No * allowed."""
    raise NotImplementedError


def fact_recur(n):
    """n! for int n >= 1, recursively."""
    raise NotImplementedError


def fact_iter(n):
    """n! for int n >= 0, with a FOR loop over range."""
    raise NotImplementedError


def iter_power(base, exp):
    """base**exp for int exp >= 0, by repeated multiplication (no **)."""
    raise NotImplementedError


def recur_power(base, exp):
    """
    base**exp for int exp >= 0, recursively (no **).
    What's the smallest exp you know the answer for?
    """
    raise NotImplementedError


def reverse_recur(s):
    """Return s reversed, recursively. No slicing with [::-1]."""
    raise NotImplementedError


def is_weak_palindrome(pw):
    """True if the password reads the same backwards. Use reverse_recur."""
    raise NotImplementedError


def hash_chain(text, n):
    """
    Hash `text` with SHA-256 n times, RECURSIVELY.
    hash_chain(t, 0) is t, hash_chain(t, 1) is sha(t), hash_chain(t, 2) is sha(sha(t)) ...
    You may call hash_password from lecture 2.
    """
    raise NotImplementedError


# Given code (don't edit) -- trace these by hand for the predictions below.
def foo_a(x, y=5):
    def bar(x):
        return x + 1
    return bar(y * 2)


def foo_b(x):
    def bar(z, x=0):
        return z + x
    return bar(3)


def foo_c(x):
    def bar(z, x=0):
        return z + x
    return bar(3, x)


PREDICTIONS_L3 = {
    "foo_a(3)": ___,
    "foo_a(3, 0)": ___,
    "foo_b(5)": ___,
    "foo_c(2)": ___,
    "'Hello there'.count('e')": ___,
    "'Hello there'.find('z')": ___,
    "'Hello there'.index('z')": ___,   # if it crashes, write the error name as a string, e.g. 'TypeError'
    "'Hello there'.replace('e', '*')": ___,
    "'Hello there'.swapcase()": ___,
}


# =============================================================================
# LECTURE 4 -- Recursion, Modules & Tuples
# =============================================================================

def is_pal(s):
    """
    True if s (a string OR a list) is a palindrome, RECURSIVELY:
    length 0 or 1 -> palindrome; otherwise first == last AND the middle is one.
    """
    if len(s) == 0 or len(s) == 1: return True

    # I don't know

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

def gcd_iter(a, b):
    """GCD of two positive ints: start at min(a, b) and count down."""
    m = min(a, b)
    # I don't know

def gcd_recur(a, b):
    """
    GCD with Euclid's algorithm, recursively:
    gcd(a, b) = gcd(b, a % b), and gcd(a, 0) = a.
    """
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)

def fib(x):
    """
    Fibonacci with TWO base cases: fib(0) = 1, fib(1) = 1,
    fib(x) = fib(x-1) + fib(x-2).
    """
    raise NotImplementedError


# MODULES: there is no function for this one. Create a file circle.py in this
# same folder containing  pi = 3.14159,  area(radius)  and  circumference(radius).
# The checker imports it.


def write_lines(filename, lines):
    """Write each string in `lines` to the file, one per line (with '\\n')."""
    raise NotImplementedError


def read_lines(filename):
    """Read the file back and return a list of lines WITHOUT the '\\n'."""
    raise NotImplementedError


def quotient_and_remainder(x, y):
    """Return the tuple (x // y, x % y)."""
    raise NotImplementedError


def get_data(a_tuple):
    """
    a_tuple is a tuple of (number, word) pairs.
    Return (min_number, max_number, how_many_unique_words).
    Build up the numbers and words as TUPLES (not lists) while you loop.
    get_data(((1, 'a'), (2, 'b'), (1, 'a'), (7, 'b'))) -> (1, 7, 2)
    """
    raise NotImplementedError


def odd_tuples(a_tup):
    """
    Return a new tuple with every other element, starting with the first.
    odd_tuples(('I', 'am', 'a', 'test', 'tuple')) -> ('I', 'a', 'tuple')
    Do it with a loop first. Then ask yourself: could slicing do it in one go?
    """
    raise NotImplementedError


def open_report(url, opener=webbrowser.open):
    """
    Print 'Opening report: <url>' and open it with `opener`.
    (opener defaults to webbrowser.open. The checker passes a fake one so
    no real browser pops up.)
    """
    raise NotImplementedError


SCAN_RESULTS = [
    ('10.0.0.5', 22, 'ssh'),
    ('10.0.0.5', 80, 'http'),
    ('10.0.0.5', 443, 'https'),
    ('10.0.0.7', 3306, 'mysql'),
    ('10.0.0.7', 443, 'https'),
]


def web_services(scan):
    """
    scan is a list of (ip, port, service) tuples.
    Return a list of (ip, service) for every record on port 80 or 443,
    in the same order. Unpack the tuple right in the for loop.
    """
    raise NotImplementedError


PREDICTIONS_L4 = {
    "fib(12)  # female rabbits after one year": ___,
    "(2, 'one', 3)[1:2]": ___,
    "(2, 'one', 3) + (5, 6)": ___,
    "swap_wrong(1, 2)": ___,
    "type((5))": ___,           # write the type itself, e.g. str or tuple
    "type((5,))": ___,
}


def swap_wrong(x, y):
    """Given code (don't edit) -- used by the predictions above."""
    x = y
    y = x
    return (x, y)


# =============================================================================
# CHECKER -- you don't need to edit anything below this line
# =============================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
SHA_ABC = 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
TESTS = []


class Skip(Exception):
    pass


def check(lecture, name):
    def register(fn):
        TESTS.append((lecture, name, fn))
        return fn
    return register


def close(a, b, tol=1e-6):
    return abs(a - b) <= tol


def calls_itself(fn):
    if 'NotImplementedError' in fn.__code__.co_names:
        raise NotImplementedError
    return fn.__name__ in fn.__code__.co_names


def check_predictions(predictions, scope):
    blanks = [k for k, v in predictions.items() if v is ___]
    if blanks:
        raise NotImplementedError(f"{len(blanks)} prediction(s) still ___")
    wrong = []
    for expr, guess in predictions.items():
        try:
            actual = eval(expr.split('#')[0], scope)
        except NotImplementedError:
            raise Skip(f"implement the function used in {expr!r} first")
        except Exception as e:
            actual = type(e).__name__
        same = (close(guess, actual)
                if isinstance(guess, float) and isinstance(actual, (int, float))
                else guess == actual)
        if not same:
            wrong.append(expr)
    assert not wrong, "wrong: " + ", ".join(wrong)


# ---- Lecture 1 ----

@check(1, "count_bob")
def _():
    assert count_bob('azcbobobegghakl') == 2
    assert count_bob('bobobob') == 3
    assert count_bob('bo') == 0


@check(1, "longest_alpha_substring")
def _():
    assert longest_alpha_substring('azcbobobegghakl') == 'beggh'
    assert longest_alpha_substring('abcbcd') == 'abc', "ties -> first one"
    assert longest_alpha_substring('zyx') == 'z'
    assert longest_alpha_substring('abcdz') == 'abcdz', "is the last run counted?"


@check(1, "square_by_addition")
def _():
    assert square_by_addition(3) == 9
    assert square_by_addition(0) == 0
    assert square_by_addition(12) == 144


@check(1, "cube_root_while")
def _():
    assert cube_root_while(27) == 3
    assert cube_root_while(0) == 0
    assert cube_root_while(10) is None
    assert cube_root_while(-8) == -2, "negatives"
    assert cube_root_while(-9) is None


@check(1, "cube_root_for")
def _():
    assert cube_root_for(27) == 3
    assert cube_root_for(1) == 1
    assert cube_root_for(0) == 0
    assert cube_root_for(26) is None


@check(1, "approx_cube_root")
def _():
    g, n = approx_cube_root(27)
    assert abs(g ** 3 - 27) < 0.01 and n > 0
    g, n = approx_cube_root(-8)
    assert abs(g ** 3 + 8) < 0.01, "negatives"


@check(1, "bisection_sqrt")
def _():
    ans, n = bisection_sqrt(25)
    assert abs(ans ** 2 - 25) < 0.01
    assert n < 30, "bisection should take ~log2 steps, not thousands"


@check(1, "bisection_sqrt (challenge: 0 < x < 1)")
def _():
    ans, n = bisection_sqrt(0.25)
    assert abs(ans ** 2 - 0.25) < 0.01


@check(1, "bisection_cube_root (challenge)")
def _():
    for x, root in [(27, 3), (1000, 10), (-27, -3), (0.125, 0.5), (-0.125, -0.5)]:
        ans = bisection_cube_root(x)
        assert abs(ans ** 3 - x) < 0.01, f"x = {x}"


@check(1, "count_alerts + is_brute_force")
def _():
    log = 'OK FAILED OK OK FAILED FAILED OK FAILED'
    assert count_alerts(log) == 4
    assert count_alerts(log, 'OK') == 4
    assert count_alerts('OK OK') == 0
    assert is_brute_force(log) is True
    assert is_brute_force('OK FAILED FAILED') is False
    assert 'count_alerts' in is_brute_force.__code__.co_names, "reuse count_alerts"


@check(1, "brute_force_pin")
def _():
    assert brute_force_pin('0427') == ('0427', 428)
    assert brute_force_pin('0000') == ('0000', 1)
    assert brute_force_pin('9999') == ('9999', 10000)
    assert brute_force_pin('abcd') == (None, 10000)


@check(1, "predictions")
def _():
    check_predictions(PREDICTIONS_L1, globals())


# ---- Lecture 2 ----

@check(2, "int_to_binary")
def _():
    assert 'bin' not in int_to_binary.__code__.co_names, "no bin() allowed"
    assert int_to_binary(19) == '10011'
    assert int_to_binary(0) == '0'
    assert int_to_binary(1) == '1'
    assert int_to_binary(255) == '11111111'
    assert int_to_binary(-5) == '-101'


@check(2, "frac_to_binary")
def _():
    assert frac_to_binary(0.375) == '0.011'
    assert frac_to_binary(0.5) == '0.1'
    assert frac_to_binary(0.625) == '0.101'
    assert frac_to_binary(0.0625) == '0.0001', "leading zeros after the point"


@check(2, "newton_sqrt")
def _():
    g, n = newton_sqrt(24)
    assert abs(g * g - 24) < 0.01
    assert 1 <= n <= 6, "Newton should need only a handful of guesses"
    g, n = newton_sqrt(2, 0.0001)
    assert abs(g * g - 2) < 0.0001


@check(2, "is_even + full_name")
def _():
    assert is_even(4) is True and is_even(3) is False and is_even(0) is True
    assert full_name('Maksim', 'Iavich') == ('Maksim', 'Iavich')
    assert full_name('Maksim', 'Iavich', True) == ('Iavich', 'Maksim')
    assert full_name('A', 'B', reverse=False) == ('A', 'B')


@check(2, "hash_password")
def _():
    assert hash_password('abc') == SHA_ABC
    assert len(hash_password('correcthorse')) == 64
    assert hash_password('correcthorse') != hash_password('correcthorse ')


@check(2, "make_qr")
def _():
    try:
        import qrcode  # noqa: F401
    except ImportError:
        raise Skip("pip install qrcode[pil]")
    import tempfile
    path = os.path.join(tempfile.mkdtemp(), 'link.png')
    make_qr('https://cu.edu.ge', path)
    assert os.path.exists(path), "no file saved"
    with open(path, 'rb') as f:
        assert f.read(4) == b'\x89PNG', "not a PNG"


@check(2, "predictions")
def _():
    check_predictions(PREDICTIONS_L2, globals())


# ---- Lecture 3 ----

@check(3, "mult_recur + mult_iter")
def _():
    assert calls_itself(mult_recur), "mult_recur must be recursive"
    assert mult_recur(5, 4) == 20 and mult_recur(7, 1) == 7
    assert mult_iter(5, 4) == 20 and mult_iter(7, 0) == 0


@check(3, "fact_recur + fact_iter")
def _():
    assert calls_itself(fact_recur), "fact_recur must be recursive"
    assert fact_recur(1) == 1 and fact_recur(5) == 120
    assert fact_iter(0) == 1 and fact_iter(1) == 1 and fact_iter(5) == 120


@check(3, "iter_power + recur_power")
def _():
    assert calls_itself(recur_power), "recur_power must be recursive"
    for f in (iter_power, recur_power):
        assert f(5, 3) == 125, f.__name__
        assert f(2, 1) == 2, f.__name__
        assert f(2, 0) == 1, f.__name__ + ": exp = 0"
        assert close(f(2.5, 2), 6.25), f.__name__ + ": float base"


@check(3, "reverse_recur + is_weak_palindrome")
def _():
    assert calls_itself(reverse_recur), "reverse_recur must be recursive"
    assert reverse_recur('abc') == 'cba'
    assert reverse_recur('') == ''
    assert reverse_recur('P@ssw0rd') == 'dr0wss@P'
    assert is_weak_palindrome('level') is True
    assert is_weak_palindrome('Str0ng!') is False
    assert 'reverse_recur' in is_weak_palindrome.__code__.co_names, "use reverse_recur"


@check(3, "hash_chain")
def _():
    assert calls_itself(hash_chain), "hash_chain must be recursive"
    assert hash_chain('secret', 0) == 'secret'
    assert hash_chain('abc', 1) == SHA_ABC
    assert hash_chain('abc', 3) == hash_chain(SHA_ABC, 2)


@check(3, "predictions")
def _():
    check_predictions(PREDICTIONS_L3, globals())


# ---- Lecture 4 ----

@check(4, "is_pal")
def _():
    assert calls_itself(is_pal), "is_pal must be recursive"
    assert is_pal('racecar') is True
    assert is_pal('ab') is False
    assert is_pal('') is True and is_pal('x') is True
    assert is_pal([1, 2, 1]) is True and is_pal([1, 2]) is False


@check(4, "is_pal_sentence (challenge)")
def _():
    assert is_pal_sentence('Able was I, ere I saw Elba') is True
    assert is_pal_sentence('Hello') is False
    assert 'is_pal' in is_pal_sentence.__code__.co_names, "reuse is_pal"


@check(4, "gcd_iter + gcd_recur")
def _():
    assert calls_itself(gcd_recur), "gcd_recur must be recursive"
    for f in (gcd_iter, gcd_recur):
        assert f(64, 48) == 16, f.__name__
        assert f(48, 64) == 16, f.__name__
        assert f(17, 5) == 1, f.__name__
        assert f(9, 9) == 9, f.__name__


@check(4, "fib")
def _():
    assert calls_itself(fib), "fib must be recursive"
    assert [fib(i) for i in range(7)] == [1, 1, 2, 3, 5, 8, 13]


@check(4, "circle.py module")
def _():
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    try:
        import circle
    except ModuleNotFoundError:
        raise NotImplementedError("create circle.py next to this file")
    assert circle.pi == 3.14159
    assert close(circle.area(3), 28.27431)
    assert close(circle.circumference(3), 18.84954)


@check(4, "write_lines + read_lines")
def _():
    import tempfile
    path = os.path.join(tempfile.mkdtemp(), 'kids')
    write_lines(path, ['alice', 'bob'])
    with open(path) as f:
        assert f.read() == 'alice\nbob\n', "file content should be 'alice\\nbob\\n'"
    assert read_lines(path) == ['alice', 'bob']


@check(4, "quotient_and_remainder")
def _():
    assert quotient_and_remainder(4, 5) == (0, 4)
    assert quotient_and_remainder(17, 5) == (3, 2)
    assert type(quotient_and_remainder(1, 1)) is tuple


@check(4, "get_data")
def _():
    result = get_data(((1, 'a'), (2, 'b'), (1, 'a'), (7, 'b')))
    assert result == (1, 7, 2) and type(result) is tuple
    assert get_data(((5, 'x'),)) == (5, 5, 1)


@check(4, "odd_tuples")
def _():
    assert odd_tuples(('I', 'am', 'a', 'test', 'tuple')) == ('I', 'a', 'tuple')
    assert odd_tuples((2, 2, 15, 18, 20)) == (2, 15, 20)
    assert odd_tuples(()) == ()
    assert type(odd_tuples((1, 2))) is tuple


@check(4, "open_report")
def _():
    opened = []
    open_report('https://cu.edu.ge', opener=opened.append)
    assert opened == ['https://cu.edu.ge'], "call opener(url) exactly once"


@check(4, "web_services")
def _():
    assert web_services(SCAN_RESULTS) == [
        ('10.0.0.5', 'http'), ('10.0.0.5', 'https'), ('10.0.0.7', 'https')]
    assert web_services([]) == []


@check(4, "predictions")
def _():
    check_predictions(PREDICTIONS_L4, globals())


def run_one(fn, timeout=3):
    """Run a check in a thread so an infinite loop shows up as TIMEOUT."""
    import threading
    import time
    outcome = {}

    class Timeout(BaseException):
        pass

    def target():
        # Stop a runaway loop for real, so it can't slow down later checks.
        deadline = time.time() + timeout

        def tracer(frame, event, arg):
            if time.time() > deadline:
                raise Timeout
            return tracer

        sys.settrace(tracer)
        try:
            fn()
            outcome['status'] = ('PASS', '')
        except Timeout:
            outcome['status'] = ('TIMEOUT', 'still running -- infinite loop?')
        except Skip as e:
            outcome['status'] = ('SKIP', str(e))
        except NotImplementedError as e:
            outcome['status'] = ('TODO', str(e))
        except AssertionError as e:
            outcome['status'] = ('FAIL', str(e))
        except RecursionError:
            outcome['status'] = ('ERROR', 'RecursionError -- is your base case ever reached?')
        except Exception as e:
            outcome['status'] = ('ERROR', f"{type(e).__name__}: {e}")
        finally:
            sys.settrace(None)

    t = threading.Thread(target=target, daemon=True)
    t.start()
    t.join(timeout + 2)
    return outcome.get('status', ('TIMEOUT', 'still running -- infinite loop?'))


def run_tests(lectures):
    counts = {}
    current = None
    for lecture, name, fn in TESTS:
        if lectures and lecture not in lectures:
            continue
        if lecture != current:
            current = lecture
            print(f"\n=== Lecture {lecture} ===")
        status, msg = run_one(fn)
        counts[status] = counts.get(status, 0) + 1
        print(f"  [{status:7}] {name}" + (f"  -- {msg}" if msg and status != 'TODO' else ''))
    total = sum(counts.values())
    print(f"\n{counts.get('PASS', 0)}/{total} passing  " +
          "  ".join(f"{k}: {v}" for k, v in sorted(counts.items()) if k != 'PASS'))


if __name__ == "__main__":
    run_tests({int(a) for a in sys.argv[1:]})
