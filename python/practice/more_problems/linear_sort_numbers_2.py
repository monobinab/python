infile = '/Users/msaha/PycharmProjects/data/number_lines.txt'
infile_hand = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/data/sorted_number_lines.txt'
outfile_hand = open(outfile, 'w')

print("name of file: ", infile_hand.name)

item=[]
i=0

for line in infile_hand:
    if line is not None:
        #print(line)
        item.insert(i, int(line.strip('\n')))
        i=i+1

print("items in the file are: ", item)
length=len(item)
number_of_iterations=(length - 1)

for j in range(number_of_iterations):
   for k in range(number_of_iterations-j):
       if item[k] > item[k+1]:
           temp = item[k]
           item[k] = item[k+1]
           item[k+1] = temp

print("sorted items in the file are: ", item)

print(item[length-1])
print(item[length-2])


