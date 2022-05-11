# Map the three first inputs as integers
L, C, N = map(int, input().split())

# Create the group list by receiving the input N times
groups =  [int(input()) for _ in range(N)]

# {int: tuple} -> {Group index: (group earnings, next group index)}
# Will be used for collecting earning sthen summing them up separately
group_earning = {}

# Earning calculation per group
for first_index in range(N):
    attraction_intake = 0
    current_group = first_index
    # Will run while the attraction has space taking group size into consideration
    while attraction_intake + groups[current_group] <= L:
        attraction_intake += groups[current_group]
        current_group += 1
        if current_group == N:
            current_group = 0
        if current_group == first_index:
            break
    group_earning[first_index] = (attraction_intake, current_group)

result = 0
current_group = 0

# Earnings summary
for _ in range(C):
    result += group_earning[current_group][0]
    current_group = group_earning[current_group][1]

print(result)