#!/usr/bin/env python
# this script parses the input file and calculates average item price
import sys

infile = '/Users/msaha/PycharmProjects/data.txt'
infile_hand = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/1_new.txt'
outfile_hand = open(outfile, 'w')

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
        l=list()
        if line is not None:
            fields = line.split("\t")
            #for field in fields:
            orderdateStr = fields[0].strip()
            if orderdateStr is not None:
                   orderdatestrTokens = orderdateStr.split(":")
                   order_id = orderdatestrTokens[0]
                   order_date = orderdatestrTokens[1]
            user_id = fields[1].strip()
            item_price_1 = fields[2].strip()
            item_price_2 = fields[3].strip()
            item_price_3 = fields[4].strip()
            item_price_4 = fields[5].strip()
            item_price_list = l.append(str(item_price_1)+ str(item_price_2)+str(item_price_3)+ str(item_price_4))

            outfile_hand.write(item_price_list)
    except:
        continue;