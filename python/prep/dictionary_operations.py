#look up element
#store and retrieve
#merge two into one
#dictionary within a dictionary (value is another dictionary adn how to add key, value and how to retrive from complex structure)

d = {}
d[1] = "auri"
d[2] = "reesh"
d[3] = "mono"
print(d)

print(d.get(2))
print(2 in d)
print(2 not in d)
#print(d.has_key(2) ) #this gives an error
print(d.items())

d_entry = d.iteritems()
for n, m in d_entry:
    m = m+"s"
print(d)