#!/usr/bin/env python
import sys
import datetime

samplefile = '/Users/msaha/PycharmProjects/vibes_sample.txt'
file_hand=open(samplefile, 'r')
outputfile = '/Users/msaha/PycharmProjects/vibes_parsed_output.txt'
file_out = open(outputfile, 'w')

for line in file_hand:
    try:
        head_date = ""
        persist_date = ""
        topology = ""
        lid = ""
        success_flag=""

        if line is not None and "VibesDao" in line:
            strTokens = line.split(",")
            if len(strTokens) > 1:
                dateStr = strTokens[0]

                topologyStr = strTokens[1].strip()
                topologyStrTokens = topologyStr.split(":")
                topology = topologyStrTokens[1].strip()

                lidStr = strTokens[2].strip()
                lidStrTokens = lidStr.split(":")
                lid = lidStrTokens[1].strip()

                successflagStr = strTokens[3].strip()
                successflagStrTokens = successflagStr.split(":")
                success_flag = successflagStrTokens[1].strip()

                dateStrTokens = dateStr.split("VibesDao")
                if len(dateStrTokens) < 2:
                    head_date = ""
                    persist_date = dateStrTokens[0].lstrip("[INFO] PERSIST:").strip()
                else:
                    head_date = dateStrTokens[0].rstrip("a.u.d.")
                    persist_date = dateStrTokens[1].lstrip("[INFO] PERSIST:").strip()


        output_line = head_date + "|" + persist_date + "|" + topology + "|" + lid + "|" + success_flag + "\n"

        fileout = file_out.write(output_line)

    except:
        raise;

