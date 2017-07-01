import json
#infile = '/staging/membermdtagsrts.csv'
infile = '/Users/msaha/PycharmProjects/data/mdtags_json_infile.csv'
infile_hand = open(infile, 'r')
#outfile = '/staging/parsed_membermdtagsrts.csv'
outfile = '/Users/msaha/PycharmProjects/data/parsed_rts_mdtags_outfile.csv'
outfile_hand = open(outfile, 'w')

for line in infile_hand:
    try:
        member_id = ""
        effective_date = ""
        expiry_date = ""
        tag_name = ""
        rts_tag = ""
        outer_json = ""
        outer_json = json.loads(line)
        member_id = outer_json['l_id']
        rts_tag = outer_json['rtsTags']
        for rts_tag in outer_json['rtsTags']:
            expiry_date = rts_tag['e']
            effective_date = rts_tag['f']
            tag_name = rts_tag['t']
            out_line = str(member_id) + "|" + str(effective_date) + "|" + str(expiry_date) + "|" + str(tag_name)
        #out_line = str(member_id) + "|" + str(rts_tag)
            outfile_hand.write(out_line)
    except:
        raise;
        #continue;



