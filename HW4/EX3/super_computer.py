import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

experiments = {}
n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    experiments[j] = d
exp_count = 0
start, end = None, None
for k, v in sorted(experiments):
    if start is None:
        start, end = k, v
        continue
    if k < end:
        exp_count += 1
    start, end = k, v


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(exp_count))