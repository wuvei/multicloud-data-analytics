#!/usr/bin/env bash
set -exo pipefail

[ -d "/home/ec2-user/tpch-spark" ] && rm -rf /home/ec2-user/tpch-spark
cd /home/ec2-user/ && git clone https://github.com/SimonZYC/tpch-spark.git
cd /home/ec2-user/tpch-spark/dbgen
make

cd /home/ec2-user/tpch-spark && sbt package

[ -d "/home/ec2-user/metrics" ] && rm -rf /home/ec2-user/metrics
mkdir -p /home/ec2-user/metrics

[ -d "/home/ec2-user/logs" ] && rm -rf /home/ec2-user/logs
mkdir -p /home/ec2-user/logs

## declare an array variable
declare -a arr=(10 50 100 150)

## now loop through the above array
for i in "${arr[@]}"
do
   /home/ec2-user/spark/bin/spark-submit \
    --master spark://$(cat /home/ec2-user/hadoop/conf/masters):7077 \
    --conf spark.driver.cores=3 \
    --conf spark.driver.memory=10g \
    --conf spark.executor.memory=4g \
    --packages ch.cern.sparkmeasure:spark-measure_2.11:0.16 \
    --conf spark.extraListeners=ch.cern.sparkmeasure.FlightRecorderStageMetrics \
    --conf spark.sparkmeasure.outputFilename=/home/ec2-user/metrics/q17_${i} \
    /home/ec2-user/tpch-spark/target/scala-2.11/spark-tpc-h-queries_2.11-1.0.jar 17 $i \
    > /home/ec2-user/logs/scale${i}_query17.log 2>&1
done


echo "Send an email to remind success of the job"
cd /home/ec2-user/multicloud-data-analytics/experiments
python send_email.py