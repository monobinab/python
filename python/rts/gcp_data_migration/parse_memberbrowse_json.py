#!/usr/bin/python
import json

def member_browse_remove_oid(json_input_file, output_file):
	input_file_object = open(json_input_file, 'r')
	output_file_object = open(output_file, 'w')
	for line in input_file_object:
		oid = ""
		rest_of_line = ""
		json_str = json.loads(line)
		#for element in json_str:
		json_str.pop('_id', None)
		output_file_object.write(json.dumps(json_str))
		output_file_object.write('\n')	
#json.dump(json_str, output_file_object)
	close(json_input_file)
	close(output_file)
	return json_str

def member_browse_lid_parser(json_input_file, lid_output_file):
	input_file_object = open(json_input_file, 'r')
	output_file_object = open(lid_output_file, 'w')
	for line in input_file_object:
		lid = ""
		json_str = json.loads(line)
		lid = json_str["l_id"].lstrip('"').rstrip('"')
		output_file_object.write(json.dumps(lid))
		output_file_object.write('\n')
	close(json_input_file)
	close(lid_output_file)
	return lid


#member_browse_remove_oid("/Users/msaha/git/AdvancedAnalytics/GCPDataMigration/src/main/resources/memberBrowse.json", "/Users/msaha/git/AdvancedAnalytics/GCPDataMigration/src/main/resources/memberBrowseNew.json")
member_browse_lid_parser("/Users/msaha/git/AdvancedAnalytics/GCPDataMigration/src/main/resources/memberBrowse.json", "/Users/msaha/git/AdvancedAnalytics/GCPDataMigration/src/main/resources/memberBrowse_lid.json")
