def solution(m, n, puddles):
    answer = 0
    mod = 1000000007

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for puddle in puddles:
        puddle[0], puddle[1] = puddle[1], puddle[0]
    
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    
    answer = dp[n][m] % mod
            
    return answer