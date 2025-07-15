from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, rank, row_number, dense_rank
from pyspark.sql.window import Window

print("🚀 Starting PySpark Session...")
# Start Spark Session
spark = SparkSession.builder.appName("PySpark Joins & Windows").getOrCreate()

print("📥 Loading datasets from CSV files...")
# Load datasets
customers = spark.read.option("header", "true").csv("/app/customer.csv", inferSchema=True)
transactions = spark.read.option("header", "true").csv("/app/transactions.csv", inferSchema=True)

print("\n✅ CUSTOMER DATA:")
customers.show()

print("\n✅ TRANSACTION DATA:")
transactions.show()

print("\n🔗 Performing INNER JOIN on 'customer_id'...")
# Join on customer_id
joined = transactions.join(customers, on="customer_id", how="inner")
print("\n✅ JOINED DATA:")
joined.show()

print("\n🧮 Calculating LATEST TRANSACTION per customer...")
# Window 1: Get latest transaction per customer
window_latest = Window.partitionBy("customer_id").orderBy(col("date").desc())
latest_txn = joined.withColumn("row_num", row_number().over(window_latest)).filter("row_num = 1")
print("\n✅ LATEST TRANSACTION PER CUSTOMER:")
latest_txn.show()

print("\n📊 Ranking PRODUCTS BY REVENUE in each CATEGORY...")
# Window 2: Rank products by revenue in each category
window_revenue = Window.partitionBy("category").orderBy(col("amount").desc())
ranked = joined.withColumn("rank", rank().over(window_revenue)) \
               .withColumn("dense_rank", dense_rank().over(window_revenue))
print("\n✅ RANKED PRODUCTS BY REVENUE PER CATEGORY:")
ranked.select("product", "category", "amount", "rank", "dense_rank").show()



print("\n📌 Registering 'joined' DataFrame as a temporary SQL view...")
joined.createOrReplaceTempView("joined_table")

print("\n🧠 Running SQL query to rank products by revenue in each category...")
sql_result = spark.sql("""
    SELECT 
        product,
        category,
        amount,
        RANK() OVER (PARTITION BY category ORDER BY amount DESC) AS sql_rank,
        DENSE_RANK() OVER (PARTITION BY category ORDER BY amount DESC) AS sql_dense_rank
    FROM joined_table
""")

print("\n✅ SQL RANK OUTPUT:")
sql_result.show()



print("\n✅ Done. Stopping Spark Session.")
spark.stop()
