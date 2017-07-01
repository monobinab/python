#!/usr/bin/python
# this script accepts an input file and parses the fields and calculates average item price and outputs another data file
import sys


infile = '/Users/msaha/PycharmProjects/data.txt'
infile_hand = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/new_data.txt'
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
            start_url = fields[6].strip()
            if start_url.startswith("http://www.insacart.com"):
                error_msg = ""

            else:
                start_url = ""
                error_msg = "Invalid URL"


            outline = str(order_id) + "|" + str(order_date) + "|" + str(user_id) + "|" + str(item_price_1) + "|" + str(item_price_2) + "|" + str(item_price_2) + "|" + str(item_price_4) + "|" + str(start_url) + "|" + str(error_msg) + "\n"
            outfile_hand.write(outline)

    except:
        continue;

if __name__ == "__main__":
    main()

