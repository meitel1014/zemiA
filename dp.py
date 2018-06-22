# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext
import random

conf = SparkConf().setMaster("local").setAppName("DynamicPlanning")
sc = SparkContext(conf = conf)

def table(rdd):
    return [(i,-1) for i in range(rdd[0]*100,(rdd[0]+1)*100-1)]

N = 10
A = 0

random.seed(1)
a = [random.randint(0, 10) for i in range(N)]  # 小切手の配列
for i in range(N):
#    print(a[i])
    if random.randint(0, 1) != 0:
        A += a[i]

# 初期化
dp = [i for i in range(100)]

dp_rdd=sc.parallelize(dp)
dp_rdd=dp_rdd.map(lambda x:(x,-1))
while(dp_rdd.count()<A+1):
    dp_rdd=dp_rdd.flatMap(table)
    
dp_rdd=dp_rdd.map(lambda x:(x[0],0)if x[0]==0 else x)
dp_rdd.sortByKey()
results=dp_rdd.collect()

for result in results:
    print("dp["+str(result[0])+"]:"+str(result[1]))

# DP
for i in range(N):
    for j in reversed(range(A+1)):
        if(dp_rdd.lookup(j) == -1):
            continue
        if ((a[i]+j <= A) and (dp_rdd.lookup(a[i]+j) == -1)):
            #dp[a[i]+j] = a[i]
            
    if(dp_rdd.lookup(A) != -1):
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
