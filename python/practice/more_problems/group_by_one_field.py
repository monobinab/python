infile = '/Users/msaha/PycharmProjects/data/site_visits_by_individual.txt'
infile_handle = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/data/group_by_site.txt'
outfile_handle = open(outfile, 'w')

item=[]
i = 0

for line in infile_handle:
    item.insert(i, line.strip('\n'))
    i = i + 1
print("list of people visiting sites", item)

length = len(item)
no_of_iterations = (length - 1)
cnt = 0
url = ""

for j in no_of_iterations:
    fields = item[j].split(",")
    url = fields[1]
    if upper(url[j]) == upper(url[j+1]):
        url[j].name
