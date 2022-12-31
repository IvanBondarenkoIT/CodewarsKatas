# Friend or Foe?
# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
def friend(x):
    return [i for i in x if len(i) == 4]


# DESCRIPTION:
# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    return '-'.join(f'{ch}{ch * ind}'.capitalize() for ind, ch in enumerate(s))


# Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()