n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()

dp = [[-1] * (k+1) for _ in range(n)]

def rec(i, teams):
    if i == n or teams == 0:
        return 0
    
    if dp[i][teams] != -1:
        return dp[i][teams]

    #take 
    start = arr[i]
    for j in range(i, n):
        if arr[j] - start <= 5:
            j += 1
        else:
            break
    res1 = j-i + rec(j, teams-1)

    #don't take
    res2 = rec(i+1, teams)

    dp[i][teams] = max(res1, res2)
    return dp[i][teams]
    
print(rec(0, k))