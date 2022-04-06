import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

experiments = []
result = 0
last_expr = 0
for i in range(int(input())):
    j, d = [int(j) for j in input().split()]
    # We will create a matrix of all the experiments
    experiments.append((j, j + d))
    last_expr = max(last_expr, experiments[i][1])
# we will sort all the experiments by the second argument which is the end date
experiments.sort(key=lambda exp: exp[1])
# Initialize a timeline line
timeline = [0] * last_expr
for c in experiments:
    # We check if there is a free timeline for the experiment
    if 1 not in timeline[c[0]:c[1]]:
        result += 1
        # We mark the time as taken
        timeline[c[0]:c[1]] = [1] * (c[1] - c[0])

print(result)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



