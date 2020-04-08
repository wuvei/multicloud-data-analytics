sudo mkfs -t xfs /dev/nvme1n1

sudo mkdir -p /home/ec2-user/data

sudo mount /dev/nvme1n1 /home/ec2-user/data

sudo chmod 777 /home/ec2-user/data