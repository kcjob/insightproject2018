#!/usr/bin/env python

# importing SparkContext, SparkSession and SparkConf from pyspark
# ----------------------------------------------------------------
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.window import Window as W

# COPY CSV DATA FROM S3 BUCKET INTO SPARK
# ----------------------------------------

dataFile = "s3a://nycparkingviolationdata/nycparkingViolations2014August2013June2014.csv"
sc = SparkContext("local", "data file")
sqlContext = SQLContext(sc)
data_frame = sqlContext.read.csv(dataFile, header='True', inferSchema='True')
data_frame2 = data_frame.withColumn("index", F.monotonically_increasing_id())
windowSpec = W.orderBy("index")
data_frame2 = data_frame2.withColumn("index", F.row_number().over(windowSpec))
#lines = data_frame2.take(20)

df2 = data_frame2.select(["index", 'Summons Number', 'Violation Code', 'Violation Location', 'Violation Precinct', 'Violation County',
                          'Violation Description', 'No Standing or Stopping Violation', 'Hydrant Violation', 'Double Parking Violation'])

print df2

df2.show(n=3)

# Copy processed data to database
#--------------------------------

df2.write.format('jdbc').options(
    url="jdbc:mysql://masterdb.ch0ib4epgaak.us-west-2.rds.amazonaws.com:3306/nycparkingdata",
    driver="com.mysql.cj.jdbc.Driver",
    dbtable="",
    user="",
    password="").mode('append').save()
