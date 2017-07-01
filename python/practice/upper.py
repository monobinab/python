filein = '/Users/msaha/PycharmProjects/practice/test.txt'
fhand = open(filein,'r')
fileout = '/Users/msaha/PycharmProjects/practice/out_test.txt'
fwrite = open(fileout, 'w')


for line in fhand:
 try:
    if line is not None:
      newline = line.upper();
      print newline;
      fwrite.write(newline);
 except:
    raise
