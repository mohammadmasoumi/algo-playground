

def edit_distance(s1, s2, n, m, dp):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif dp[n][m] != -1:
        return dp[n][m]
    elif s1[n-1] == s2[m-1]:
        dp[n][m] = max(edit_distance(s1, s2, n-1, m-1,  dp), dp[n-1][m-1])
    else:
        dp[n][m] = 1 + max(
            dp[n-1][m-1],
            min(
                min(
                    edit_distance(s1, s2, n-1, m-1, dp), 
                    edit_distance(s1, s2, n-1, m, dp)
                ), 
                edit_distance(s1, s2, n, m-1, dp)
            )
        )
    
    return dp[n][m]

str1 = "geek"
str2 = "gesek"
n = len(str1)
m = len(str2)
dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
print(edit_distance(str1, str2, n, m, dp))


str1 = "GEEXSFRGEEKKS"
str2 = "GEEKSFORGEEKS"
n = len(str1)
m = len(str2)
dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
print(edit_distance(str1, str2, n, m, dp))

str1 = "sunday"
str2 = "saturday"
n = len(str1)
m = len(str2)
dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
print(edit_distance(str1, str2, n, m, dp))

"""
Time Complexity: O(m x n) 
Auxiliary Space: O( m *n)+O(m+n) , (m*n) extra array space and (m+n) recursive stack space.
"""