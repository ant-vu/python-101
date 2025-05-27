import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_hex = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

tmp = _hex[2:]
res = ""
for i in range(len(tmp), -1, -2):
    res += tmp[i-2:i] + " "
print(res[:-2])
