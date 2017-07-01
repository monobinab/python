#RDDs into Relations (Python)

#load a text file and convert each line to a dictionary.
lines = sc.textFile("../../../people.txt")

parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p:{"name": p[0], "age": int(p[1])})

#infer the schema, and register the schema RDD as a table
peopleTable = sqlCtx.inferSchema(people)
peopleTable.registerAsTable("people")

#####################################################################

##RDDs into Relations (Scala)
val sqlContext = new org.apache.spark.sql.SQLContext(sc)
import sqlContext._

// Define the schema using a case class.
case class Person(name: String, age: Int)

// Create an RDD of Person objects and register it as a table.
val people
    sc.textFile("examples/src/main/resources/people.txt")
    .map(_.split(","))
    .map(p => Person(p(0), p(1).trim.toInt))
people=registerAsTable("people")

######################################################################

#after the data gets in now we want to query them
registerFunction("countmatches",
    lambda (pattern, text) :   #lambda function done in python and scala. read about it.
        re.subn(pattern, '', text)[1])

sql("select countMatches('a', text)...")

#####################################################################

# SQL and Machine Learning

training_data_table = sql("""
   select e.action, u.age, u.latitude, u.longitude
   from Users u
   Join Event e on u.userId = e.userid """
)

def featurize(u):
    LabeledPoint(u.action, [u.age, u.latitude, u.longitude])

    // SQL results are RDDs so can be used directly in MLLib.

