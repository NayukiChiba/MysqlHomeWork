# 实验二 数据库和数据表的创建

## 一、实验目的

1. 掌握使用命令方式创建数据库的方法
2. 掌握使用 MySQL workbench 创建数据库的方法
3. 掌握使用命令方式创建数据表的方法
4. 掌握使用 MySQL workbench 创建数据表的方法
5. 掌握约束的使用方法

## 二、实验内容

### 题目一：创建 yggl 数据库

创建 yggl 数据库,包含以下三个数据表：

#### Employees 表(员工信息表)

| 列名 | 数据类型 | 长度 | 是否为空 | 说明 |
|------|----------|------|----------|------|
| EmployeelD | char | 6 | 否 | 员工编号,主码 |
| Name | char | 10 | 否 | 姓名 |
| Education | char | 4 | 否 | 学历 |
| Birthday | date | - | 否 | 出生日期 |
| Sex | tinyint | 1 | 否 | 性别(0为女,1为男) |
| WorkYear | tinyint | 1 | 是 | 工作时间 |
| Address | varchar | 20 | 是 | 地址 |
| PhoneNumber | char | 12 | 是 | 电话号码 |
| DepartmentID | char | 3 | 否 | 员工部门号,外码 |

#### Departments 表(部门信息表)

| 列名 | 数据类型 | 长度 | 是否为空 | 说明 |
|------|----------|------|----------|------|
| DepartmentID | char | 3 | 否 | 部门编号,主码 |
| DepartmentName | char | 20 | 否 | 部门名 |
| Note | text | - | 是 | 备注 |

#### Salary 表(员工薪水表)

| 列名 | 数据类型 | 长度 | 是否为空 | 说明 |
|------|----------|------|----------|------|
| EmployeelD | char | 6 | 否 | 员工编号,主码 |
| Income | float | - | 否 | 收入 |
| Outcome | float | - | 否 | 支出 |

### 任务要求

#### 命令方式：

1. 以命令方式创建数据库
2. 以命令方式创建表 Employees
3. 以命令方式创建表 Departments
4. 以命令方式创建表 Salary
5. 创建上面三个表时分别使用三种定义主键约束的方式
6. 在创建 Employees 表时,使用外键约束定义 DepartmentID 是参照 Departments 表 DepartmentID 的外码

#### MySQL Workbench 方式：

7. 以 MySQL Workbench 方式创建 yggl 数据库
8. 以 MySQL Workbench 方式创建以上三个表

---

### 题目二：创建 netshop 数据库

创建 netshop 数据库(网上购物系统),包含以下 10 个数据表：

#### shop_user 用户信息表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| user_id | int | - | 否 | 用户编号(主键) |
| user_name | char | 40 | 否 | 用户登录名 |
| password | char | 40 | 否 | 登录密码 |
| sex | tinyint | 1 | 否 | 性别(1为男,0为女) |
| regdate | datetime | - | 否 | 注册日期 |
| level | int | - | 是 | 用户等级(钻石、黄金、普通) |
| email | char | 50 | 是 | 电子邮件 |
| IDcard | char | 18 | 是 | 身份证号码 |
| address | char | 100 | 是 | 联系地址 |
| linkphone | char | 20 | 是 | 联系电话 |

#### category 商品类别表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| category_id | int | - | 否 | 商品类别编号(主键) |
| category_name | varchar | 40 | 否 | 商品类别名称 |
| up_category | int | - | 是 | 上级商品类别编号 |
| isleaf | tinyint | 1 | 否 | 是否是叶子类别 |

#### goods 商品信息表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| goods_id | int | - | 否 | 商品编号(主键) |
| goods_name | varchar | 100 | 否 | 商品名称 |
| category_id | int | - | 否 | 商品类别编号(外键) |
| price | decimal | (10,2) | 否 | 商品价格 |
| store | int | - | 是 | 库存量 |
| sold | int | - | 是 | 已售数量 |
| description | text | - | 是 | 商品描述 |
| pic | char | 100 | 是 | 商品图片路径 |
| status | tinyint | 1 | 否 | 商品状态(上下架) |

#### orders 订单表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| order_id | int | - | 否 | 订单编号(主键) |
| user_id | int | - | 否 | 用户编号(外键) |
| orderdate | datetime | - | 是 | 订单日期 |
| status | tinyint | 1 | 否 | 订单状态 |
| totalprice | decimal | (10,2) | 否 | 订单总金额 |
| pay_method | varchar | 20 | 是 | 支付方式 |

#### order_detail 订单明细表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| detail_id | int | - | 否 | 订单明细编号(主键) |
| order_id | int | - | 否 | 订单编号(外键) |
| goods_id | int | - | 否 | 商品编号(外键) |
| num | int | - | 否 | 商品数量 |
| price | decimal | (10,2) | 否 | 成交价 |
| totalprice | decimal | (10,2) | 否 | 商品总金额 |

#### shipping 配送信息表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| ship_id | int | - | 否 | 配送编号(主键) |
| order_id | int | - | 否 | 订单编号(外键) |
| ship_method | char | 20 | 是 | 配送方式 |
| ship_fee | decimal | (8,2) | 否 | 配送费 |
| ship_address | char | 100 | 否 | 配送地址 |
| ship_phone | char | 20 | 否 | 配送电话 |

#### favorite 收藏表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| fav_id | int | - | 否 | 收藏编号(主键) |
| user_id | int | - | 否 | 用户编号(外键) |
| goods_id | int | - | 否 | 商品编号(外键) |
| favdate | datetime | - | 是 | 收藏日期 |

#### cart 购物车表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| cart_id | int | - | 否 | 购物车编号(主键) |
| user_id | int | - | 否 | 用户编号(外键) |
| goods_id | int | - | 否 | 商品编号(外键) |
| num | int | - | 否 | 商品数量 |
| adddate | datetime | - | 是 | 添加日期 |

#### comment 商品评论表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| comm_id | int | - | 否 | 评论编号(主键) |
| goods_id | int | - | 否 | 商品编号(外键) |
| user_id | int | - | 否 | 用户编号(外键) |
| content | varchar | 400 | 是 | 评论内容 |
| comdate | datetime | - | 是 | 评论日期 |

#### admin 管理员表

| 列名 | 类型 | 长度 | 是否空 | 说明 |
|------|------|------|--------|------|
| admin_id | int | - | 否 | 管理员编号(主键) |
| admin_name | char | 40 | 否 | 管理员账号 |
| password | char | 40 | 否 | 管理员密码 |
| last_logintime | datetime | - | 是 | 最后登录时间 |

### 任务要求

1. 在数据库中画出 E-R 图
2. 创建以上 10 个数据表
