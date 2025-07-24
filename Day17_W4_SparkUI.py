!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!pip install -q pyspark pyngrok     

from google.colab import files
uploaded = files.upload() #Upload spark-3.5.1-bin-hadoop3.tgz

# Unzip the manually uploaded file
!tar -xzf /content/spark-3.5.1-bin-hadoop3.tgz

# Move Spark folder to /usr/local
!mv spark-3.5.1-bin-hadoop3 /usr/local/spark4


!pip install -q findspark
import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark UI Example") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()


import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/usr/local/spark4"


!npm install -g localtunnel

# Start localtunnel on port 4040
!npx localtunnel --port 4040 --subdomain bigmart-ui
!curl https://loca.lt/mytunnelpassword

from google.colab import files
uploaded = files.upload() #Upload yellow_tripdata_2021-01.csv

import pandas as pd
import io

# Load the uploaded CSV into a Spark DataFrame
df = spark.read.csv("yellow_tripdata_2021-01.csv", header=True, inferSchema=True)

# Show schema to confirm column names and types
df.printSchema()

# Task 1: Filter records and compute average fare per VendorID
filtered_df = df.filter((df["trip_distance"] > 10) & (df["fare_amount"] > 30))

# Group by VendorID and compute average fare
avg_fare_df = filtered_df.groupBy("VendorID").avg("fare_amount")

# Rename column for clarity
avg_fare_df = avg_fare_df.withColumnRenamed("avg(fare_amount)", "average_fare")

# Show the result
avg_fare_df.show()
