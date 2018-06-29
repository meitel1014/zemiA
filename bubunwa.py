# -*- coding: utf-8 -*-

#N=100000,MAX=100000まで5分以内に終了
N = 100000 #小切手の枚数
MAX = 100000 #金額の上限（最終的には100万）

#小切手の準備
import random
kogitte = []
for i in range(N):
   kogitte = kogitte + [random.randint(1,MAX)]

#目標金額の決定
import copy
X = 0 #目標金額
kotae = [] #答え（確認用、最終的に不要、一致するとは限らない）
NUM = random.randint(1,N)
cpy = copy.deepcopy(kogitte)
for i in range(NUM):
    j = random.randint(0,N-i-1)
    X = X + cpy[j]
    kotae = kotae + [cpy.pop(j)]
    
#ここまで準備（kogitte,X以外の上記の変数を以下で使用してはいけない）


#各金額の小切手が何枚あるかをリストに（n円の枚数はn-1番目の要素に入る）
kogitte.sort()
kingaku = []

#print(kogitte)
#print(kotae)
print("goal",X)

num = len(kogitte)

#ここをRDDにする
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Bubunnwa")
sc = SparkContext(conf = conf)

rdd = sc.parallelize(kogitte)
rddKingaku = rdd.map(lambda x: (x,1)).reduceByKey(lambda x,y:x[1]+y[1])
sortedRdd = rddKingaku.sortByKey()
kingakuPair = rddKingaku.collect()
#kingakuは二次元配列？
i = 0
for key,value in kingakuPair.items():
    kingaku[i] = key
    i = i + 1     
print(kingaku)

#目標金額となる組み合わせを求める
S = 0 #現在の合計金額
kaitou = [] #選んだ小切手のリスト（各金額の小切手を何枚選んだかを表す、n円の枚数はn-1番目の要素に入る）
for i in range(MAX):
    kaitou = kaitou + [0]
    
#1週目
for i in range(MAX):
    while (S < X) and (kaitou[MAX-1-i] < kingaku[MAX-1-i]):
        kaitou[MAX-1-i] = kaitou[MAX-1-i] + 1
        S = S + MAX-i
    if S > X:
        S = S - (MAX-i)
        kaitou[MAX-1-i] = kaitou[MAX-1-i] - 1 

#2週目以降          
while S != X:
    for i in range(MAX):
        if kaitou[MAX-1-i] > 0:
            min = MAX -1 - i
    kaitou[min] = kaitou[min] - 1
    S = S - (min+1)
    for i in range(min):
        while(S < X) and (kaitou[min-1-i] < kingaku[min-1-i]):
            kaitou[min-1-i] = kaitou[min-1-i] + 1
            S = S + min-i
        if S > X:
            S = S - (min-i)
            kaitou[min-1-i] = kaitou[min-1-i] - 1 
#確認用
SUM = 0
OUTPUT = []
for i in range(MAX):
    SUM = SUM + kaitou[i]*(i+1)
    while kaitou[i] > 0:
        OUTPUT = OUTPUT + [i+1]
        kaitou[i] = kaitou[i] - 1
print(SUM)
#print(OUTPUT)
    