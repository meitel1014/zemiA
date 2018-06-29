# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext
import random
import time

conf = SparkConf().setMaster("local").setAppName("DynamicPlanning")
sc = SparkContext(conf = conf)

def table(rdd):
    return [(i,-1) for i in range(rdd[0]*100,(rdd[0]+1)*100-1)]

N = 10
A = 0

random.seed(1)
a = random.sample(range(15),N)  # 小切手の配列
for i in range(N):
#    print(a[i])
    if random.randint(0, 1) != 0:
        A += a[i]
        
start = time.time()
# 初期化
dp = [i for i in range(A+1)]

dp_rdd=sc.parallelize(dp)
dp_rdd=dp_rdd.map(lambda x:(x,-1))
while(dp_rdd.count()<A+1):
    dp_rdd=dp_rdd.flatMap(table)
    
dp_rdd=dp_rdd.map(lambda x:(x[0],0)if x[0]==0 else x)
dp_rdd.sortByKey()
results=dp_rdd.collect()

# DP
for i in range(N):
    for j in reversed(range(A+1)):
        print(dp_rdd.lookup(j)[0])
        if(dp_rdd.lookup(j)[0] == -1):
            continue
        if ((a[i]+j <= A) and (dp_rdd.lookup(a[i]+j)[0] == -1)):
            dp_rdd=dp_rdd.map(lambda x:(x[0],a[i])if x[0]==a[i]+j else x)
            dp_rdd.cache()
            #dp[a[i]+j] = a[i]
           
    dp_rdd.uncache() 
    dp_rdd.cache()
    if(dp_rdd.lookup(A)[0] != -1):
        break

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print("Answer:" + str(A))
check = 0
x = A

dpresult=dp_rdd.collect()

for dp in dpresult:
    print("dp_rdd["+str(dp[0])+"]:"+str(dp[1]))

while(1):
    dpx = dp_rdd.lookup(x)[0]
    check += dpx
    print(dpx)
    x = x-dpx
    if(x <= 0):
        break
print("check="+str(check))
if check == A:
    print("OK")
