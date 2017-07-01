#find the name of the student who scored second lowest
from operator import itemgetter
l1 = list()
for _ in range(int(raw_input())):
    l2 = list()
    name = raw_input()
    l2.append(name)
    score = float(raw_input())
    l2.append(score)
    l1.append(l2)
    
l1.sort()
l1.sort(key=itemgetter(1))
max_score =  max(l1, key=lambda x: x[1])
l1.remove(max_score)
max_Score_2nd = max(l1, key=lambda x: x[1])
print max_Score_2nd
enumerate(l1)
print l1

