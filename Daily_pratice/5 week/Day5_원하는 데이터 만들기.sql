
## 시간관련 함수!
SELECT NOW(), CURRENT_DATE(), CURRENT_TIME();


SELECT NOW(), YEAR(NOW()), MONTH(NOW()), MONTHNAME(NOW());


SELECT NOW(), DAYNAME(NOW()), DAYOFMONTH(NOW()), DAYOFWEEK(NOW()), WEEK(NOW());

SELECT NOW(), HOUR(NOW()), MINUTE(NOW()), SECOND(NOW());

SELECT DATE_FORMAT(NOW(), '%Y년 %m월 %d일 %h시') AS formatted_date;

SELECT DATEDIFF() AS DATE_DIFF,
		TIMEDIFF() AS TIME_DIFF;
        
## [실습] 데이터를 요청 대로 만들어보자.

DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
use pokemon;
create table mypokemon (
		number INT,
        name VARCHAR(20),
        type VARCHAR(10),
        attack INT,
        defense INT,
        capture_date DATE
);

INSERT INTO mypokemon (number, name, type, attack, defense, capture_date)
VALUES (10, 'caterpie', 'bug', 30, 35, '2019-10-14'),
	   (25, 'pikachu', 'electric', 55, 40, '2018-11-04'),
	   (26, 'raichu', 'electric', 90, 55, '2019-05-28'),
      	  (125, 'electabuzz', 'electric', 83, 57, '2020-12-29'),
	   (133, 'eevee', 'normal', 55, 50, '2021-10-03'),
     	   (137, 'porygon', 'normal', 60, 70, '2021-01-16'),
	   (152, 'chikoirita', 'grass', 49, 65, '2020-03-05'),
     	  (153, 'bayleef', 'grass', 62, 80, '2022-01-01');

SELECT * FROM mypokemon;

##1. 포켓몬 테이블에서 포켓몬의 이름과 이름의 글자 수를 이름의 글자 수로 정렬해서 가져와 주세요.
SELECT name, length(name) AS len_nm
FROM mypokemon
ORDER BY len_nm;


##2. 방어력 순위를 보여주는 컬럼을 새로 만들어서 'defense_rank'라는 별명으로 가져와라.
## 이때 이름도 함께 가져와라.

SELECT name, RANK() OVER (ORDER BY defense DESC) AS defense_rank
FROM mypokemon;

##3. 포켓몬 테이블에서 포켓몬을 포획한 지 기준 날짜까지 며칠이 지났는 지를 ‘days’라는 별명으로 가져와 주세요. 이 때, 포켓몬의 이름도 함께 가져와 주세요.
## 조건: 기준 날짜는 2022년 2월 14일입니다

SELECT name, DATEDIFF('2022-02-14', capture_date) AS days
FROM mypokemon;