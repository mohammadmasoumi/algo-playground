from pprint import pprint

s1 = "AGGTAB"
s2 = "GXTXAYB"

n, m = len(s1), len(s2)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


print(dp[-1][-1])
pprint(dp)


