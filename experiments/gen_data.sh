set -exo pipefail


function gen_lineitem {
    scale=$1
    sec=$2
    cd /home/ec2-user/data/tpch-spark/dbgen
    /home/ec2-user/data/tpch-spark/dbgen/dbgen -s $scale -S $sec -C $scale -T L
}

function gen_part {
    scale=$1
    sec=$2
    cd /home/ec2-user/data/tpch-spark/dbgen
    /home/ec2-user/data/tpch-spark/dbgen/dbgen -s $scale -S $sec -C $scale -T P
}

function wrap_lineitem {
    PID=() # record PID to array to check if PID exists - whether program finishes
    Njob=$1    # factual scale
    Nproc=$2
    scale=$3
    for((i=1; i<=Njob; )); do
        for((Ijob=0; Ijob<Nproc; Ijob++)); do
            if [[ $i -gt $Njob ]]; then
                break;
            fi
            if [[ ! "${PID[Ijob]}" ]] || ! kill -0 ${PID[Ijob]} 2> /dev/null; then
                gen_lineitem $Njob $i &
                PID[Ijob]=$!
                i=$((i+1))
            fi
        done
        sleep 1
    done
    wait

    mkdir -p /home/ec2-user/data/lineitem
    mv /home/ec2-user/data/tpch-spark/dbgen/lineitem* /home/ec2-user/data/lineitem/
    cd /home/ec2-user/data/lineitem/
    for f in *; do
        aws s3 cp $f s3://ttestspark/tpch-${scale}/lineitem.tbl/
    done
    rm -rf /home/ec2-user/data/lineitem
}

function wrap_part {
    PID=() # record PID to array to check if PID exists - whether program finishes
    Njob=$1    # scale
    Nproc=$2
    scale=$3
    for((i=1; i<=Njob; )); do
        for((Ijob=0; Ijob<Nproc; Ijob++)); do
            if [[ $i -gt $Njob ]]; then
                break;
            fi
            if [[ ! "${PID[Ijob]}" ]] || ! kill -0 ${PID[Ijob]} 2> /dev/null; then
                gen_part $Njob $i &
                PID[Ijob]=$!
                i=$((i+1))
            fi
        done
        sleep 1
    done
    wait

    mkdir -p /home/ec2-user/data/part
    mv /home/ec2-user/data/tpch-spark/dbgen/part* /home/ec2-user/data/part/
    cd /home/ec2-user/data/part/
    for f in *; do
        aws s3 cp $f s3://ttestspark/tpch-${scale}/part.tbl/
    done
    rm -rf /home/ec2-user/data/part
}

sudo yum install -y git gcc

cd /home/ec2-user/data
[ -d "/home/ec2-user/data/tpch-spark" ] && rm -rf /home/ec2-user/data/tpch-spark
git clone https://github.com/ssavvides/tpch-spark.git

cd /home/ec2-user/data/tpch-spark/dbgen

make

# wrap_lineitem 13 8 10
# wrap_part 13 8 10

wrap_lineitem 65 8 50
wrap_part 65 8 50

wrap_lineitem 129 8 100
wrap_part 129 8 100

wrap_lineitem 193 8 150
wrap_part 193 8 150