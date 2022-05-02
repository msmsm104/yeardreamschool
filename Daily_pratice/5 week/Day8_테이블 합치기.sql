## Day 8 테이블 합치기


DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
	   number  INT,
       name	VARCHAR(20),
       type	VARCHAR(10)
);
INSERT INTO mypokemon (number, name, type)
VALUES (10, 'caterpie', 'bug'),
	   (25, 'pikachu', 'electric'),
       (26, 'raichu', 'electric'),
       (133, 'eevee', 'normal'),
       (152, 'chikoirita', 'grass');
CREATE TABLE ability (
	   number INT,
       height FLOAT,
       weight FLOAT,
       attack INT,
       defense INT,
       speed int
);
INSERT INTO ability (number, height, weight, attack, defense, speed)
VALUES (10, 0.3, 2.9, 30, 35, 45),
	   (25, 0.4, 6, 55, 40, 90),
       (125, 1.1, 30, 83, 57, 105),
	   (133, 0.3, 6.5, 55, 50, 55),
       (137, 0.8, 36.5, 60, 70, 40),
	   (152, 0.9, 6.4, 49, 65, 45),
       (153, 1.2, 15.8, 62, 80, 60),
       (172, 0.3, 2, 40, 15, 60),
       (470, 1, 25.5, 110, 130, 95);


SELECT * FROM mypokemon;
SELECT * FROM ability;

## join 키워드
### inner join - default
#### 교집합만 합침.

SELECT *
FROM mypokemon
INNER JOIN ability
ON mypokemon.number = ability.number;


## 한쪽을 기준으로 합치기
### left, right join

SELECT *
FROM mypokemon
LEFT JOIN ability
ON mypokemon.number = ability.number;


SELECT *
FROM mypokemon
RIGHT JOIN ability
ON mypokemon.number = ability.number;


## 다양한 방식으로 테이블 합치기
### outer(left + right join), cross, self join

#### outer join

SELECT *
FROM mypokemon
LEFT JOIN ability
ON mypokemon.number = ability.number
UNION
SELECT *
FROM mypokemon
RIGHT JOIN ability
ON mypokemon.number = ability.number;


#### cross join 각각 모두 합친다.
SELECT *
FROM mypokemon
CROSS JOIN ability;



#### self join: 같은 테이블 끼리의 inner join을 의미

SELECT *
FROM mypokemon AS t1
INNER JOIN mypokemon AS t2
ON t1.number = t2.number;





## [실습] 다양한 방식으로 합쳐보자!!
/*
MISSION (1)
포켓몬 테이블과 능력치 테이블을 합쳐서 포켓몬 이름, 공격력, 방어력을 한번에 가져와 주세요.
이 때, 포켓몬 테이블에 있는 모든 포켓몬의 데이터를 가져와 주세요. 만약, 포켓몬의 능력치 데이터를 구할 수 없다면, NULL을 가져와도 좋습니다.
*/

SELECT name, attack, defense
FROM mypokemon
LEFT JOIN ability
ON mypokemon.number = ability.number;




/*
MISSION (2)
포켓몬 테이블과 능력치 테이블을 합쳐서 포켓몬 번호와 이름을 한번에 가져와 주세요.
이 때, 능력치 테이블에 있는 모든 포켓몬의 데이터를 가져와 주세요. 만약, 포켓몬의 이름 데이터를 구할 수 없다면, NULL을 가져와도 좋습니다.

*/

SELECT ability.number, name
FROM mypokemon
RIGHT JOIN ability
ON mypokemon.number = ability.number;

