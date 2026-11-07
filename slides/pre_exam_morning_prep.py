# Pre-exam morning prep -- 5 small ORIGINAL problems built from lectures 1-4.
#
# Focus: recursion, string slicing, tuples, binary (bisection) search.
#
# HOW TO USE
#   1. Read the docstring, delete the `raise NotImplementedError` line and
#      write the function yourself. No slides, no AI.
#   2. Problem 2 has a PREDICTIONS dict: fill it in BEFORE running.
#   3. Run:   python pre_exam_morning_prep.py
#      Each problem shows PASS / FAIL / TODO / ERROR.
#
# Rules for the recursion problems: no loops, no built-ins that do the
# work for you (.count(), min(), max(), `in` on the whole sequence).

import sys

___ = "___"  # placeholder for predictions you haven't made yet


# =============================================================================
# PROBLEM 1 -- Recursion + slicing   (lecture 3: reverse a string, lecture 4: isPal)
# =============================================================================

def count_char(s, ch):
    """
    Return how many times the single character ch appears in s.
    RECURSIVE. No loops, no s.count().

    count_char('banana', 'a') -> 3
    count_char('banana', 'z') -> 0
    count_char('', 'a')       -> 0

    Think before coding:
      - What is the smallest string you already know the answer for?
      - If you look ONLY at s[0], what does it contribute (0 or 1)?
      - Who handles the rest of the string, s[1:]?
    """
    if len(s) == 0:
        return 0
    else:
        return (s[0] == ch) + count_char(s[1:], ch)

# =============================================================================
# PROBLEM 2 -- String slicing   (lecture 1: 'bob' / longest substring)
# =============================================================================

# Part A -- predict the output. Write the exact string Python would give.
# Do it on paper first: index each letter 0..6 and -7..-1.
#
#        0123456
#   w = "MORNING"
#
PREDICTIONS = {
    'w[2:5]':    "RNIN",
    'w[:3]':     "MO",
    'w[-3:]':    "NING",
    'w[::2]':    "MRIG",
    'w[::-1]':   "GNINROM",
    'w[5:2:-1]': "NIN",
    'w[10:]':    "Uhm, maybe, but maybe Python handles this and wraps around so it would become index 4. Return: \"NG\"",   # careful: is this an error?
}

def mirror(s):
    """
    Part B. Return s followed by its reverse, WITHOUT repeating the last
    letter, so the result is always a palindrome. Use slicing only
    (no loops, no reversed()).

    mirror('abc')  -> 'abcba'
    mirror('step') -> 'stepets'
    mirror('x')    -> 'x'
    mirror('')     -> ''

    Hint: you need "s reversed, but skip its first character".
    Can one slice do that, or is it easier as two slices?
    """
    # Get every char except last
    res = s[0:len(s) - 1]
    rev = s[::-1]
    return res + rev

# =============================================================================
# PROBLEM 3 -- Tuples   (lecture 4: get_data, oddTuples, scan records)
# =============================================================================

def exam_summary(records):
    """
    records is a TUPLE of (name, score) tuples, e.g.
        (('Ana', 72), ('Gio', 45), ('Nino', 91), ('Luka', 50))

    Return a TUPLE of three things:
        (passed, top_name, average)
      passed   -- tuple of names with score >= 51, in the original order
      top_name -- name with the highest score (first one if there's a tie)
      average  -- average score as a float

    exam_summary(that example) -> (('Ana', 'Nino'), 'Nino', 64.5)

    Rules:
      - Build `passed` as a tuple from the start (start with () and add
        to it). Don't make a list and convert it.
      - Unpack each record in the for line itself: for (name, score) in ...
      - Don't use max() or sum().
    Assume records has at least one entry.

    Trap to think about: how do you add ONE name to a tuple?
    What is the difference between ('Ana') and ('Ana',)?
    """
    passed  = ()
    average  = ()

    best    = 0
    best_res = ()
    current = records[0][1]
    average = 0.0

    for (name, score) in records:
        average += score
        current = score
        if current > best:
            best = current
            best_res = name
        if score >= 51:
            passed += (name,)

    average /= len(records)

    return (passed, best_res, average)

# =============================================================================
# PROBLEM 4 -- Binary search on a sorted tuple   (lecture 1/2: bisection sqrt)
# =============================================================================

def find_seat(seats, target):
    """
    seats is a SORTED tuple of distinct ints (seat numbers sold for a show).
    Use BISECTION (no `in`, no .index(), no scanning one by one) to find
    target.

    Return a tuple (index, steps):
      index -- position of target in seats, or -1 if it isn't there
      steps -- how many times you looked at a middle element

    seats = (3, 8, 15, 21, 30, 42, 57)
    find_seat(seats, 21) -> (3, 1)     # middle on the first look
    find_seat(seats, 42) -> (5, 2)
    find_seat(seats, 3)  -> (0, 3)
    find_seat(seats, 10) -> (-1, 3)
    find_seat((), 5)     -> (-1, 0)

    In the sqrt slides, low/high were VALUES (floats). Here they are
    INDEXES (ints). So:
      - What are low and high at the start?
      - mid = ? (it must be an int -- which division operator?)
      - If seats[mid] is too small, which half do you throw away, and
        what does low or high become? (mid, or mid + 1? why?)
      - When do you stop if the target isn't there?
    """
    high  = len(seats) - 1
    low   = 0
    steps = 0

    while low < high:
        index = (high + low) // 2
        steps += 1
        if seats[index] == target:
            return (index, steps)
        if seats[index] > target:
            high = index
        elif seats[index] < target:
            low = index + 1
    return (-1, steps)

