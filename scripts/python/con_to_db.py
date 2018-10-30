#!/usr/bin/env python

# importing SparkContext, SparkSession and SparkConf from pyspark
# ----------------------------------------------------------------
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import Row


# COPY CSV DATA FROM S3 BUCKET INTO SPARK
# ----------------------------------------

dataFile = "s3a://nycparkingviolationdata/nycparkingViolations2014August2013June2014.csv"
sc = SparkContext("local", "data file")
sqlContext = SQLContext(sc)
data = sc.textFile(dataFile)  # .count()
lines = data.take(10)


##### THIS IS DEMO DATA BELOW #########

# READ FROM DATA IN DATABASE
# ---------------------------

source_df = sqlContext.read.format('jdbc').options(
    url="jdbc:mysql://masterdb.ch0ib4epgaak.us-west-2.rds.amazonaws.com:3306/demo",
    driver="com.mysql.cj.jdbc.Driver",
    dbtable="demotable",
    user="chrisj",
    password="").load()
source_df.show()


# WRITE CSV DATA TO DATABASE
#----------------------------

df = sqlContext.read.csv('/home/ubuntu/demodata.csv', header='True', inferSchema='True')

# df.dtypes
# df.show()

df.write.format('jdbc').options(
    url="jdbc:mysql://masterdb.ch0ib4epgaak.us-west-2.rds.amazonaws.com:3306/demo",
    driver="com.mysql.cj.jdbc.Driver",
    dbtable="demotable",
    user="chrisj",
    password="myparkingdata").mode('append').save()
