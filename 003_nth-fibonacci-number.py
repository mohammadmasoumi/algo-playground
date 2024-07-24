
n = 9

def fibo(n, dp = {}):
    if n < 3:
        return 1
    elif dp.get(n):
        return dp.get(n)
    else:
        res = fibo(n-1, dp) + fibo(n-2, dp)
        dp[n] = res
        return res 

print(fibo(n)) 
