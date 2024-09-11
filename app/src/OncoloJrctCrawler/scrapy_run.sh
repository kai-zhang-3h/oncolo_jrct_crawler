cd src/OncoloJrctCrawler

LOGFILE="public/bash.log"
exec 3>&1 1>"$LOGFILE" 2>&1

t1=$(date +%s)

rm public/data.json
touch public/data.json

rm public/jrctList.txt
touch public/jrctList.txt

scrapy crawl oncolojrctid

t2=$(date +%s)

scrapy crawl oncolojrct

t3=$(date +%s)

python scripts/to_csv.py
python scripts/to_mysql.py

t4=$(date +%s)

jrct_id_crawl_time=t2-t1
jrct_crawl_time=t3-t2
data_output_time=t4-t3
total_time=t4-t1

# h=$(($(($time)) / 3600)) m=$((($(($time)) % 3600) / 60)) s=$(($(($time)) % 60))

# echo "Elapsed Time: $h hours $m minutes $s seconds"

seconds2human() {
    sec="$1"
    task="$2"
    h=$((sec / 3600)) m=$(((sec % 3600) / 60)) s=$((sec % 60))
    printf "Elapsed Time of $task: %2dh %02dm %02ds\n" $h $m $s
}

seconds2human $(($jrct_id_crawl_time)) "jrct_id_crawl"
seconds2human $(($jrct_crawl_time)) "jrct_crawl"
seconds2human $(($data_output_time)) "data_output"
seconds2human $(($total_time)) "total"

