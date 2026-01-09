# 创建数据库
CREATE DATABASE IF NOT EXISTS YGGL;
use YGGL;

create table Departments(
    DepartmentID char(3) not null primary key ,
    DepartmentName char(20) not null,
    Note text null
);



create table Employees(
    EmployeeID char(6) not null primary key ,
    Name char(10) not null ,
    Education char(4) not null ,
    Birthday date not null ,
    Sex char(1) not null ,
    WorkYear tinyint(1) null,
    Address varchar(20) null ,
    PhoneNumber char(12) null,
    DepartmentID char(3) not null,
    foreign key (DepartmentID) references Departments(DepartmentID)
);

create table Salary(
    EmployeeID char(6) not null primary key ,
    Income float(8) not null ,
    Outcome float(8) not null,
    foreign key (EmployeeID) references Employees(EmployeeID)
);

create table Employees0 like Employees;

show tables;
drop table Employees0;

