#/usr/bin/python
import json
import os
os.system('gsutil cp gs://dev-ashish/divLnItm.jsn /Users/msaha/PycharmProjects/data/')
input_file = "/Users/msaha/PycharmProjects/data/divLnItm.jsn"
input_file_handle = open(input_file, 'r')
output_file = "/Users/msaha/PycharmProjects/data/divLnItm_parsed.txt"
output_file_handle = open(output_file, 'w')

d = ""
v = ""

for line in input_file_handle:
        #print(line)
        if  "NumberInt" in line:
		ln = line.replace("NumberInt(", "")
		ln = ln.replace(")", "")
		print(ln)
	else:
		try:
			ln = line
			json_str = json.loads(line)
			json_str.pop("_id")
			print(json_str)
			output_file_handle.write(json.dumps(json_str))
			output_file_handle.write('\n')
		except:
			continue;
input_file_handle.close()
output_file_handle.close()

os.system('gsutil cp /Users/msaha/PycharmProjects/data/divLnItm_parsed.txt  gs://dev-msaha/')

