from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import uuid 


import warnings
warnings.filterwarnings('ignore')
app_name = uuid.uuid1().hex
spark = (SparkSession.builder
.config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
.config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
.appName(app_name)
.getOrCreate()
)

output = spark.select('''select 1''').collect()

print(output)

spark.stop()