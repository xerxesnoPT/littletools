echo ********BackTime:`date +%Y-%m-%d--%T`********
OUT_DIR=/Users/guoyufei/testsh/         #备份存放路径
LINUX_USER=guoyufei                           #系统用户名
DB_USER=guoyufei                         
SRC_FOLD=/home/odoo/.local/share/Odoo
DB_NAME=demo
DAYS=7   #DAYS=5代表删除=5天前的备份，即只保留最近5天的
cd $OUT_DIR                                 #进入备份存放目录
DATE=`date +%Y_%m_%d`                       #获取当前系统时间
OUT_SQL="$DATE.sql"                         #备份数据库的文件名
TAR_SQL="SQL_bak_$DATE.tar.gz"        #最终保存的数据库备份文件名
pg_dump -U$DB_USER -d $DB_NAME -E utf-8 > $OUT_SQL #备份
tar -czf $TAR_SQL ./$OUT_SQL                #压缩为.tar.gz格式
rm $OUT_SQL                                 #删除.sql格式的备份文件
tar -czf "Odoo_bak_$DATE.tar.gz" $SRC_FOLD
find $OUT_DIR -name "SQL_bak_*" -type f -atime +$DAYS -exec rm {} \;  #删除7天前的备份文件
find $OUT_DIR -name "Odoo_bak_*" -type f -atime +$DAYS -exec rm {} \;  #删除7天前的备份文件
