create table customer(
customer_id serial primary key,
first_name varchar(50) not null,
last_name varchar(100) not null
);


create table customer_profile(
profile_id serial primary key,
isLoggedIn boolean default False,
customer_id integer not null,
CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);


insert into customer(first_name, last_name)
values ('John','Doe'),
('Jerome','Lalu'),
('Lea', 'Rive');

insert into customer_profile(profile_id,isLoggedIn,customer_id)
values ((select customer_id from customer where first_name = 'John'),True,
        (select customer_id from customer where first_name = 'John'));

insert into customer_profile(profile_id,isLoggedIn,customer_id)
values ((select customer_id from customer where first_name = 'Jerome'),False,
        (select customer_id from customer where first_name = 'Jerome'));

--The first_name of the LoggedIn customers
select t1.first_name
from customer as t1 join customer_profile as t2 on t1.customer_id = t2.customer_id
where t2.isLoggedIn is True;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select t1.first_name, t2.isLoggedIn
from customer as t1 left join customer_profile as t2 on t1.customer_id = t2.customer_id;

--The number of customers that are not LoggedIn
select count(*)
from customer as t1 left join customer_profile as t2 on t1.customer_id = t2.customer_id
where  t2.isLoggedIn is FALSE or t2.isLoggedIn is Null;

--Part II:
--Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

create table book(
book_id SERIAL PRIMARY KEY,
title varchar(50) NOT NULL,
author varchar(100) NOT NULL
);

insert into book(title,author)
values ('Alice In Wonderland', 'Lewis Carroll'),
     ('Harry Potter', 'J.K Rowling'),
     ('To kill a mockingbird', 'Harper Lee');

create table Student(
student_id SERIAL PRIMARY KEY,
name varchar(100) NOT NULL UNIQUE,
age int check (age <= 15)
);

insert into Student(name,age)
values ('John', 12),
       ('Lera', 11),
       ('Patrick', 10),
       ('Bob', 14);


create table library(
book_fk_id INTEGER not null ,
student_fk_id  INTEGER not null,
borrowed_date date,
PRIMARY KEY (book_fk_id, student_fk_id),
foreign key (book_fk_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (book_fk_id) REFERENCES Student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM book where title = 'Alice In Wonderland'),
(SELECT student_id FROM Student where name = 'John'), '15/02/2022');

INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM book where title = 'To kill a mockingbird'),
(SELECT student_id FROM Student where name = 'Bob'), '03/03/2021');

INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM book where title = 'Alice In Wonderland'),
(SELECT student_id FROM Student where name = 'Lera'), '23/05/2021');

INSERT into library(book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM book where title = 'Harry Potter'),
(SELECT student_id FROM Student where name = 'Bob'), '12/08/2021');

--Select all the columns from the junction table
select*
from library;

--Select the name of the student and the title of the borrowed books
select t3.name,t2.title
from library as t1  join book as t2 on t1.book_fk_id = t2.book_id
                    join Student as t3 on t1.student_fk_id=t3.student_id;
--
-- Select the average age of the children, that borrowed the book Alice in Wonderland
select avg(t3.age) as average_age
from library as t1  join book as t2 on t1.book_fk_id = t2.book_id
                    join Student as t3 on t1.student_fk_id=t3.student_id
where t2.title = 'Alice In Wonderland';

--Delete a student from the Student table, what happened in the junction table ?

--It will cause deleting the student from library with the same id as in students table.
