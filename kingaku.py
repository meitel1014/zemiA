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
form pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Bubunnwa")
sc = SparkContext(conf = conf)

rdd = sc.parallelize(kogitte)
rddKingaku = rdd.map(lambda x: (x,1)).reduceByKey(lambda x,y:x[1]+y[1])
sortedRdd = rddKingaku.sortByKey()
kingaku = rddkingaku.collect
#kingakuは二次元配列？
         
print(kingaku)