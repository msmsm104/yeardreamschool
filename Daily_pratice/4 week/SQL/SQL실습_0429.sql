SHOW DATABASES;
USE university;

SHOW TABLES;

SELECT * FROM instructor;

## Q.1 'Kim'의 dept_name와 salary를 보여주세요.
SELECT dept_name, salary 
FROM instructor
WHERE name = 'Kim';

## Q.2 dept_name이 Physics인 사람의 name을 보여주세요.
SELECT name
FROM instructor
WHERE dept_name = 'Physics';

## Q.3 salary가 65000을 넘는 모든 사람의 이름을 출력해주세요.
SELECT name
FROM instructor
WHERE salary > 65000;

## Q.4 Finance department에 속한 사람중에 salary가 70000이 넘는 사람의 이름을 출력해주세요.
SELECT name
FROM instructor
WHERE dept_name = 'Finance' AND salary > 70000;


## Q.5 Comp. Sci. department에 속한 사람들의 평균 연봉을 출력해주세요.
SELECT avg(salary) AS avg_salary
FROM instructor
WHERE dept_name = 'Comp. Sci.';


## Q.6 각 department 별로 가장 높은 연봉을 받은 사람의 이름을 출력해주세요.
## subquery 활용하기

SELECT name, dept_name, salary
FROM instructor
WHERE salary 
IN (SELECT max(salary) as max_salary
FROM instructor
GROUP BY dept_name);