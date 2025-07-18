# Install PySpark
!pip install pyspark

# Import necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, rand, when
import time

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Optimization") \
    .getOrCreate()

from google.colab import files
uploaded = files.upload()


file_path = "/content/BigMart Sales.csv" 
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show sample data
df.show(3)
df.printSchema()



# Simulate large dataset by unioning the same data multiple times
large_df = df
for _ in range(9):
    large_df = large_df.union(df)

print("Original row count:", df.count())
print("After replication (10x) row count:", large_df.count())



# Add synthetic join column for testing joins
large_df = large_df.withColumn("Department", when(rand() < 0.5, "Sales").otherwise("Marketing"))

# Create lookup DataFrame for join
lookup_data = [("Sales", "D001"), ("Marketing", "D002")]
lookup_df = spark.createDataFrame(lookup_data, ["Department", "Dept_ID"])

large_df.select("Department").distinct().show()
lookup_df.show()

start = time.time()
joined_shuffle = large_df.join(lookup_df, on="Department", how="left")
joined_shuffle.count()
print("Default Shuffle Join Time:", time.time() - start)



start = time.time()
joined_broadcast = large_df.join(broadcast(lookup_df), on="Department", how="left")
joined_broadcast.count()
print(" Broadcast Join Time:", time.time() - start)

# Cache and trigger action
joined_broadcast.cache()
joined_broadcast.count()

# Confirm it's cached
print("Is cached:", joined_broadcast.is_cached)


repartitioned_df = joined_broadcast.repartition(8)
repartitioned_df.write.mode("overwrite").parquet("/tmp/repartitioned_output")
print("Repartitioned and written to /tmp/repartitioned_output")


coalesced_df = joined_broadcast.coalesce(1)
coalesced_df.write.mode("overwrite").parquet("/tmp/coalesced_output")
print("Coalesced and written to /tmp/coalesced_output")


joined_broadcast.explain(True)
