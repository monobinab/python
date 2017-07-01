l=[]
def sort_list(l):
    newList = l;
    newList.sort();
    return newList;

try:
    inp = raw_input("enter a list of words: ")
    inp = inp.split(",")
    print sort_list(inp);
    print "|".join(sort_list(inp));
    print inp;
except e1:
    raise e1;

