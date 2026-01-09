#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pymysql>=1.1.0",
#     "python-dotenv>=1.0.0",
#     "cryptography>=42.0.0",
# ]
# ///
"""
MySQL 实验作业自动化脚本
完整实现 Work_1 到 Work_9 的所有实验流程

使用 uv 运行: uv run python run_all_works.py
"""

import os
import pymysql
from pymysql.cursors import DictCursor
import sys
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 数据库配置 (从 .env 读取)
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
    'charset': os.getenv('DB_CHARSET', 'utf8mb4'),
    'autocommit': False,
    'ssl_disabled': True,  # 禁用 SSL
}


class MySQLWorkRunner:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, database=None):
        """连接数据库"""
        config = DB_CONFIG.copy()
        if database:
            config['database'] = database
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor(DictCursor)

    def close(self):
        """关闭连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, fetch=False, commit=True):
        """执行SQL语句"""
        try:
            self.cursor.execute(sql)
            if commit:
                self.conn.commit()
            if fetch:
                return self.cursor.fetchall()
            return None
        except Exception as e:
            print(f"  ❌ 执行失败: {e}")
            self.conn.rollback()
            return None

    def execute_many(self, sqls, desc=""):
        """执行多条SQL语句"""
        for sql in sqls:
            if sql.strip():
                self.execute(sql)

    def print_result(self, result, title="查询结果"):
        """打印查询结果"""
        if result:
            print(f"  📋 {title}:")
            for row in result[:10]:  # 最多显示10条
                print(f"     {row}")
            if len(result) > 10:
                print(f"     ... 共 {len(result)} 条记录")
        else:
            print(f"  📋 {title}: 无数据")


# ============== Work 2: 创建数据库和表 ==============
def work_2(runner):
    """实验二：数据库和数据表的创建"""
    print("\n" + "="*60)
    print("📚 实验二：数据库和数据表的创建")
    print("="*60)

    runner.connect()

    # 1. 创建 yggl 数据库
    print("\n🔹 创建 yggl 数据库...")
    runner.execute("DROP DATABASE IF EXISTS yggl")
    runner.execute("CREATE DATABASE IF NOT EXISTS yggl")
    runner.execute("USE yggl")

    # 2. 创建 Departments 表
    print("🔹 创建 Departments 表...")
    runner.execute("""
        CREATE TABLE Departments(
            DepartmentID CHAR(3) NOT NULL PRIMARY KEY COMMENT '部门编号',
            DepartmentName CHAR(20) NOT NULL COMMENT '部门名',
            Note TEXT NULL COMMENT '备注'
        )
    """)

    # 3. 创建 Employees 表
    print("🔹 创建 Employees 表...")
    runner.execute("""
        CREATE TABLE Employees(
            EmployeeID CHAR(6) NOT NULL PRIMARY KEY COMMENT '员工编号',
            Name CHAR(10) NOT NULL COMMENT '姓名',
            Education CHAR(4) NOT NULL COMMENT '学历',
            Birthday DATE NOT NULL COMMENT '出生日期',
            Sex TINYINT(1) NOT NULL COMMENT '性别',
            WorkYear TINYINT(1) COMMENT '工作时间',
            Address VARCHAR(20) NULL COMMENT '地址',
            PhoneNumber CHAR(12) NULL COMMENT '电话号码',
            DepartmentID CHAR(3) NOT NULL COMMENT '部门编号',
            FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
        )
    """)

    # 4. 创建 Salary 表
    print("🔹 创建 Salary 表...")
    runner.execute("""
        CREATE TABLE Salary(
            EmployeeID CHAR(6) NOT NULL PRIMARY KEY COMMENT '员工编号',
            InCome FLOAT NOT NULL COMMENT '收入',
            OutCome FLOAT NOT NULL COMMENT '支出',
            FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
        )
    """)

    # 显示创建的表
    result = runner.execute("SHOW TABLES", fetch=True)
    runner.print_result(result, "yggl 数据库中的表")

    print("✅ 实验二完成！")
    runner.close()


# ============== Work 3: 数据插入、修改、删除 ==============
def work_3(runner):
    """实验三：数据的插入、修改、删除"""
    print("\n" + "="*60)
    print("📚 实验三：数据的插入、修改、删除")
    print("="*60)

    runner.connect('yggl')

    # 1. 插入部门数据
    print("\n🔹 插入部门数据...")
    runner.execute("""
        INSERT INTO Departments VALUES
        ('1', '财务部', NULL),
        ('2', '人力资源部', NULL),
        ('3', '经理办公室', NULL),
        ('4', '研发部', NULL),
        ('5', '市场部', NULL)
    """)

    # 2. 插入员工数据
    print("🔹 插入员工数据...")
    runner.execute("""
        INSERT INTO Employees VALUES
        ('000001', '王林', '大专', '1966-01-23', 1, 8, '中山路32-1-508', '83355668', '2'),
        ('010008', '伍容华', '本科', '1976-03-28', 1, 3, '北京东路100-2', '83321321', '1'),
        ('020010', '王向蓉', '硕士', '1982-12-09', 1, 2, '四牌楼10-10-108', '83792361', '1'),
        ('020018', '李丽', '大专', '1960-07-30', 0, 6, '中山东路102-2', '83413301', '1'),
        ('102201', '刘明', '本科', '1972-10-18', 1, 3, '虎踞路100-2', '83606608', '5'),
        ('102208', '朱骏', '硕士', '1965-09-28', 1, 2, '牌楼巷5-3-106', '84708817', '5'),
        ('108991', '钟敏', '硕士', '1979-08-10', 0, 4, '中山路10-3-105', '83346722', '3'),
        ('111006', '张石兵', '本科', '1974-10-01', 1, 1, '解放路34-1-203', '84563418', '5'),
        ('210678', '林涛', '大专', '1977-04-02', 1, 2, '中山北路24-35', '83467336', '3'),
        ('302566', '李玉珉', '本科', '1968-09-20', 1, 3, '热河路209-3', '58765991', '4'),
        ('308759', '叶凡', '本科', '1978-11-18', 1, 2, '北京西路3-7-52', '83308901', '4'),
        ('504209', '陈林琳', '大专', '1969-09-03', 0, 5, '汉中路120-4-12', '84468158', '4')
    """)

    # 3. 插入薪水数据
    print("🔹 插入薪水数据...")
    runner.execute("""
        INSERT INTO Salary VALUES
        ('000001', 2100.8, 123.09),
        ('010008', 1582.62, 88.03),
        ('020010', 2860, 198),
        ('020018', 2347.68, 180),
        ('102201', 2569.88, 185.65),
        ('102208', 1980, 100),
        ('108991', 3259.98, 281.52),
        ('111006', 1987.01, 79.58),
        ('210678', 2240, 121),
        ('302566', 2980.7, 210.2),
        ('308759', 2531.98, 199.08),
        ('504209', 2066.15, 108)
    """)

    # 4. 使用 REPLACE 语句
    print("🔹 使用 REPLACE 语句修改张石兵为张石山...")
    runner.execute("""
        REPLACE INTO Employees VALUES
        ('111006', '张石山', '本科', '1972-10-01', 1, 1, '解放路34-1-203', '84563418', '5')
    """)

    # 5. UPDATE 修改数据
    print("🔹 修改员工000001姓名为李四...")
    runner.execute("UPDATE Employees SET Name='李四' WHERE EmployeeID='000001'")

    # 6. 查看修改结果
    result = runner.execute("SELECT EmployeeID, Name FROM Employees WHERE EmployeeID IN ('000001', '111006')", fetch=True)
    runner.print_result(result, "修改后的员工")

    print("✅ 实验三完成！")
    runner.close()


# ============== Work 4: 数据库查询 ==============
def work_4(runner):
    """实验四：数据库的查询"""
    print("\n" + "="*60)
    print("📚 实验四：数据库的查询")
    print("="*60)

    runner.connect('yggl')

    queries = [
        ("1. 查询所有员工数据", "SELECT * FROM Employees"),
        ("2. 查询员工地址和电话", "SELECT Name, Address, PhoneNumber FROM Employees"),
        ("3. 查询000001员工信息", "SELECT Address, PhoneNumber FROM Employees WHERE EmployeeID = '000001'"),
        ("4. 使用别名查询", "SELECT EmployeeID AS '编号', Name AS '姓名', Sex AS '性别' FROM Employees"),
        ("5. 计算实际收入", "SELECT e.EmployeeID, e.Name, (s.InCome - s.OutCome) AS '实际收入' FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID"),
        ("6. 去重查询部门", "SELECT DISTINCT DepartmentID FROM Employees"),
        ("7. 月收入高于2000", "SELECT e.EmployeeID, e.Name, s.InCome FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID WHERE s.InCome > 2000"),
        ("8. 1970年后出生员工", "SELECT Name, Address FROM Employees WHERE Birthday > '1970-12-31'"),
        ("9. 姓王的员工", "SELECT * FROM Employees WHERE Name LIKE '王%'"),
        ("10. 按出生日期排序", "SELECT Name, Birthday FROM Employees ORDER BY Birthday"),
        ("11. 收入最低3人", "SELECT e.Name, s.InCome FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID ORDER BY s.InCome LIMIT 3"),
        ("12. 各部门员工数", "SELECT DepartmentID, COUNT(*) AS '员工数' FROM Employees GROUP BY DepartmentID"),
        ("13. 员工姓名和部门名", "SELECT e.Name, d.DepartmentName FROM Employees e JOIN Departments d ON e.DepartmentID = d.DepartmentID"),
        ("14. 财务部员工(子查询)", "SELECT Name FROM Employees WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = '财务部')"),
        ("15. 平均工资", "SELECT AVG(InCome) AS '平均收入' FROM Salary"),
    ]

    for title, sql in queries:
        print(f"\n🔹 {title}")
        result = runner.execute(sql, fetch=True)
        runner.print_result(result, "结果")

    print("\n✅ 实验四完成！")
    runner.close()


# ============== Work 5: 上机练习 ==============
def work_5(runner):
    """实验五：上机练习 (XSCJ数据库)"""
    print("\n" + "="*60)
    print("📚 实验五：上机练习 (学生选课成绩数据库)")
    print("="*60)

    runner.connect()

    # 创建 XSCJ 数据库
    print("\n🔹 创建 XSCJ 数据库...")
    runner.execute("DROP DATABASE IF EXISTS xscj")
    runner.execute("CREATE DATABASE xscj")
    runner.execute("USE xscj")

    # 创建表
    print("🔹 创建数据表...")
    runner.execute("""
        CREATE TABLE XSB (
            XH CHAR(6) PRIMARY KEY,
            XM CHAR(8) NOT NULL,
            XB CHAR(2),
            CSSJ DATE,
            ZY CHAR(12),
            ZXF TINYINT DEFAULT 0,
            BZ VARCHAR(200)
        )
    """)

    runner.execute("""
        CREATE TABLE KCB (
            KCH CHAR(3) PRIMARY KEY,
            KCM CHAR(16) NOT NULL,
            KS INT,
            XF TINYINT
        )
    """)

    runner.execute("""
        CREATE TABLE CJB (
            XH CHAR(6),
            KCH CHAR(3),
            CJ TINYINT,
            PRIMARY KEY (XH, KCH),
            FOREIGN KEY (XH) REFERENCES XSB(XH),
            FOREIGN KEY (KCH) REFERENCES KCB(KCH)
        )
    """)

    # 插入测试数据
    print("🔹 插入测试数据...")
    runner.execute("""
        INSERT INTO XSB VALUES
        ('081101', '王林', '男', '2000-02-10', '计算机', 50, NULL),
        ('081102', '程明', '男', '1999-02-01', '计算机', 50, NULL),
        ('081103', '王燕', '女', '2000-10-06', '计算机', 50, NULL),
        ('081104', '韦严平', '男', '2000-08-26', '计算机', 50, NULL),
        ('081106', '李方方', '男', '1999-11-20', '计算机', 54, NULL),
        ('081107', '李明', '男', '2000-05-01', '计算机', 54, '转专业'),
        ('081108', '林一帆', '男', '1999-08-05', '计算机', 52, NULL),
        ('081109', '张强民', '男', '1999-08-11', '计算机', 50, NULL),
        ('081110', '张蔚', '女', '2001-07-22', '计算机', 50, '三好学生'),
        ('081111', '赵琳', '女', '2000-03-18', '计算机', 50, NULL),
        ('081201', '王敏', '女', '2000-06-10', '通信工程', 42, NULL),
        ('081202', '王林', '男', '1999-01-29', '通信工程', 40, NULL),
        ('081203', '王玉民', '男', '2000-03-26', '通信工程', 42, NULL),
        ('081204', '马琳琳', '女', '1999-02-10', '通信工程', 42, NULL),
        ('081206', '李计', '男', '2000-09-20', '通信工程', 42, NULL),
        ('081210', '李红庆', '男', '1999-05-01', '通信工程', 44, '转专业'),
        ('081216', '孙祥欣', '男', '1999-03-09', '通信工程', 42, NULL),
        ('081218', '孙研', '男', '2000-10-09', '通信工程', 42, NULL),
        ('081220', '吴薇华', '女', '2000-03-18', '通信工程', 42, NULL),
        ('081221', '刘燕敏', '女', '1999-11-12', '通信工程', 42, NULL)
    """)

    runner.execute("""
        INSERT INTO KCB VALUES
        ('101', '计算机基础', 80, 5),
        ('102', '程序设计与语言', 68, 4),
        ('206', '离散数学', 68, 4),
        ('208', '数据结构', 68, 4),
        ('209', '操作系统', 68, 4),
        ('210', '计算机原理', 85, 5),
        ('212', '数据库原理', 68, 4),
        ('301', '计算机网络', 51, 3),
        ('302', '软件工程', 51, 3)
    """)

    runner.execute("""
        INSERT INTO CJB VALUES
        ('081101', '101', 80), ('081101', '102', 78), ('081101', '206', 76),
        ('081102', '102', 78), ('081102', '206', 78),
        ('081103', '101', 62), ('081103', '102', 70), ('081103', '206', 81),
        ('081104', '101', 90), ('081104', '102', 84), ('081104', '206', 65),
        ('081106', '101', 65), ('081106', '102', 71), ('081106', '206', 80),
        ('081107', '101', 78), ('081107', '102', 80), ('081107', '206', 68),
        ('081108', '101', 85), ('081108', '102', 64), ('081108', '206', 87),
        ('081109', '101', 66), ('081109', '102', 83),
        ('081110', '101', 95), ('081110', '102', 90), ('081110', '206', 89),
        ('081111', '101', 91), ('081111', '102', 70), ('081111', '206', 76),
        ('081201', '101', 80), ('081202', '101', 65), ('081203', '101', 87),
        ('081204', '101', 91), ('081206', '101', 76), ('081210', '101', 82),
        ('081216', '101', 81), ('081218', '101', 70), ('081220', '101', 82), ('081221', '101', 76)
    """)

    # 执行查询
    queries = [
        ("1. 查询所有女同学", "SELECT * FROM XSB WHERE XB = '女'"),
        ("2. 查询姓名和学号(使用别名)", "SELECT XM AS name, XH AS number FROM XSB"),
        ("3. 查询计算机专业学生", "SELECT * FROM XSB WHERE ZY = '计算机'"),
        ("4. 查询姓王的同学", "SELECT XM, XH FROM XSB WHERE XM LIKE '王%'"),
        ("5. 成绩70-85之间", "SELECT XH, KCH, CJ FROM CJB WHERE CJ BETWEEN 70 AND 85"),
        ("6. 课程按学分排序", "SELECT * FROM KCB ORDER BY XF ASC, KS DESC"),
        ("7. 学号081111的成绩", "SELECT x.XH, x.XM, k.KCM, c.CJ FROM XSB x JOIN CJB c ON x.XH = c.XH JOIN KCB k ON c.KCH = k.KCH WHERE x.XH = '081111'"),
        ("8. 选课学生统计", "SELECT XH, COUNT(*) AS '选课门数', AVG(CJ) AS '平均成绩' FROM CJB GROUP BY XH"),
    ]

    for title, sql in queries:
        print(f"\n🔹 {title}")
        result = runner.execute(sql, fetch=True)
        runner.print_result(result, "结果")

    print("\n✅ 实验五完成！")
    runner.close()


# ============== Work 6: 存储过程 ==============
def work_6(runner):
    """实验六：存储过程"""
    print("\n" + "="*60)
    print("📚 实验六：存储过程")
    print("="*60)

    runner.connect('yggl')

    # 1. 创建无参存储过程 p1
    print("\n🔹 创建存储过程 p1 (统计员工人数)...")
    runner.execute("DROP PROCEDURE IF EXISTS p1")
    runner.execute("""
        CREATE PROCEDURE p1()
        BEGIN
            DECLARE emp_count INT;
            SELECT COUNT(*) INTO emp_count FROM Employees;
            IF emp_count < 10 THEN
                SELECT '人太少' AS '人员状态';
            ELSE
                SELECT '满员' AS '人员状态';
            END IF;
        END
    """)
    print("  调用 p1():")
    result = runner.execute("CALL p1()", fetch=True)
    runner.print_result(result, "p1结果")

    # 2. 创建存储过程 p2 (备份中山路员工)
    print("\n🔹 创建存储过程 p2 (备份中山路员工)...")
    runner.execute("DROP PROCEDURE IF EXISTS p2")
    runner.execute("""
        CREATE PROCEDURE p2()
        BEGIN
            DROP TABLE IF EXISTS employees_bak;
            CREATE TABLE employees_bak LIKE Employees;
            INSERT INTO employees_bak SELECT * FROM Employees WHERE Address LIKE '%中山%';
            SELECT * FROM employees_bak;
            DROP TABLE employees_bak;
        END
    """)
    print("  调用 p2():")
    result = runner.execute("CALL p2()", fetch=True)
    runner.print_result(result, "中山路员工")

    # 3. 创建带输入参数的存储过程 p3
    print("\n🔹 创建存储过程 p3 (查询某部门员工)...")
    runner.execute("DROP PROCEDURE IF EXISTS p3")
    runner.execute("""
        CREATE PROCEDURE p3(IN dept_id CHAR(3))
        BEGIN
            SELECT * FROM Employees WHERE DepartmentID = dept_id;
        END
    """)
    print("  调用 p3('1') 查询财务部:")
    result = runner.execute("CALL p3('1')", fetch=True)
    runner.print_result(result, "财务部员工")

    # 4. 创建带输出参数的存储过程 p4
    print("\n🔹 创建存储过程 p4 (计算实际收入)...")
    runner.execute("DROP PROCEDURE IF EXISTS p4")
    runner.execute("""
        CREATE PROCEDURE p4(IN p_name CHAR(10), OUT income DECIMAL(7,2))
        BEGIN
            SELECT s.InCome - s.OutCome INTO income
            FROM Salary s JOIN Employees e ON s.EmployeeID = e.EmployeeID
            WHERE e.Name = p_name LIMIT 1;
        END
    """)
    runner.execute("CALL p4('朱骏', @income)")
    result = runner.execute("SELECT @income AS '朱骏实际收入'", fetch=True)
    runner.print_result(result, "结果")

    # 5. 创建提高工资的存储过程 p5
    print("\n🔹 创建存储过程 p5 (提高某学历员工工资)...")
    runner.execute("DROP PROCEDURE IF EXISTS p5")
    runner.execute("""
        CREATE PROCEDURE p5(IN edu CHAR(6), IN x DECIMAL(5,1))
        BEGIN
            UPDATE Salary s JOIN Employees e ON s.EmployeeID = e.EmployeeID
            SET s.InCome = s.InCome * (1 + x/100)
            WHERE e.Education = edu;
        END
    """)
    print("  提高硕士工资10%前:")
    result = runner.execute("SELECT e.Name, e.Education, s.InCome FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID WHERE e.Education = '硕士'", fetch=True)
    runner.print_result(result, "硕士工资")

    runner.execute("CALL p5('硕士', 10.0)")
    print("  提高硕士工资10%后:")
    result = runner.execute("SELECT e.Name, e.Education, s.InCome FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID WHERE e.Education = '硕士'", fetch=True)
    runner.print_result(result, "硕士工资")

    print("\n✅ 实验六完成！")
    runner.close()


# ============== Work 7: 存储函数、触发器、事件 ==============
def work_7(runner):
    """实验七：存储函数、触发器和事件"""
    print("\n" + "="*60)
    print("📚 实验七：存储函数、触发器和事件")
    print("="*60)

    runner.connect('yggl')

    # 允许创建函数
    runner.execute("SET GLOBAL log_bin_trust_function_creators = 1")

    # ========== 存储函数 ==========
    print("\n📌 一、存储函数")

    # 1. 获取员工总人数
    print("\n🔹 创建函数 GetTotalEmployees...")
    runner.execute("DROP FUNCTION IF EXISTS GetTotalEmployees")
    runner.execute("""
        CREATE FUNCTION GetTotalEmployees()
        RETURNS INT
        DETERMINISTIC
        BEGIN
            DECLARE total INT;
            SELECT COUNT(*) INTO total FROM Employees;
            RETURN total;
        END
    """)
    result = runner.execute("SELECT GetTotalEmployees() AS '员工总数'", fetch=True)
    runner.print_result(result, "结果")

    # 2. 判断员工是否在研发部
    print("\n🔹 创建函数 CheckResearchDept...")
    runner.execute("DROP FUNCTION IF EXISTS CheckResearchDept")
    runner.execute("""
        CREATE FUNCTION CheckResearchDept(emp_id CHAR(6))
        RETURNS VARCHAR(20)
        DETERMINISTIC
        BEGIN
            DECLARE dept_name CHAR(20);
            DECLARE edu CHAR(4);
            SELECT d.DepartmentName, e.Education INTO dept_name, edu
            FROM Employees e JOIN Departments d ON e.DepartmentID = d.DepartmentID
            WHERE e.EmployeeID = emp_id;
            IF dept_name = '研发部' THEN
                RETURN edu;
            ELSE
                RETURN 'NO';
            END IF;
        END
    """)
    result = runner.execute("SELECT CheckResearchDept('302566') AS '302566是否研发部'", fetch=True)
    runner.print_result(result, "结果")

    # ========== 触发器 ==========
    print("\n📌 二、触发器")

    # 1. 删除员工时同步删除工资记录
    print("\n🔹 创建触发器 AfterEmployeeDelete...")
    runner.execute("DROP TRIGGER IF EXISTS AfterEmployeeDelete")
    runner.execute("""
        CREATE TRIGGER AfterEmployeeDelete
        AFTER DELETE ON Employees
        FOR EACH ROW
        BEGIN
            DELETE FROM Salary WHERE EmployeeID = OLD.EmployeeID;
        END
    """)
    print("  ✅ 触发器创建成功 (删除员工时自动删除工资记录)")

    # 2. 创建 Departments2 表和插入触发器
    print("\n🔹 创建触发器 AfterDepartmentInsert...")
    runner.execute("DROP TABLE IF EXISTS Departments2")
    runner.execute("CREATE TABLE Departments2 LIKE Departments")
    runner.execute("DROP TRIGGER IF EXISTS AfterDepartmentInsert")
    runner.execute("""
        CREATE TRIGGER AfterDepartmentInsert
        AFTER INSERT ON Departments
        FOR EACH ROW
        BEGIN
            INSERT INTO Departments2 VALUES (NEW.DepartmentID, NEW.DepartmentName, NEW.Note);
        END
    """)

    # 测试插入触发器
    runner.execute("INSERT INTO Departments VALUES ('6', '测试部', '测试用')")
    result = runner.execute("SELECT * FROM Departments2", fetch=True)
    runner.print_result(result, "Departments2 (通过触发器同步)")

    # ========== 事件 ==========
    print("\n📌 三、事件")

    # 创建事件日志表
    print("\n🔹 创建事件日志表...")
    runner.execute("DROP TABLE IF EXISTS eventlog")
    runner.execute("""
        CREATE TABLE eventlog (
            log_id INT AUTO_INCREMENT PRIMARY KEY,
            event_type INT,
            log_time DATETIME
        )
    """)

    # 开启事件调度器
    runner.execute("SET GLOBAL event_scheduler = ON")

    # 创建立即执行事件
    print("🔹 创建立即执行事件...")
    runner.execute("DROP EVENT IF EXISTS EventImmediate")
    runner.execute("""
        CREATE EVENT EventImmediate
        ON SCHEDULE AT CURRENT_TIMESTAMP
        DO INSERT INTO eventlog (event_type, log_time) VALUES (1, NOW())
    """)

    import time
    time.sleep(1)
    result = runner.execute("SELECT * FROM eventlog", fetch=True)
    runner.print_result(result, "事件日志")

    print("\n✅ 实验七完成！")
    runner.close()


# ============== Work 8: 事务处理和视图 ==============
def work_8(runner):
    """实验八：事务处理和视图"""
    print("\n" + "="*60)
    print("📚 实验八：事务处理和视图")
    print("="*60)

    runner.connect('yggl')

    # ========== 事务处理演示 ==========
    print("\n📌 一、事务处理")

    print("\n🔹 1. 演示事务回滚...")
    # 开始事务
    runner.execute("START TRANSACTION", commit=False)
    runner.execute("UPDATE Salary SET InCome = InCome + 1000 WHERE EmployeeID = '000001'", commit=False)

    result = runner.execute("SELECT EmployeeID, InCome FROM Salary WHERE EmployeeID = '000001'", fetch=True)
    runner.print_result(result, "修改后(未提交)")

    # 回滚
    runner.conn.rollback()
    result = runner.execute("SELECT EmployeeID, InCome FROM Salary WHERE EmployeeID = '000001'", fetch=True)
    runner.print_result(result, "回滚后")

    print("\n🔹 2. 演示事务提交...")
    runner.execute("START TRANSACTION", commit=False)
    runner.execute("UPDATE Salary SET InCome = InCome + 100 WHERE EmployeeID = '000001'", commit=False)
    runner.conn.commit()

    result = runner.execute("SELECT EmployeeID, InCome FROM Salary WHERE EmployeeID = '000001'", fetch=True)
    runner.print_result(result, "提交后")

    print("\n🔹 3. 查看当前隔离级别...")
    result = runner.execute("SELECT @@transaction_isolation AS '隔离级别'", fetch=True)
    runner.print_result(result, "结果")

    # ========== 视图 ==========
    print("\n📌 二、视图")

    # 1. 创建部门视图
    print("\n🔹 创建视图 ds_view (部门全部信息)...")
    runner.execute("DROP VIEW IF EXISTS ds_view")
    runner.execute("CREATE VIEW ds_view AS SELECT * FROM Departments")
    result = runner.execute("SELECT * FROM ds_view", fetch=True)
    runner.print_result(result, "ds_view")

    # 2. 创建员工实际收入视图
    print("\n🔹 创建视图 Employees_view (员工实际收入)...")
    runner.execute("DROP VIEW IF EXISTS Employees_view")
    runner.execute("""
        CREATE VIEW Employees_view AS
        SELECT e.EmployeeID, e.Name, (s.InCome - s.OutCome) AS ActualIncome
        FROM Employees e JOIN Salary s ON e.EmployeeID = s.EmployeeID
    """)
    result = runner.execute("SELECT * FROM Employees_view", fetch=True)
    runner.print_result(result, "Employees_view")

    # 3. 通过视图查询
    print("\n🔹 从视图查询部门号为3的部门名称...")
    result = runner.execute("SELECT DepartmentName FROM ds_view WHERE DepartmentID = '3'", fetch=True)
    runner.print_result(result, "结果")

    print("\n🔹 查询王林的实际收入...")
    result = runner.execute("SELECT ActualIncome FROM Employees_view WHERE Name LIKE '%林%'", fetch=True)
    runner.print_result(result, "结果")

    print("\n✅ 实验八完成！")
    runner.close()


# ============== Work 9: 用户和权限管理 ==============
def work_9(runner):
    """实验九：用户和权限管理"""
    print("\n" + "="*60)
    print("📚 实验九：用户和权限管理")
    print("="*60)

    runner.connect()

    # ========== 用户管理 ==========
    print("\n📌 一、用户管理")

    # 1. 创建用户
    print("\n🔹 创建用户 user_1 和 user_2...")
    runner.execute("DROP USER IF EXISTS 'user_1'@'localhost'")
    runner.execute("DROP USER IF EXISTS 'user_2'@'localhost'")
    runner.execute("CREATE USER 'user_1'@'localhost' IDENTIFIED BY '1234'")
    runner.execute("CREATE USER 'user_2'@'localhost' IDENTIFIED BY '1234'")
    print("  ✅ 用户创建成功")

    # 2. 重命名用户
    print("\n🔹 将 user_2 重命名为 user_3...")
    runner.execute("RENAME USER 'user_2'@'localhost' TO 'user_3'@'localhost'")
    print("  ✅ 重命名成功")

    # 3. 修改密码
    print("\n🔹 修改 user_3 密码为 123456...")
    runner.execute("ALTER USER 'user_3'@'localhost' IDENTIFIED BY '123456'")
    print("  ✅ 密码修改成功")

    # 4. 删除用户
    print("\n🔹 删除用户 user_3...")
    runner.execute("DROP USER 'user_3'@'localhost'")
    print("  ✅ 用户删除成功")

    # ========== 权限管理 ==========
    print("\n📌 二、权限管理")

    # 1. 授予查询权限
    print("\n🔹 授予 user_1 对 yggl.Employees 的 SELECT 权限...")
    runner.execute("GRANT SELECT ON yggl.Employees TO 'user_1'@'localhost'")
    print("  ✅ 权限授予成功")

    # 2. 授予更多权限
    print("\n🔹 授予 user_1 INSERT, UPDATE, DELETE 权限...")
    runner.execute("GRANT INSERT, UPDATE, DELETE ON yggl.Employees TO 'user_1'@'localhost'")

    # 3. 显示权限
    print("\n🔹 显示 user_1 的权限...")
    result = runner.execute("SHOW GRANTS FOR 'user_1'@'localhost'", fetch=True)
    runner.print_result(result, "user_1 权限")

    # 4. 撤销权限
    print("\n🔹 撤销 user_1 的 SELECT 权限...")
    runner.execute("REVOKE SELECT ON yggl.Employees FROM 'user_1'@'localhost'")
    result = runner.execute("SHOW GRANTS FOR 'user_1'@'localhost'", fetch=True)
    runner.print_result(result, "撤销后的权限")

    # ========== 角色管理 ==========
    print("\n📌 三、角色管理")

    # 1. 创建角色
    print("\n🔹 创建角色 db_read 和 db_write...")
    runner.execute("DROP ROLE IF EXISTS db_read, db_write")
    runner.execute("CREATE ROLE db_read, db_write")
    print("  ✅ 角色创建成功")

    # 2. 给角色授权
    print("\n🔹 给角色授权...")
    runner.execute("GRANT SELECT ON yggl.* TO db_read")
    runner.execute("GRANT INSERT, UPDATE, DELETE, SELECT ON yggl.* TO db_write")
    print("  ✅ 角色授权成功")

    # 3. 创建用户并分配角色
    print("\n🔹 创建 user_test 并分配 db_read 角色...")
    runner.execute("DROP USER IF EXISTS 'user_test'@'localhost'")
    runner.execute("CREATE USER 'user_test'@'localhost' IDENTIFIED BY '1234'")
    runner.execute("GRANT db_read TO 'user_test'@'localhost'")
    runner.execute("SET DEFAULT ROLE ALL TO 'user_test'@'localhost'")
    print("  ✅ 角色分配成功")

    result = runner.execute("SHOW GRANTS FOR 'user_test'@'localhost'", fetch=True)
    runner.print_result(result, "user_test 权限")

    # 清理
    print("\n🔹 清理测试用户...")
    runner.execute("DROP USER IF EXISTS 'user_1'@'localhost'")
    runner.execute("DROP USER IF EXISTS 'user_test'@'localhost'")
    runner.execute("DROP ROLE IF EXISTS db_read, db_write")
    print("  ✅ 清理完成")

    print("\n✅ 实验九完成！")
    runner.close()


# ============== 主程序 ==============
def main():
    print("=" * 60)
    print("🎓 MySQL 实验作业自动化脚本")
    print("=" * 60)
    print("""
