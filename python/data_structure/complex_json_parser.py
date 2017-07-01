import json

infile='sample_json_file.txt'
infile_hand = open(infile,'r')
outfile = 'parsed_json_sample_outfile.txt'
outfile_hand = open(outfile, 'w')

def parse_json(your_json):
    to_dict = json.loads(your_json)
    for item in to_dict['scoresInfo']:
        print (item['modelId'], scoresInfo['modelName'], scoresInfo['format'])

for line in infile_hand:
    try:
        outer_json = ""
        status = ""
        statusCode = ""
        memberId = ""
        lastUpdated = ""
        scoresInfo = ""
        modelId = ""
        modelName = ""
        format = ""
        category = ""
        tag = ""
        score = ""
        percentile =""
        rank = ""
        outer_json =  json.loads(line)
        #print outer_json

        status = outer_json['status']
        statusCode = outer_json['statusCode']
        memberId = outer_json['memberId']
        lastUpdated = outer_json['lastUpdated']
        scoresInfo = outer_json['scoresInfo']

        for scoresInfo in outer_json['scoresInfo']:
             modelId= scoresInfo['modelId']
             modelName = scoresInfo['modelName']
             format = scoresInfo['format']
             category = scoresInfo['category']
             tag = scoresInfo['tag']
             score = scoresInfo['score']
             percentile = scoresInfo['percentile']
             rank = scoresInfo['rank']



             output_line = str(status) + "|" + str(statusCode) + "|" + str(memberId) + "|" + str(lastUpdated) + "|" + str(modelId) + "|" + str(modelName) + "|" + str(format) + "|" + str(category) + "|" + str(tag) + "|" + str(score) + "|" + str(percentile) + "|" + str(rank) + "\n"

             print output_line
             outfile_hand.write(output_line)
    except:
        continue;

print type(scoresInfo)
print type(outer_json)
print dir(scoresInfo)


