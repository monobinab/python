infile = '/Users/msaha/PycharmProjects/data/counts_of_site_visits.txt'
infile_handle = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/data/sorted_counts_of_site_visits.txt'
outfile_handle = open(outfile, 'w')

url_visit_list = []
i=0
temp=0

for line in infile_handle:
    if line is not None:
        try:
          url_visit_list.insert(i, line.strip('\n'))
          i = i + 1

        except:
            raise

print("url visits are", url_visit_list)
print(url_visit_list[1])

length_of_list = len(url_visit_list)
no_of_iterations = (length_of_list -1 )


for i in range(no_of_iterations):
    for j in range(no_of_iterations - i ):
            field1 = url_visit_list[j].split(",") #first line
            field2 = url_visit_list[j+1].split(",") #2nd line
            cnt1 = int(field1[1].strip())
            cnt2 = int(field2[1].strip())
            if cnt1 > cnt2:
                try:
                    temp = url_visit_list[j]
                    url_visit_list[j] = url_visit_list[j+1]
                    url_visit_list[j+1] = temp
                except:
                    raise

print("sorted list is", url_visit_list)

