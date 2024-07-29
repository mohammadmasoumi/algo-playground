
def lcs(s1, s2, n, m):

    if m == 0 or n == 0:
        return 0
    elif s1[n-1] == s2[m-1]:
        return 1 + lcs(s1, s2, n-1, m-1)
    else:
        return max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1))

print(lcs("AGGTAB", "GXTXAYB", 6, 7))