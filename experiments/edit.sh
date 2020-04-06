declare -i Dline

# getline
line=`grep -n "fs.defaultFS" core-site.xml | head -1 | cut -d ":" -f 1 | tr -d '\r\n'`
# echo $a
Dline=`awk "BEGIN{a=$line;b="1";c=(a+b);print c}"`;
echo "line is ${Dline}";

sed -i "${Dline}d" core-site.xml

add='\ \ \ \ <value>s3a://ttestspark/</value>'
sed -i '' -e "${line}a\\
$add" core-site.xml