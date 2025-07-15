from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum as _sum, round

# Step 1: Start Spark session
spark = SparkSession.builder \
    .appName("Sales CSV to MySQL") \
    .getOrCreate()

# Step 2: (TASK 1) Load dataset from CSV
csv_path = "/app/sales_data.csv" 
df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_path)

# Step 3: (TASK 2)Clean nulls and standardize column names
df = df.dropna()
df = df.toDF(*[c.strip().lower().replace(" ", "_") for c in df.columns])

# Step 4: (TASK 3) Calculate average sales by region
avg_sales_region = df.groupBy("region").agg(round(avg("sales"), 2).alias("avg_sales"))

# Step 5: (TASK 4) Calculate category revenue share
category_totals = df.groupBy("category").agg(_sum("sales").alias("category_total"))
df_with_totals = df.join(category_totals, on="category")
df_with_share = df_with_totals.withColumn("category_share", round(col("sales") / col("category_total"), 4))

# Step 6: MySQL connection settings
mysql_url = "jdbc:mysql://mysql:3306/myappdb"
mysql_properties = {
    "user": "myuser",
    "password": "mypassword",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Step 7: Write outputs to MySQL
avg_sales_region.write.jdbc(
    url=mysql_url,
    table="avg_sales_by_region",
    mode="overwrite",
    properties=mysql_properties
)

df_with_share.select("product", "category", "sales", "category_share").write.jdbc(
    url=mysql_url,
    table="category_revenue_share",
    mode="overwrite",
    properties=mysql_properties
)

spark.stop()
