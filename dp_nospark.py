# coding:utf-8
import random
import pdb

N = 3
A = 0

random.seed(1)
a = [random.randint(0, 100) for i in range(N)]  # 小切手の配列
for i in range(N):
    if random.randint(0, 1) != 0:
        A += a[i]

# 初期化
dp = [[(False,[]) for j in range(A+1)] for i in range(N+1)]
dp[0][0] = (True,[])
pdb.set_trace()
# DP
for i in range(N):
    for j in range(A+1):
        if a[i] <= j:  # i+1番目の数字a[i]を足せるかも
            if dp[i][j - a[i]][0]:
                dp[i + 1][j] = (True,dp[i][j-a[i]][1]+[a[i],])

            elif dp[i][j][0]:
                dp[i+1][j] = (True,dp[i][j][1])
                
            else:
                dp[i+1][j] = (False,[])
        else:  # 入る可能性はない
            dp[i+1][j] = (False,[])

print("Target:" + str(A))
sum = 0
for selected in dp[N][A][1]:
    sum+=selected
print("Answer:" + str(sum))
if sum != A:
    print("error!")
