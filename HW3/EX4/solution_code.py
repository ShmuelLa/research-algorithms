import sys
import math

"""
https://www.codingame.com/ide/puzzle/temperatures
codingam temperatures python solution
"""

n = int(input())  # the number of temperatures to analyse
abs_current_min = float('inf')
negative_list = []
positive_list = []


for i in input().split():
    t = int(i)
    if t < 0:
        negative_list.append(t)
    else:
        positive_list.append(t)
negative_list.sort(reverse=True)
positive_list.sort()
if not positive_list and negative_list:
    print(negative_list[0])
elif not negative_list and positive_list:
    print(positive_list[0])
elif n == 0:
    print(0)
elif abs(negative_list[0]) < positive_list[0]:
    print(negative_list[0])
else:
    print(positive_list[0])
