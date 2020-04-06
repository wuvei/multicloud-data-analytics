declare -i Dline

file=$1
# getline
line=`grep -n "fs.defaultFS" $file | head -1 | cut -d ":" -f 1 | tr -d '\r\n'`
# echo $a
Dline=`awk "BEGIN{a=$line;b="1";c=(a+b);print c}"`;
echo "line is ${Dline}";

sed -i "${Dline}d" $file

add='\ \ \ \ <value>s3a://ttestspark/</value>'
sed -i -e "${line}a\\
$add" $file