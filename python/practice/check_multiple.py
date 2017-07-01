def divisibleby7(x):
    if x % 7 == 0:
        return True


def multipleof5(y):
    if y % 5 != 0:
        return True


try:
    for i in range(2000, 3000):
        if not (not divisibleby7(i) or not multipleof5(i)):
            l.append(str(i))
    print ",".join(l)
except:
    print "Error"
    quit()
