def problem_11726(num):
    dp = [0]*1001
    dp[1] = 1
    dp[2] = 2
    for j in range(3,1001):
        dp[j] = dp[j-1] + dp[j-2]
    return dp[num] % 10007

print(problem_11726(4)) 