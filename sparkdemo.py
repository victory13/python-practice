from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
        .master("local") \
        .appName("spark demo") \
        .getOrCreate()

#print(spark.sparkContext.textFile("C://Users/Nikita/Desktop/cca/deckofcards.txt").first())
linesList = ["this is an apple",
"this is not an apple",
"this is a green apple",
"this is a not green apple"]

lines = spark.sparkContext.parallelize(linesList)

line_filter = lines.filter(lambda x: ('not' not in x)).map(lambda sp: len(sp.split(" ")))
line_filter.collect()
#[4, 5]
