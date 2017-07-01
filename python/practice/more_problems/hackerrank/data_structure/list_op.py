def listOp():
    if __name__ == '__main__':
    	N = int(raw_input()) # input 12 from prompt
    	l = list()
    	l.append(N)
    	l.extend([6])
    	l.extend([5])
    	l.insert(3,10)
    	l.remove(12)
    	print (l)
    	l.remove(6)
    	l.append(1)
    	l.append(9)
    	l.sort()
    
    	print(l)
    	l.pop(-1)
    	l.reverse()
    	print(l)
listOp()
