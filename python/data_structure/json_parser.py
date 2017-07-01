import json
infile='simple_json_input_file.txt'
infile_hand = open(infile,'r')
outfile = 'parsed_json_outfile.txt'
outfile_hand = open(outfile, 'w')

for line in infile_hand:
    modelId = ""
    modelName = ""
    format = ""
    category = ""
    tag = ""
    score = ""
    percentile =""
    rank = ""
    scores_info =  json.loads(line)
    print scores_info

    modelId = scores_info['modelId']
    modelName = scores_info['modelName']
    format = scores_info['format']
    category = scores_info['category']
    tag = scores_info['tag']
    score = scores_info['score']
    percentile = scores_info['percentile']
    rank = scores_info['rank']

    output_line = str(modelId) + "|" + str(modelName) + "|" + str(format) + "|" + str(category) + "|" + str(tag) + "|" + str(score) + "|" + str(percentile) + "|" + str(rank) + "\n"

    print output_line

    outfile_hand.write(output_line)