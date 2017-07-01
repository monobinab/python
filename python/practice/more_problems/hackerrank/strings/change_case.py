def swap_case(s):
	print s
	l = list(s)	
	print l
	l_new = []
	s_new = ""
	i_new = ""
	for i in l:
		if i.islower() == True:
			i_new = i.upper()
			l_new.append(i_new)
		else:
			i_new = i.lower()
			l_new.append(i_new)
	
	s_new = ''.join(l_new)
	return s_new

print swap_case('HackerRank.com presents')


		
