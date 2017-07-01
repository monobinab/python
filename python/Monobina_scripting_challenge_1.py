#!/usr/bin/python

# this script accepts an input file name and output file name from command line.
# It parses the fields and calculates average item price and outputs another data file

import sys, getopt

infile = ''
outfile = ''
try:
   myopts, args = getopt.getopt(sys.argv[1:], "i:o:")

except getopt.GetoptError as e:
    print(str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
      if o == '-i':
        infile = a
      elif o == '-o':
        outfile = a
      else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print ("Input file: %s and output file: %s" % (infile, outfile))


infile_hand = open(infile, 'r')

outfile_hand = open(outfile, 'w')

def main():
 for line in infile_hand:
    try:
        orderdateStr = ""
        order_id = ""
        order_date = ""
        user_id = ""
        item_price_1 = ""
        item_price_2 = ""
        item_price_3 = ""
        item_price_4 = ""
        avg_item_price = ""
        start_url = ""
        error_msg = ""

        if line is not None:
            fields = line.split("\t")
            orderdateStr = fields[0].strip()
            if orderdateStr is not None:
                   orderdatestrTokens = orderdateStr.split(":")
                   if len(orderdatestrTokens) < 2:
                       raise Exception("Insufficient Order information");
                   order_id = orderdatestrTokens[0]
                   order_date = orderdatestrTokens[1]
            else:
                    order_id = ""
                    order_date = ""
            user_id = fields[1].strip()
            item_price_1 = fields[2].strip()
            item_price_2 = fields[3].strip()
            item_price_3 = fields[4].strip()
            item_price_4 = fields[5].strip()

            s = float(item_price_1) + float(item_price_2) + float(item_price_3) + float(item_price_4);
            n = 1 if (item_price_1>0) else 0 + 1 if (item_price_2>0) else 0 \
                + 1 if (item_price_3>0) else 0 + 1 if (item_price_4>0) else 0;
            avg_item_price = s/n;

            start_url = fields[6].strip()

            if start_url.startswith("http://www.insacart.com"):
                error_msg = ""

            else:
                #start_url = ""
                error_msg = "Invalid URL"

            outline = str(order_id) + "|" + str(order_date) + "|" + str(user_id) + "|" + str(avg_item_price) + "|" + str(start_url) + "|" + str(error_msg) + "\n";
            outfile_hand.write(outline)

    except Exception, e:
        error_msg = str(e);
        outline = str(order_id) + "|" + str(order_date) + "|" + str(user_id) + "|" + str(avg_item_price) + "|" + str(start_url) + "|" + str(error_msg) + "\n";
        outfile_hand.write(outline)
        continue;

if __name__ == "__main__":
    main()

