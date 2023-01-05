def tower_builder(n_floors):
    """Build Tower
    Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

    For example, a tower with 3 floors looks like this:

    [
      "  *  ",
      " *** ",
      "*****"
    ]
    And a tower with 6 floors looks like this:

    [
      "     *     ",
      "    ***    ",
      "   *****   ",
      "  *******  ",
      " ********* ",
      "***********"
    ]"""

    lst = []
    for i in range(n_floors):
        lst.append(f"{' ' * (n_floors - 1 - i)}{'*' * i}*{'*' * i}{' ' * (n_floors - 1 - i)}")
    return lst


def solution(s):
    """
    Complete the solution so that the function will break up camel casing, using a space between words.
    Example
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""
    """
    res = ''
    for i in s:
        if i.isupper():
            res += ' '
        res += i
    return res
