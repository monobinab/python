def mutate_string(s, i, c):
	i = int(i)
	l = list(s)
	s_new = ""
	l[i] = c
	s_new = ''.join(l)
	print s_new
	return s_new

print mutate_string("abracadabra", 5, "k")
