#!/usr/bin/python
import sys;
import subprocess;

subprocess.call('ls -ltr', shell = True)
subprocess.call('bq ls', shell = True)
subprocess.call('bq query --use_legacy_sql=false  "select * from rts_dataset.msm_var_category"', shell = True) 
subprocess.call("""bq query --use_legacy_sql=false \"INSERT INTO rts_dataset.msm_var_category (msm_variable,bu_category) VALUES ('NUM_S_MAT_H_BIG_T_SLS_01M', 'Mattress_home_big_Tckt')\"""", shell = True)
