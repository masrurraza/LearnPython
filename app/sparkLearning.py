from pyspark.sql import SparkSession


def main():
    # Initialize a SparkSession
    print("Creating SparkSession")
    spark = SparkSession.builder.appName("sparkLearning").config("spark.ui.reverseProxyUrl", "http://localhost:4040").getOrCreate()
    print("SparkSession created successfully")

    # Read a CSV file into a DataFrame
    df = (spark.read.format('csv').option('header', 'true').option('inferSchema', 'true')
          .load(r'C:\Users\Masrur Raza\Desktop\Exam Prep\sample-csv-files\files\customers\customers-100.csv'))

    # Show the DataFrame
    df.show(df.count())


if __name__ == '__main__':
    main()

