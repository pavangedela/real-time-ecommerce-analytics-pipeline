from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HiveAnalysis") \
    .enableHiveSupport() \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.parquet("data/processed_orders")

df.createOrReplaceTempView("orders")

print("Top Products")
spark.sql("""
SELECT product,
SUM(revenue) as total_revenue
FROM orders
GROUP BY product
ORDER BY total_revenue DESC
""").show()

print("Category Sales")
spark.sql("""
SELECT category,
SUM(revenue) as total_revenue
FROM orders
GROUP BY category
ORDER BY total_revenue DESC
""").show()

print("Top Customers")
spark.sql("""
SELECT customer_id,
SUM(revenue) as spending
FROM orders
GROUP BY customer_id
ORDER BY spending DESC
LIMIT 10
""").show()

spark.stop()