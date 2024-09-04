def problem_1904(num):
    dp = [0]*1000001
    dp[1] = 1
    dp[2] = 2
    for i in range(3,num+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num] % 15746
    
print(problem_1904(4))