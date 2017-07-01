#if you input 4 then it will print 123

def printInt():
	n = int(raw_input())
	s = str(1)
	for i in range(n-1):
		s = s + str(i+2)
	print (s)

printInt()
