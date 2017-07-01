def count_substring(string, substring):
	substring = list(substring)
	l1 = []
	cnt = 0
	for i in range(len(string)):
		for j in range(len(substring)):
			if i == j:
				print i
				l1.append(j)
				j+1
				i+1
			else:
				j+1
		
		if len(l1) == len(substring):
			cnt+1
		else:
			cnt
	
	return cnt

print count_substring("abcde", "abc")
