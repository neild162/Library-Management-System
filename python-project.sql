create database db;
use db;
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
create table member(Name varchar(20) primary key, Password varchar(20));
INSERT INTO member(Name,Password) VALUES ('neil','neil');

drop table member;
select * from member;