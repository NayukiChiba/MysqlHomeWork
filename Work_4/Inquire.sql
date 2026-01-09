use yggl;
# (1)
# 查询每个员工的所有数据,查询Departments表和Salary表的所有数据
SELECT * FROM Employees;
SELECT * FROM Departments;
SELECT * FROM Salary;

# (2)
# 查询每个员工的姓名、地址和电话号码
SELECT Name, Address, PhoneNumber FROM Employees;

# (3)
# 查询Employees表中的部门号和性别,消除重复行
SELECT DISTINCT DepartmentID, Sex FROM Employees;

# (4)
# 查询EmployeeID为000001的员工地址和电话
SELECT Address, PhoneNumber FROM Employees WHERE EmployeeID = '000001';

# (5)
# 查询月收入高于2000元的员工号、姓名和收入
SELECT e.EmployeeID, e.Name, s.InCome
FROM Employees e
    JOIN Salary s ON e.EmployeeID = s.EmployeeID
WHERE s.InCome > 2000;

# (6)
# 查询1970年以后出生的员工的姓名和住址
SELECT Name, Address FROM Employees WHERE Birthday > '1970-12-31';

# (7)
# 查询财务部的所有员工的员工号和姓名
SELECT e.EmployeeID, e.Name
FROM Employees e
    JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = '财务部';

# (8)
# 查询女员工的地址和电话(标题设为“地址”和“电话”)
SELECT Address AS 地址, PhoneNumber AS 电话
FROM Employees
WHERE Sex = '0';

# (9)
# 查询员工的姓名和性别(1显示“男”,0显示“女”)
SELECT Name,
    CASE
       WHEN Sex = '1' THEN '男'
       WHEN Sex = '0' THEN '女'
       END AS 性别
FROM Employees;

# (10)
# 查询员工的姓名、住址和收入水平分类
SELECT e.Name, e.Address,
   CASE
       WHEN s.InCome < 2000 THEN '低收入'
       WHEN s.InCome BETWEEN 2000 AND 3000 THEN '中等收入'
       ELSE '高收入'
       END AS 收入水平
FROM Employees e
    JOIN Salary s ON e.EmployeeID = s.EmployeeID;

# (11)
# 计算每个员工的实际收入
SELECT e.EmployeeID, e.Name, (s.InCome - s.OutCome) AS 实际收入
FROM Employees e
    JOIN Salary s ON e.EmployeeID = s.EmployeeID;

# (12)
# 获取员工人数
SELECT COUNT(*) AS 员工人数 FROM Employees;

# (13)
# 计算月收入的平均值
SELECT AVG(InCome) AS 平均月收入 FROM Salary;

# (14)
# 计算所有员工的总收入
SELECT SUM(InCome) AS 总收入 FROM Salary;

# (15)
# 查询财务部员工的最高和最低实际收入
SELECT MAX(s.InCome - s.OutCome) AS 最高实际收入, MIN(s.InCome - s.OutCome) AS 最低实际收入
FROM Salary s
    JOIN Employees e ON s.EmployeeID = e.EmployeeID
WHERE e.DepartmentID = '1';

# (16)
# 查询姓“王”的员工的姓名和部门号
SELECT Name, DepartmentID FROM Employees WHERE Name LIKE '王%';

# (17)
# 查询员工号倒数第二位为0的员工
SELECT EmployeeID, Name FROM Employees WHERE EmployeeID LIKE '%0_';

# (18)
# 查询地址含“中山”的员工的ID和部门号
SELECT EmployeeID, DepartmentID FROM Employees WHERE Address LIKE '%中山%';

# (19)
# 查询收入在2000~3000元的员工的ID和姓名
SELECT e.EmployeeID, e.Name
FROM Employees e
    JOIN Salary s ON e.EmployeeID = s.EmployeeID
WHERE s.InCome BETWEEN 2000 AND 3000;

# (20)
# 查询部门号为1或3的员工的ID和姓名
SELECT EmployeeID, Name FROM Employees WHERE DepartmentID IN ('1', '3');