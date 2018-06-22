# -*- coding: utf-8 -*-
# coding UTF-8
import random

N = 100
A = 0

random.seed(1)
a = [random.randint(0, 100) for i in range(N)]  # 小切手の配列
for i in range(N):
    print(a[i])
    if random.randint(0, 1) != 0:
        A += a[i]

# 初期化
dp = [-1 for i in range(A+1)]
dp[0] = 0

# DP
for i in range(N):
    for j in reversed(range(A+1)):
        if(dp[j] == -1):
            continue
        if ((a[i]+j <= A) and (dp[a[i]+j] == -1)):
            dp[a[i]+j] = a[i]
    if(dp[A] != -1):
        break
print("Answer:" + str(A))
check = 0
x = A
while(1):
    check += dp[x]
    print(dp[x])
    x = x-dp[x]
    if(x <= 0):
        break
print("check="+str(check))
if check == A:
    print("OK")