# =============================================================================
# PROBLEM 5 -- Recursion that RETURNS a tuple   (lectures 3 + 4 combined)
# =============================================================================

def lowest_highest(t):
    """
    t is a non-empty tuple of numbers. Return the tuple (lowest, highest).
    RECURSIVE. No loops, no min(), no max(), no sorted().

    lowest_highest((4,))             -> (4, 4)
    lowest_highest((7, 2, 9, 4))     -> (2, 9)
    lowest_highest((-1, -8, 0, -3))  -> (-8, 0)

    Think:
      - Base case: a tuple with ONE element. What are lowest and highest?
      - Recursive case: ask the function about t[1:]. It hands you back
        a tuple -- unpack it: (lo, hi) = lowest_highest(t[1:])
      - Now compare t[0] with lo and with hi. What do you return?
    """
    if len(t) == 1:
        return (t[0], t[0])        
    (lo, hi) = lowest_highest(t[1:])
    if t[0] < lo:
        lo = t[0]
    if t[0] > hi:
        hi = t[0]
    return (lo, hi)

# =============================================================================
# CHECKER -- don't edit below this line
# =============================================================================

W = "MORNING"


def test_1():
    assert count_char('banana', 'a') == 3
    assert count_char('banana', 'b') == 1
    assert count_char('banana', 'z') == 0
    assert count_char('', 'a') == 0
    assert count_char('aaaa', 'a') == 4


def test_2():
    wrong = [k for k, v in PREDICTIONS.items() if v == ___ or v != eval(k, {'w': W})]
    todo = [k for k, v in PREDICTIONS.items() if v == ___]
    if todo:
        raise NotImplementedError
    assert not wrong, "wrong predictions: " + ", ".join(wrong)
    assert mirror('abc') == 'abcba'
    assert mirror('step') == 'stepets'
    assert mirror('x') == 'x'
    assert mirror('') == ''


def test_3():
    recs = (('Ana', 72), ('Gio', 45), ('Nino', 91), ('Luka', 50))
    res = exam_summary(recs)
    assert type(res) is tuple, "return a tuple, not " + type(res).__name__
    assert type(res[0]) is tuple, "passed should be a tuple"
    assert res == (('Ana', 'Nino'), 'Nino', 64.5), "got " + repr(res)
    assert exam_summary((('Solo', 51),)) == (('Solo',), 'Solo', 51.0), \
        "one record, exactly 51 -> passes (note the comma in ('Solo',))"
    assert exam_summary((('A', 80), ('B', 80))) == (('A', 'B'), 'A', 80.0), \
        "tie -> first one"
    assert exam_summary((('X', 10), ('Y', 20)))[0] == (), "nobody passed -> ()"


def test_4():
    seats = (3, 8, 15, 21, 30, 42, 57)
    assert find_seat(seats, 21) == (3, 1)
    assert find_seat(seats, 42) == (5, 2)
    assert find_seat(seats, 3) == (0, 3)
    assert find_seat(seats, 57) == (6, 3)
    assert find_seat(seats, 10) == (-1, 3), "not found -> index -1"
    assert find_seat((), 5) == (-1, 0), "empty tuple -> no looks at all"
    for i, s in enumerate(seats):
        assert find_seat(seats, s)[0] == i
    big = tuple(range(0, 2000, 2))
    idx, steps = find_seat(big, 1234)
    assert idx == 617
    assert steps <= 11, "1000 items should take ~10 looks, you took %d" % steps


def test_5():
    assert lowest_highest((4,)) == (4, 4)
    assert lowest_highest((7, 2, 9, 4)) == (2, 9)
    assert lowest_highest((-1, -8, 0, -3)) == (-8, 0)
    assert lowest_highest((5, 5, 5)) == (5, 5)
    assert lowest_highest((1.5, 0.5)) == (0.5, 1.5)


def main():
    tests = [test_1, test_2, test_3, test_4, test_5]
    passed = 0
    for n, test in enumerate(tests, 1):
        try:
            test()
            status = "PASS"
            passed += 1
        except NotImplementedError:
            status = "TODO"
        except AssertionError as e:
            status = "FAIL  " + (str(e) or "a test case gave the wrong answer")
        except RecursionError:
            status = "ERROR RecursionError -- is your base case ever reached?"
        except Exception as e:
            status = "ERROR %s: %s" % (type(e).__name__, e)
        print("Problem %d: %s" % (n, status))
    print("\n%d / %d passed" % (passed, len(tests)))


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
