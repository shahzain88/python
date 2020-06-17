# debugging

# linting
#ide/ editor
# read error

# PDB
# python debugging

import pdb
num3 = 0


def add(num1, num2):
    num3 = 0
    pdb.set_trace()
    adding = num1 + num2
    num3 = adding

    return adding


print(f"first{num3}")
num3 = add(1, "hhoo")
print(f"second{num3}")
num3 = add(2, 3)
print(num3)
