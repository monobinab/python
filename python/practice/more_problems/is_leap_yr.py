def is_leap(year):
    leap = False
    
    if((year%4 == 0) or ((year%100 == 0) and year%400 == 0)):
	leap = True
	print (leap)
    else:
	print(leap)
    
    return leap

is_leap(1990)
