def get_dp(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[1][1] = triangle[0][0]
    
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i-1][j-1]

    
    
    return (max(dp[n]))


def solution(triangle):
    return get_dp(triangle)
