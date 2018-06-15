# coding UTF-8
import random

N = 100
A = 0

random.seed(1)
a = [random.randint(0, 100) for i in range(N)]  # 小切手の配列
for i in range(N):
    if random.randint(0, 1) != 0:
        A += a[i]

# 初期化
dp = [[0 for i in range(A+1)] for j in range(N+1)]
dp[0][0] = 1
flag = [0 for i in range(N)]

# DP
for i in range(N):
    for j in range(A+1):
        if a[i] <= j:  # i+1番目の数字a[i]を足せるかも
            if dp[i][j - a[i]]:
                dp[i + 1][j] = 1

            elif dp[i][j]:
                dp[i+1][j] = 1
        else:  # 入る可能性はない
            dp[i+1][j] = dp[i][j]

print("Answer:" + str(A))
check = 0
for i in range(N):
    if(flag[i]):
        print(a[i])
        check += a[i]

if check != A:
    print("error!")
