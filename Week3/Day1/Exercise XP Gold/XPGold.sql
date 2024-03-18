-- -- Database: bootcamp

-- -- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.936'
--     LC_CTYPE = 'Russian_Russia.936'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- create table students(
-- student_id serial primary key,
-- first_name varchar(50) not null,
-- last_name varchar(100) not null,
-- birth_date date not null
-- );


-- insert into students(first_name,last_name,birth_date)
-- values ('Marc','Benichou','02/11/1998'),
-- ('Yoan','Cohen','03/12/2010'),
-- ('Lea','Benichou','27/07/1987'),
-- ('Amelia','Dux','07/04/1996'),
-- ('David','Grez','14/06/2003'),
-- ('Omer','Simpson','03/10/1980');

-- insert into students(first_name,last_name,birth_date)
-- values ('Mikhail','Tiurin','09/07/1999')

-- select*
-- from students

-- select first_name, last_name
-- from students

-- select first_name, last_name
-- from students
-- where student_id = 2;

-- select first_name, last_name
-- from students
-- where last_name  = 'Benichou' and first_name = 'Marc';


-- select first_name, last_name
-- from students
-- where last_name  = 'Benichou' or first_name = 'Marc';


-- select first_name, last_name
-- from students
-- where first_name ilike '%a%';

-- select first_name, last_name
-- from students
-- where first_name ilike 'a%';


-- select first_name, last_name
-- from students
-- where first_name ilike '%a';


-- insert into students(first_name,last_name,birth_date)
-- values ('Antonio','Merkaz','09/07/1995')

-- select first_name, last_name
-- from students
-- where first_name ilike '_%a%';


-- select first_name, last_name
-- from students
-- where student_id = 1 or student_id = 3;

-- select first_name, last_name
-- from students
-- where birth_date >= '01/01/2000';

-- select *
-- from students
-- order by last_name
-- limit 4;
--
-- select*
-- from students
-- order by birth_date desc
-- limit 1;
--
-- select*
-- from students
-- limit 3
-- offset 2;

