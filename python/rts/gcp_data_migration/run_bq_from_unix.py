#!/usr/bin/python
import sys;
import subprocess;

#subprocess.call('ls -ltr', shell = True)

input_file = sys.argv[1];
input_file_handle = open(input_file, 'r');

for line in input_file_handle:
    l=line.strip()
    if(l is not None and l != ""): 	
        query="INSERT INTO rts_dataset.msm_var_sears_bu_cat_map (msm_variable,bu_Category) VALUES " + l
	cmd = "bq query --use_legacy_sql=false \""+ query +"\""
	print "executing .... >>> " + cmd + " <<<" 
	subprocess.call(cmd, shell = True)
