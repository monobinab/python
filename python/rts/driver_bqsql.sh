#!/bin/bash

# Remove all the temporary files
# ------------------------------
rm -f "outfile*"

# Split the query file based on the delimiter ";"
# -----------------------------------------------
csplit --digits=2  --quiet --prefix=outfile $1 "/;/+1" "{*}"
if [ $? -ne 0]
      then
          echo "-----ERROR--------"
          exit
fi

# Calculate the number of SQL queries in the file
# -----------------------------------------------
count=`ls ./outfile*|wc -l`
if [ $? -ne 0]
      then
          echo "-----ERROR--------"
          exit
fi


a=00
count=`expr $count - 1`
echo " Number of files = $count"

# Loop over all the file segments and run the SQL statements
# ----------------------------------------------------------
while [ "$a" -lt $count ]
do

   if [ -e outfile$a ]
   then
      echo " ---------- line $a ------------"
      cat "outfile$a"

      # Run the SQL statement
      # ---------------------
      bq query --use_legacy_sql=false `cat outfile$a`

      if [ $? -ne 0]
      then
          echo "-----ERROR--------"
          exit
      else
          echo "-----------SUCCESS $a --------------------"
      fi
   fi

a=`expr $a + 1`
printf -v a "%02d" $a 

done

exit



