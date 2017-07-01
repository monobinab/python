'''
Python Programming Assessment

Produce a python module (ayasdi_python_code.py) which does the following:

Create a tab-delimited file (ayasdi_assignment.csv) containing 20 columns and a million rows

with the following characteristics:

1. Column 1 (labeled as col1 is the index column where the values are 1 to 1 million)

2. The next 9 columns (2 to 10) are labelled col2_x ... col10_x where each contains

random values and 'x' is the mean mentioned in the next sentence. Each column has

random data generated from a gaussian distribution at different means and variances.

Additionally, each of these columns have 10% nulls.

3. Columns 11 to 19 are labelled as col11...col19, where each column has random strings

selected from the English Dictionary. 10% nulls in this column as well.

4. Column 20 has random dates selected between January 1, 2014 to December 31, 2014.

No nulls in this column.

Once this dataset has been created, load it into a single table in a sqlite database

(ayasdi_assignment.db).

Guidelines:

 The code should follow PEP 8 guidelines (https://www.python.org/dev/peps/pep-0008/)

 Stick to core-python packages in the code (no pandas, numpy, etc.)

 Write object-oriented code

 Include doctests in your code.

 A pylint score (http://www.pylint.org/) greater than 80%
'''


import random
file='processed_seq.txt'
randfile = open(file, "w" )

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(1, 100)) + "\n"
    randfile.write(line)
    print(line)

randfile.close()


