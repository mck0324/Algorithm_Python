def problem_11726(num):
    dp = [0]*101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,101):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[num]        
    
print(problem_11726(2)) 
print(problem_11726(6)) 
print(problem_11726(12))