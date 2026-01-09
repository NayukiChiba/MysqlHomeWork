# 用户管理
## 以 root 用户登录,创建用户 user_1 和 user_2,密码都设为 1234
CREATE USER 'user_1'@'localhost' IDENTIFIED BY '1234';
CREATE USER 'user_2'@'localhost' IDENTIFIED BY '1234';
## 将用户 user_2 的名称修改为 user_3
RENAME USER 'user_2'@'localhost' TO 'user_3'@'localhost';
## 将用户 user_3 的密码修改为 123456
ALTER USER 'user_3'@'localhost' IDENTIFIED BY '123456';
## 删除用户 user_3
DROP USER 'user_3'@'localhost';
## 以 user_1 用户登录,切换到 mydb 数据库
CREATE DATABASE mydb;
USE mydb; -- 若 mydb 不存在会报错,建议替换为 USE yggl;
# 权限管理
## 切换到 root 用户,授予用户 user_1 对 YGGL 数据库 Employees 表的查询操作权限
GRANT SELECT ON yggl.Employees TO 'user_1'@'localhost';
## 切换到 user_1 用户,查询 YGGL 数据库 Employees 表的数据；往 Employees表插入一条员工数据
SELECT * FROM yggl.Employees;
INSERT INTO yggl.Employees VALUES ('999999', '测试', '本科', '2000-01-01', '男', 1, '地址', '123456', '1');
## 切换到 root 用户,授予用户 user_1 对 YGGL 数据 Employees 表的插入、修改、删除操作权限,显示用户 user_1 的权限
GRANT INSERT, UPDATE, DELETE ON yggl.Employees TO 'user_1'@'localhost';
SHOW GRANTS FOR 'user_1'@'localhost';
## 切换到 user_1 用户,重复(2)中的操作
INSERT INTO yggl.Employees VALUES ('999999', '测试', '本科', '2000-01-01', '男', 1, '地址', '123456', '1');
## 切换到 root 用户,撤销用户 user_1 对 Employees 表的 select 权限
REVOKE SELECT ON yggl.Employees FROM 'user_1'@'localhost';
## 切换到 user_1 用户,查询 Employees 表中的数据
SELECT * FROM yggl.Employees; -- 无权限
## 切换到 root 用户,撤销用户 user_1 的所有权限
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_1'@'localhost';
# 角色管理
## 创建用户 user_3 和 user_4,密码设为 1234；创建角色 db_read 和 db_write
CREATE USER 'user_3'@'localhost' IDENTIFIED BY '1234';
CREATE USER 'user_4'@'localhost' IDENTIFIED BY '1234';
## 分别授予对 YGGL 数据库的 select 权限和 insert、update、delete、select 权限
CREATE ROLE db_read, db_write;
GRANT SELECT ON yggl.* TO db_read;
GRANT INSERT, UPDATE, DELETE, SELECT ON yggl.* TO db_write;
## 分别为 user_3 和 user_4 分配 db_read 和 db_write 权限
GRANT db_read TO 'user_3'@'localhost';
GRANT db_write TO 'user_4'@'localhost';
SET DEFAULT ROLE ALL TO 'user_3'@'localhost', 'user_4'@'localhost';
## 并对 user_3 和 user_4 的权限进行检验
SELECT * FROM yggl.Employees; -- 成功
INSERT INTO yggl.Employees VALUES (...); -- 失败
INSERT INTO yggl.Employees VALUES (...); -- 成功