# MySQL 数据库实验作业

MySQL 数据库课程实验作业合集，包含 9 个实验项目，并提供 Python 自动化脚本一键运行所有实验。

## 📚 实验目录

| 实验 | 名称 | 内容 |
|------|------|------|
| [Work_1](./Work_1/) | 概念模型与逻辑模型 | ER 图设计、关系模式转换 |
| [Work_2](./Work_2/) | 创建数据库和表 | CREATE DATABASE/TABLE、约束设置 |
| [Work_3](./Work_3/) | 数据插入、修改和删除 | INSERT、UPDATE、DELETE、REPLACE |
| [Work_4](./Work_4/) | 数据库查询 | SELECT、WHERE、JOIN、子查询 |
| [Work_5](./Work_5/) | 数据库查询(进阶) | 聚合函数、GROUP BY、HAVING |
| [Work_6](./Work_6/) | 存储过程 | PROCEDURE、IN/OUT 参数、流程控制 |
| [Work_7](./Work_7/) | 存储函数、触发器和事件 | FUNCTION、TRIGGER、EVENT |
| [Work_8](./Work_8/) | 事务处理和视图 | TRANSACTION、COMMIT/ROLLBACK、VIEW |
| [Work_9](./Work_9/) | 用户和权限管理 | CREATE USER、GRANT、ROLE |

## 🗄️ 数据库说明

| 数据库 | 说明 | 使用实验 |
|--------|------|----------|
| **yggl** | 员工管理系统 (Employees, Departments, Salary) | 实验 2-4, 6-9 |
| **XSCJ** | 学生选课成绩系统 (XS, KC, XS_KC) | 实验 5 |

## 🚀 快速开始

### 1. 环境要求

- **MySQL** 8.0+
- **Python** 3.8+
- **uv** (Python 包管理器)

### 2. 安装依赖

```bash
# 安装 uv (如果还没有)
pip install uv

# 安装项目依赖
uv sync
```

### 3. 配置数据库连接

在项目根目录创建 `.env` 文件：

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_CHARSET=utf8mb4
```

> ⚠️ `.env` 文件已在 `.gitignore` 中，不会被提交到 Git

### 4. 运行实验

```bash
# 启动交互式菜单
uv run python run_all_works.py
```

运行后会显示菜单：

```
============================================================
📚 MySQL 数据库实验作业 - 自动化运行脚本
============================================================

请选择要运行的实验:
  [1] 实验一：概念模型与逻辑模型
  [2] 实验二：数据库和数据表的创建
  [3] 实验三：数据的插入、修改、删除
  [4] 实验四：数据库的查询
  [5] 实验五：上机练习 (学生选课成绩数据库)
  [6] 实验六：存储过程
  [7] 实验七：存储函数、触发器和事件
  [8] 实验八：事务处理和视图
  [9] 实验九：用户和权限管理
  [a] 运行全部实验
  [q] 退出

请输入选项 (1-9/a/q):
```

- 输入 `1-9` 运行单个实验
- 输入 `a` 运行全部实验
- 输入 `q` 退出

## 📁 项目结构

```
MysqlHomeWork/
├── .env                  # 数据库配置 (需自行创建)
├── .gitignore
├── pyproject.toml        # Python 项目配置
├── uv.lock               # 依赖锁定文件
├── run_all_works.py      # 自动化运行脚本
├── README.md
└── Work_1-9/             # 各实验目录
    ├── README.md         # 实验题目
    ├── Answer.sql        # SQL 答案
    └── prepare.sql       # 准备脚本 (部分实验)
```

## 🛠️ 技术栈

- **MySQL 8.0** - 数据库
- **Python 3.8+** - 自动化脚本
- **pymysql** - MySQL 连接库
- **python-dotenv** - 环境变量管理
- **uv** - 现代 Python 包管理器

## 📝 许可证

本项目仅供学习参考使用
