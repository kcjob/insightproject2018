#!/bin/bash

RDS_MYSQL_ENDPOINT="masterdb.ch0ib4epgaak.us-west-2.rds.amazonaws.com";
RDS_MYSQL_USER="DB_USER";
RDS_MYSQL_PASS="USER_PASSWORD";
RDS_MYSQL_BASE="DB_NAME";

mysql -h $RDS_MYSQL_ENDPOINT -u $RDS_MYSQL_USER -p$RDS_MYSQL_PASS -D $RDS_MYSQL_BASE -e 'quit';

if [[ $? -eq 0 ]]; then
    echo "MySQL connection: OK";
else
    echo "MySQL connection: Fail";
fi;

# Run flask server
#----------------
./flask_server.sh
