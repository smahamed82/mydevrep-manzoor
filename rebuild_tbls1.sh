#!/bin/ksh
#
#
export ORACLE_HOME=/u01/app/oracle/product/11.2.0.3
export PATH=$ORACLE_HOME/bin:$PATH

echo "Started" > /home/oracle/status.log

sqlplus proddba/ahamed@testdb1 @/home/oracle/rebuild_sql.sql &
sqlplus proddba/ahamed@testdb2 @/home/oracle/rebuild_sql.sql &

wait
echo "Completed" >> /home/oracle/status.log
