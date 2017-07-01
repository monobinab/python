s = 'cAt'
l = list(s)
l_new = []
s_new = ""
i_new = ""
print l
for i in l:
	print type(i)
	if i.islower() ==True:
		print ("Original", i)
		i_new = i.upper()
		l_new.append(i_new)
		print ("ToUpper", i_new)
	else:
		print ("Original", i)
		i_new = i.lower()
		l_new.append(i_new)
		print ("ToLower", i_new)
s_new = str(l_new)
print s_new


