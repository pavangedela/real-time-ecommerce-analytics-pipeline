from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .load()

schema = StructType([
    StructField("order_id", IntegerType()),
    StructField("customer_id", IntegerType()),
    StructField("product", StringType()),
    StructField("category", StringType()),
    StructField("quantity", IntegerType()),
    StructField("price", IntegerType()),
    StructField("timestamp", StringType())
])

orders = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

orders = orders.withColumn(
    "revenue",
    col("quantity") * col("price")
)

query = orders.writeStream \
    .format("parquet") \
    .option("path", "data/processed_orders") \
    .option("checkpointLocation", "data/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()