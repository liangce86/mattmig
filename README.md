# mattmig
MYSQL迁移工具（全量+增量）

下载到linux环境下，执行./matt_mig打开主菜单。

mattmig介绍
   mattmig是一款利用binlog日志同步mysql数据库数据的软件，支持myisam、innodb引擎，实时同步业务数据库表数据。
在使用前本软件前，建议用户检查源实例和目的实例的引擎、参数、字符集等是否一致，并不再进行DDL相关操作。
mattmig打开时候会自动创建mattdata、mattetc、mattlog三个文件夹,分别存放备份文件、配置文件和日志文件。
备份账号应具有RELOAD, REPLICATION SLAVE, REPLICATION CLIENT和该对象的权限。

0:返回主菜单

1:全库备份

2:全库还原

3:校验数据

4:增量数据同步

5:查看同步日志

6:查看校验日志

7:停止增量同步。

100:退出


