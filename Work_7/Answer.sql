USE yggl;

# 1. 储存函数
## 创建一个存储函数,返回员工的总人数
DELIMITER //
CREATE FUNCTION GetTotalEmployees()
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total FROM Employees;
    RETURN total;
END //
DELIMITER ;
## 创建一个存储函数,删除在 Salary 表中有但在 Employees 表中不存在的员工号若在 Employees 表中存在则返回 FALSE,若不存在则删除该员工号并返回 TRUE
DELIMITER //
CREATE PROCEDURE DeleteInvalidEmployee(IN emp_id CHAR(6), OUT result BOOLEAN)
BEGIN
    DECLARE exists_flag INT;
    SELECT COUNT(*) INTO exists_flag FROM Employees WHERE EmployeeID = emp_id;
    IF exists_flag > 0 THEN
        SET result = FALSE;
    ELSE
        DELETE FROM Salary WHERE EmployeeID = emp_id;
        SET result = TRUE;
    END IF;
END //
DELIMITER ;
## 创建存储函数,判断员工是否在研发部工作,若是则返回其学历,若不是则返回字符串“NO”
DELIMITER //
CREATE FUNCTION CheckResearchDept(emp_id CHAR(6))
    RETURNS VARCHAR(255)
    DETERMINISTIC
BEGIN
    DECLARE dept_name CHAR(20);
    DECLARE edu CHAR(4);
    SELECT d.DepartmentName, e.Education INTO dept_name, edu
    FROM Employees e
             JOIN Departments d ON e.DepartmentID = d.DepartmentID
    WHERE e.EmployeeID = emp_id;
    IF dept_name = '研发部' THEN
        RETURN edu;
    ELSE
        RETURN 'NO';
    END IF;
END //
DELIMITER ;
## 创建一个存储函数,将工作时间满 4 年的员工收入增加 500 元
DELIMITER //
CREATE PROCEDURE IncreaseSalaryForFourYears()
BEGIN
    -- 通过 Employees.WorkYear 筛选员工,并关联更新 Salary.Income
    UPDATE Salary s
        JOIN Employees e ON s.EmployeeID = e.EmployeeID
    SET s.Income = s.Income + 500
    WHERE e.WorkYear >= 4;
END //
DELIMITER ;
# 2. 触发器
## 创建触发器,在 Employees 表中删除员工信息的同时将 Salary表中该员工的信息删除,以确保数据完整性
## 创建完后删除 Employees 表中的一行数据,然后查看 Salary 表中的变化情况
DELIMITER //
CREATE TRIGGER AfterEmployeeDelete
    AFTER DELETE ON Employees
    FOR EACH ROW
BEGIN
    DELETE FROM Salary WHERE EmployeeID = OLD.EmployeeID;
END //
DELIMITER ;
## 假设 Departments2 表和 Department 表的结构和内容都相同,在 Departments 上创建一个触发器,如果添加一个新的部门,该部门也会添加到 Departments2 表中
CREATE TABLE Departments2 LIKE Departments;
DELIMITER //
CREATE TRIGGER AfterDepartmentInsert
    AFTER INSERT ON Departments
    FOR EACH ROW
BEGIN
    INSERT INTO Departments2 (DepartmentID, DepartmentName, Note)
    VALUES (NEW.DepartmentID, NEW.DepartmentName, NEW.Note);
END //
DELIMITER ;
## 创建触发器,当修改 Employees 表时,若将 Employees 表中员工的工作时间增加 1 年,则将收入增加 500 元,若工作时间增加 2 年则收入增加 1000 元,依次增加若工作时间减少则无变化
DELIMITER //
CREATE TRIGGER UpdateSalaryOnWorkYearIncrease
    AFTER UPDATE ON Employees
    FOR EACH ROW
BEGIN
    DECLARE diff INT;
    SET diff = NEW.WorkYear - OLD.WorkYear;  -- 计算工作时间增量
    IF diff > 0 THEN
        -- 根据增量更新 Salary 表中的 Income
        UPDATE Salary
        SET Income = Income + (diff * 500)
        WHERE EmployeeID = NEW.EmployeeID;
    END IF;
END //
DELIMITER ;
## 创建触发器,当 Departments 表中部门发生变化时,Employees表中对应部门员工所属的部门也将改变
DELIMITER //
CREATE TRIGGER AfterDepartmentUpdate
    AFTER UPDATE ON Departments
    FOR EACH ROW
BEGIN
    UPDATE Employees
    SET DepartmentID = NEW.DepartmentID
    WHERE DepartmentID = OLD.DepartmentID;
END //
DELIMITER ;
# 3. 事件
## 创建表eventlog,含3个字段:
## log_id int 自增长 主键;
## event_type int;
## log_time datetime
CREATE TABLE eventlog (
                       log_id INT AUTO_INCREMENT PRIMARY KEY,
                       event_type INT,
                       log_time DATETIME);
## 以下3个小题的事件执行的内容为在yggl.eventlog插入一条记录
## event_type为小题编号,log_time为now()

# (1)创建一个立即执行的事件
CREATE EVENT EventImmediate
    ON SCHEDULE AT CURRENT_TIMESTAMP
    DO
    INSERT INTO eventlog (event_type, log_time) VALUES (1, NOW());
# (2)创建一个事件,每2分钟执行一次,它从现在开始直到 2025 年 12 月31日结束
CREATE EVENT EventEveryTwoMinutes
    ON SCHEDULE EVERY 2 MINUTE
        STARTS NOW()
        ENDS '2025-12-31 23:59:59'
    DO
    INSERT INTO eventlog (event_type, log_time) VALUES (2, NOW());
# (3)创建一个 2025 年 4 月 3 日下午 5 点执行的事件
CREATE EVENT EventSpecificTime
    ON SCHEDULE AT '2025-04-03 17:00:00'
    DO
    INSERT INTO eventlog (event_type, log_time) VALUES (3, NOW());