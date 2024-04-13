select*
from students;

INSERT INTO students (first_name, last_name, birth_date)
VALUES 
    ('Marc', 'Benichou', '1998-11-02'),
    ('Yoan', 'Cohen', '2010-12-03'),
    ('Lea', 'Benichou', '1987-07-27'),
    ('Amelia', 'Dux', '1996-04-07'),
    ('David', 'Grez', '2003-06-14'),
    ('Omer', 'Simpson', '1980-10-03');
	
-- Update the birth dates for Lea Benichou and Marc Benichou
UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name = 'Lea' AND last_name = 'Benichou';

UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name = 'Marc' AND last_name = 'Benichou';

-- Change the last name of David from 'Grez' to 'Guez'
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

select*
from students;

--Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';


---Count how many students are in the table.
SELECT COUNT(*) AS total_students
FROM students;

--Count how many students were born after 1/01/2000.
SELECT COUNT(*) AS students_born_after_2000
FROM students
WHERE birth_date > '2000-01-01';

--Add a column to the student table called math_grade.
ALTER TABLE students
ADD COLUMN math_grade INT;

--Add 80 to the student which id is 1.
--Add 90 to the students which have ids of 2 or 4.
--Add 40 to the student which id is 6.
--Count how many students have a grade bigger than 83

UPDATE students
SET math_grade = 80
WHERE student_id = 1;

UPDATE students
SET math_grade = 90
WHERE student_id IN (2, 4);

UPDATE students
SET math_grade = 40
WHERE student_id = 6;

--Count how many students have a grade bigger than 83
SELECT COUNT(*) AS students_grade_bigger_than_83
FROM students
WHERE math_grade > 83; -- 2 students 

--Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT first_name, last_name, birth_date, 70
FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;

--
SELECT first_name, last_name, COUNT(math_grade) AS total_grades
FROM students
GROUP BY first_name, last_name;

--Find the sum of all the students grades.
SELECT SUM(math_grade) AS total_grades_sum
FROM students;


---Exercise 3 : Items And Customers