请选择要运行的实验:
  1 - 实验一 (E-R图设计，无需数据库操作)
  2 - 实验二 (创建数据库和表)
  3 - 实验三 (数据插入、修改、删除)
  4 - 实验四 (数据库查询)
  5 - 实验五 (上机练习)
  6 - 实验六 (存储过程)
  7 - 实验七 (存储函数、触发器、事件)
  8 - 实验八 (事务处理和视图)
  9 - 实验九 (用户和权限管理)
  a - 运行全部实验 (2-9)
  q - 退出
""")

    runner = MySQLWorkRunner()

    while True:
        choice = input("\n请输入选项 (1-9/a/q): ").strip().lower()

        if choice == 'q':
            print("👋 再见！")
            break
        elif choice == '1':
            print("\n📚 实验一：概念模型与逻辑模型")
            print("  此实验为 E-R 图设计，无需数据库操作。")
            print("  请参考 Work_1/README.md 中的题目要求。")
        elif choice == '2':
            work_2(runner)
        elif choice == '3':
            work_3(runner)
        elif choice == '4':
            work_4(runner)
        elif choice == '5':
            work_5(runner)
        elif choice == '6':
            work_6(runner)
        elif choice == '7':
            work_7(runner)
        elif choice == '8':
            work_8(runner)
        elif choice == '9':
            work_9(runner)
        elif choice == 'a':
            print("\n🚀 运行全部实验...")
            work_2(runner)
            work_3(runner)
            work_4(runner)
            work_5(runner)
            work_6(runner)
            work_7(runner)
            work_8(runner)
            work_9(runner)
            print("\n" + "=" * 60)
            print("🎉 全部实验完成！")
            print("=" * 60)
        else:
            print("❌ 无效选项，请重新输入。")


if __name__ == "__main__":
    if DB_CONFIG['password'] == 'your_password':
        print("\n⚠️  注意：请先在 .env 文件中配置数据库密码")
        print("   编辑 .env 文件，修改 DB_PASSWORD=your_password\n")
    
    main()
