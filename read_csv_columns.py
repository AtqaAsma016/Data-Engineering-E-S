from pyspark.sql import SparkSession
import time
def main():
    spark = SparkSession.builder \
        .appName("ReadCSVandShowColumns") \
        .getOrCreate()

    hdfs_path = "hdfs://namenode:8020/data/input/yellow_tripdata_2021-01.csv"

    df = spark.read.option("header", "true").csv(hdfs_path)

    print("📌 Column Names:")
    for col in df.columns:
        print(col)

    time.sleep(1000)
    spark.stop()

if __name__ == "__main__":
    main()

