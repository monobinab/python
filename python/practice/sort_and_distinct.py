inp = raw_input("enter list of space separated words ")
inp1 = inp.split(" ")
inp2 = set(inp1)
l = sorted(list(inp2))
print ",".join(l)
