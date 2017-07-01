try:
    inp = [x for x in raw_input().split(",")]
    inp = inp.sort()
    print ",".join(inp)
except:
    print "error"
    quit()
