#!/usr/bin/env python
import sys

infile = '/Users/msaha/PycharmProjects/practice/data.txt'
infile_hand = open(infile, 'r')
outfile = '/Users/msaha/PycharmProjects/practice/new_data.txt'
outfile_hand = open(outfile, 'w')

for line in fhand:
    try:
        order_id = ""
        order_date = ""
        user_id = ""
        item_price_1 = ""
        item_price_2 = ""
        item_price_3 = ""
        item_price_4 = ""
        start_url = ""
        if line is not None:
            fields = line.split(" ")
            for field in fields:
                orderdateStr = fields[0]
                user_id = fields[1]
                item_price_1 = fields[2]
                item_price_2 = fields[3]
                item_price_3 = fields[4]
                item_price_4 = fields[5]
                start_url = fields[6]
                #if start_url not startswith “http://www.insacart.com”:


        outline = orderdateStr + "|" + user_id + "|" + item_price_1 + "|" + item_price_2 + "|" + item_price_2 + "|" item_price_3 + "|" item_price_4 + "|" + start_url
        outfile_hand.write(outline)

    except:
        raise;