use yggl;
#  1. 创建存储过程p1
# 创建无参存储过程p1并调用,功能为：
# 获取 employees表中的员工人数来初始化一个局部变量,
# 如果人数小于10输出人“太少”,否则“满员”
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
    DECLARE emp_count INT;
    SELECT COUNT(*) INTO emp_count FROM employees;

    IF emp_count < 10 THEN
        SELECT '人太少' AS '人员状态';
    ELSE
        SELECT '满员'  AS '人员状态';
    END IF;
end $$
DELIMITER ;

-- 调用示例
CALL p1();

-- 2. 创建存储过程p2
# 创建无参存储过程p2并调用,功能为：
# 创建与employees一样结构的表employees_bak,
# 将住在中山路的员工插入employees_bak,
# 查询employees_bak,删除employees_bak
DELIMITER $$
CREATE PROCEDURE p2()
BEGIN
    -- 创建备份表
    CREATE TABLE employees_bak LIKE employees;

    -- 插入中山路员工
    INSERT INTO employees_bak
        SELECT * FROM employees
    WHERE Address LIKE '%中山路%';

    -- 查询结果
    SELECT * FROM employees_bak;

    -- 删除备份表
    DROP TABLE employees_bak;
END $$
DELIMITER ;

-- 调用示例
CALL p2();

-- 3. 创建表和存储过程p3
# 创建表 randnumber
# 	字段：id 自增长,
# 		data int；
# 创建无参存储过程p3并调用,功能为：
# 向表中插入50个的随机数(1-30),但如果插入的数为18,则终止插入
CREATE TABLE randnumber (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        data INT
);

DELIMITER $$
CREATE PROCEDURE p3()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE rand_num INT;

    loop_lable:loop
        IF i>50 THEN
            LEAVE loop_lable;
        END IF;

        SET rand_num = FLOOR(RAND() * 30) + 1;

        IF rand_num = 18 THEN
            LEAVE loop_lable;
        END IF;

        INSERT INTO randnumber (data) VALUES (rand_num);
        SET i = i + 1;
    END loop;
END;
DELIMITER ;

-- 调用示例
CALL p3();

-- 4. 创建存储过程p4
# 创建存储过程p4(in name char(10),out income decimal(7,2)),
# 计算一个员工的实际收入,并调用该存储过程,将员工朱骏的实际收入保存在一个用户变量中
DELIMITER $$
CREATE PROCEDURE p4(IN p_name CHAR(10), OUT income DECIMAL(7,2))
BEGIN
    SELECT s.InCome - s.OutCome INTO income
    FROM Salary s
             JOIN Employees e ON s.EmployeeID = e.EmployeeID
    WHERE e.Name = p_name
    LIMIT 1;
END $$
DELIMITER ;

-- 调用示例
CALL p4('朱骏', @income);
SELECT @income;

-- 5. 创建存储过程p5
# 创建存储过程 p5(in edu char(6),in x decimal(5,1))
# 将所有某种学历的员工的收入提高%x, 并调用该存储过程,将所有硕士学历的员工的收入提高10%
DELIMITER $$
CREATE PROCEDURE p5(IN edu CHAR(6), IN x DECIMAL(5,1))
BEGIN
    UPDATE Salary s
        JOIN Employees e ON s.EmployeeID = e.EmployeeID
    SET s.InCome = s.InCome * (1 + x/100)
    WHERE e.Education = edu;
END $$
DELIMITER ;

-- 调用示例(提高硕士收入10%)
CALL p5('硕士', 10.0);