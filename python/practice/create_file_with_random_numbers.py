import random
file='processed_seq.txt'
randfile = open(file, "w" )
rows=10
cols=2
col1=""
col2=""

## for i in range(int(input('How many to generate?: '))):
for row in range(int(rows)):
    #for col in range(int(cols)):

            col1 = str(random.randint(1, rows))
            col2 = str(random.randint(1, 10))
            line = str(col1) + '\t' + str(col2) +"\n"
            randfile.write(line)
    #print(line)

randfile.close()