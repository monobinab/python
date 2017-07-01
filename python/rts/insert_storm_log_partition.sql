SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

use real_time_scoring;
ALTER TABLE api_storm_log DROP IF EXISTS PARTITION(year = '${hiveconf:current_year}', month = '{hiveconf:current_month}', day = '{hiveconf:current_day}');
ALTER TABLE api_storm_log DROP IF EXISTS PARTITION(year = '${hiveconf:current_year}', month = '{hiveconf:current_month}', day = '{hiveconf:yesterday}');

insert into table api_storm_log
PARTITION(Year, Month, Day)

select
trim(head_date) as head_date,
trim(tail_date) as tail_date,
--trim(lid) as encrypted_lyl_id_no,
--trim(modelId),
--trim(oldScore),
--trim(newScore),
--trim(minExpiry),
--trim(maxExpiry),
--trim(source),
unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy") as epoch,
from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy")) as timestamp,
to_date(from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy"))) as date,
year(from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy"))) as year,
month(from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy"))) as month,
day(from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy"))) as day
from real_time_scoring.rts_storm_log_staging
where length(to_date(from_unixtime(unix_timestamp(tail_date, "EEE MMM dd HH:mm:ss z yyyy"))))=10
limit 100;


select
tail_date,
unix_timestamp('Wed Dec 31 17:43:44 EST 2014', "EEE MMM dd HH:mm:ss z yyyy")
from 
real_time_scoring.rts_storm_log_staging
where tail_date like '%Wed Dec 31 17:43:44 EST 2014%'
;