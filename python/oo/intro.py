movies = list()
movie1 = dict()
movie1['Director']='James'
movie1['Title'] = 'Avatar'
movie1['Release Date'] = '18 December 2009'
movie1['Running Time'] = '162 minutes'
movie1['Rating'] = 'PG-13'

movies.append(movie1)
movie2=dict()
movie2['Director']='Fox'
movie2['Title'] = 'Star Wars'
movie2['Release Date'] = '20 December 2009'
movie2['Running Time'] = '202 minutes'
movie2['Rating'] = 'PG-13'

movies.append(movie2)
print movies
print movie1
print movie2

keys = ['Title', 'Director', 'Rating', 'Release Date', 'Running Time']
for item in movies:
    print '-----'
    for key in keys:
        print key,': ',item[key]
print '------'
