sql_file="/Users/msaha/PycharmProjects/rts/bqmemberinfo.txt"
sql_file_handle==$(cat $sql_file);
IFS=';' read -a sqls <<< "$sql_file_handle"
echo "FirstQuery: ${sqls[0]}"
#for sql in $sql_file_handle
#do
#	echo "> [$sql]"
#done
