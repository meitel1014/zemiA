from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("DynamicPlanning")
sc = SparkContext(conf = conf)

