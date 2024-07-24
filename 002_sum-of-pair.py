numbers = [8, 10, 2, 9, 7, 5, 6, 1]
target = 11

dp ={}
for number in numbers:
    diff = target - number
    if dp.get(number):
        print(f"Congrates! you've found a pair({number}, {dp.get(number)})" )
    else:
        dp[diff] = number