
def lcs(s1, s2, n, m, dp):
    if m == 0 or n == 0:
        return 0
    elif s1[n-1] == s2[m-1]:
        dp[n][m] = 1 + lcs(s1, s2, n-1, m-1, dp) 
        return dp[n][m] 

    dp[n][m] = max(lcs(s1, s2, n-1, m, dp), lcs(s1, s2, n, m-1, dp)) 
    return dp[n][m] 

s1 = "AGGTAB"
s2 = "GXTXAYB"

n, m = len(s1), len(s2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(lcs(s1, s2, n, m, dp))