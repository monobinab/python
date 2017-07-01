infile = '/Users/msaha/PycharmProjects/data/counts_of_site_visits.txt'
infile_handle = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/data/sorted_counts_of_site_visits.txt'
outfile_handle = open(outfile, 'w')

url_visit_dict = {}
i=0
temp=0

for line in infile_handle:
    if line is not None:
        try:
            url = ""
            visit = ""
            (url, visit) = line.split(",")
            visitCnt = int(visit.strip('\n'))
            url_visit_dict[str(url)] = visitCnt
            print("URL visits are" , url_visit_dict)
        except:
            raise

url_visit_dict['TEST'] = 123;
print( url_visit_dict.get('TEST') )
print(url_visit_dict['TEST'])

length_of_dict = len(url_visit_dict)
no_of_iterations = (length_of_dict - 1)

#for i in range(no_of_iterations):
#    for j in range(no_of_iterations - i ):
#        if visit[j] > visit[j+1]:
            #url_visit_dict[] = temp
