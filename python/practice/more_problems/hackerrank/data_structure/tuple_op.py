if __name__ == '__main__':
	n = int(raw_input())
	integer_list = map(int, raw_input().split())
	print(n)
	print(integer_list)
	t = tuple(integer_list)
	print t
	print(hash(t))

