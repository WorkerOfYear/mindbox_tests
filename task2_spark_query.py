from pyspark.sql import SparkSession, DataFrame


spark = SparkSession.builder.appName("MindBox is best").getOrCreate()

products = [
    (1, "Product1"),
    (2, "Product2"),
    (3, "Product3"),
    (4, "Product4"),
]

categories = [
    (1, "Category1"),
    (2, "Category2"),
    (3, "Category3"),
]

re_category_product = [
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3),
]

product_frame = spark.createDataFrame(data=products, schema=["product_id", "product_name"])
category_frame = spark.createDataFrame(data=categories, schema=["category_id", "category_name"])
relations_frame = spark.createDataFrame(data=re_category_product, schema=["category_id", "product_id"])

result = product_frame.join(relations_frame, product_frame.product_id == relations_frame.product_id, how="left") \
    .join(category_frame, category_frame.category_id == relations_frame.category_id, how="left") \
    .select(["product_name", "category_name"])

result.show()
spark.stop()