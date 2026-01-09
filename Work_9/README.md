# 实验九 用户和权限管理

## 一、实验目的

1. 掌握 MySQL 用户管理的方法
2. 掌握 MySQL 权限管理的方法
3. 掌握 MySQL 角色管理的方法

## 二、实验内容

### 一、用户管理

#### 1. 创建用户
创建一个名为 `testuser` 的用户,设置密码为 `123456`,只允许从本地登录

#### 2. 创建允许远程登录的用户
创建一个名为 `remoteuser` 的用户,允许从任意主机登录

#### 3. 修改用户密码
修改 `testuser` 用户的密码为 `newpassword`

#### 4. 重命名用户
将 `testuser` 用户重命名为 `newuser`

#### 5. 删除用户
删除 `remoteuser` 用户

---

### 二、权限管理

#### 1. 授予单个权限
授予 `newuser` 用户对 yggl 数据库 Employees 表的 SELECT 权限

#### 2. 授予多个权限
授予 `newuser` 用户对 yggl 数据库 Employees 表的 INSERT、UPDATE、DELETE 权限

#### 3. 授予数据库级别权限
授予 `newuser` 用户对 yggl 数据库的所有权限

#### 4. 授予全局权限
授予 `newuser` 用户创建数据库的权限

#### 5. 查看用户权限
查看 `newuser` 用户的所有权限

#### 6. 撤销权限
撤销 `newuser` 用户对 yggl 数据库 Employees 表的 DELETE 权限

#### 7. 撤销所有权限
撤销 `newuser` 用户的所有权限

---

### 三、角色管理

#### 1. 创建角色
创建一个名为 `readonly` 的角色

#### 2. 为角色授权
为 `readonly` 角色授予 yggl 数据库的 SELECT 权限

#### 3. 将角色分配给用户
将 `readonly` 角色分配给 `newuser` 用户

#### 4. 删除角色
删除 `readonly` 角色



