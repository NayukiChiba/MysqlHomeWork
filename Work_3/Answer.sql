use yggl;
desc employees;
desc departments;
insert into departments(departmentid, departmentname, note)
values
    ('2', '人力资源部', NULL),
    ('3', '经理办公室', NULL),
    ('4', '研发部', NULL),
    ('5', '市场部', NULL),
    ('1', '财务部', NULL);
insert into Employees (EmployeeID, Name, Education, Birthday, Sex, WorkYear, Address, PhoneNumber, DepartmentID)
values
    ('000001', '王林', '大专', '1966-01-23', 1, 8, '中山路32-1-508', '83355668', 2),
    ('010008', '伍春华', '本科', '1976-03-28', 1, 3, '北京东路100-2', '83321321', 1),
    ('020010', '王向荣', '硕士', '1982-12-09', 1, 2, '四牌楼10-10-108', '83792361', 1),
    ('020018', '李丽', '大专', '1960-07-30', 0, 6, '中山东路102-2', '83413301', 1),
    ('102201', '刘明', '本科', '1972-10-18', 1, 3, '虎圈路100-2', '83606608', 5),
    ('102208', '朱骏', '硕士', '1965-09-28', 1, 2, '牌楼巷5-3-106', '84708817', 5);

INSERT INTO salary (EmployeeID, InCome, OutCome)
VALUES
    ('000001', 2100.8, 123.09),
    ('010008', 1582.62, 88.03),
    ('020010', 2860, 598),
    ('020018', 2347.68, 180),
    ('102201', 2569.88, 185.65),
    ('102208', 1980, 100);


update salary set Income=2890 where EmployeeID='102201';

update salary set Income=Income+100;

delete from salary where EmployeeID='102201';

delete from salary where Income>=2500;

select * from salary;
