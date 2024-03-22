# Description: This file contains the functions to create the customers table.
import pySpark.common.SparkSession as SparkSession


def startSparkSession():
    spark = SparkSession.getSparkSession("Customers")
    return spark

def createCustomersTable(spark):
    # Create a DataFrame
    data =