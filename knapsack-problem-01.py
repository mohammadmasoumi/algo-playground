

"""
            capacities
                0   1   2   3   4   5   6   7   8   9   10  
weigth  items       
         0      0   0   0   0   0   0   0   0   0   0   0
   2     1      0   0   300 300 300 300 300 300 300 300 300    
   1     2      0   200 300 500 500 500 500 500 500 500 500
   5     3      0   200 300 500 500 500 600 700 900 900 900
   4     4      0   200 300 500 700 800 10001000100011001200 
"""


profits = [300, 200, 400, 500]
weights = [2, 1, 5, 3]

capacity = 10

dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights)+1)]
from pprint import pprint

for idx, w in enumerate(weights):
    for c in range(capacity + 1):
        if c >= w:
            dp[idx+1][c] = max(profits[idx] + dp[idx][c-w], dp[idx][c])
        else:
            dp[idx+1][c] = dp[idx][c]

pprint(dp)
print(dp[-1][-1])