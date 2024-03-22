from pyspark.sql import SparkSession


# Create Spark Session
def _createSparkSession(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


# get spark session
def getSparkSession(appName):
    return _createSparkSession(appName)