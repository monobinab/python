def isOdd():
        n = int(raw_input())
        if ((n%2 == 0 and n >= 2 and n <= 5) or (n%2 == 0 and n > 20)):
                print "Not Weird"
	elif ((n%2 == 1) or (n%2 == 0 and n >= 6 and n <= 20)):
		print "Weird"
	else:
		print "Not Applicable"

mytest = isOdd()
