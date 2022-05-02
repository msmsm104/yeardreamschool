DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
	number  int,
       name	varchar(20),
       type	varchar(10),
       attack int,
       defense int
);
INSERT INTO mypokemon (number, name, type, attack, defense)
VALUES (10, 'caterpie', 'bug', 30, 35),
	   (25, 'pikachu', 'electric', 55, 40),
	   (26, 'raichu', 'electric', 90, 55),
      	  (125, 'electabuzz', 'electric', 83, 57),
	   (133, 'eevee', 'normal', 55, 50),
         (137, 'porygon', 'normal', 60, 70),
	   (152, 'chikoirita', 'grass', 49, 65),
         (153, 'bayleef', 'grass', 62, 80),
         (172, 'pichu', 'electric', 40, 15),
         (470, 'leafeon', 'grass', 110, 130);

## day7 규칙만들기
use pokemon;
## 조건만들기

## 사용예제

SELECT * FROM mypokemon;

## IF 사용예제
SELECT name, IF(attack >= 60, 'strong', 'weak') AS attack_class
FROM mypokemon;

## IFNULL 사용예제
SELECT name, IFNULL(name, 'unknown') AS full_name
FROM mypokemon;



## 여러 조건 만들기

### CASE 문법

SELECT name,
CASE
	WHEN attack >= 100 THEN 'very strong'
    WHEN attack >= 60 THEN 'strong'
    ELSE 'weak'
END AS attack_class
FROM mypokemon;

SELECT name, type,
CASE type
	WHEN 'bug' THEN 'grass'
    WHEN 'electric' THEN 'water'
    WHEN 'grass' THEN 'bug'
    ELSE 'unknown'
END AS rival_type
FROM mypokemon;



## 함수만들기
### 함수를 만드는 쿼리
SET GLOBAL log_bin_trust_function_creators=1;





## 실습예제

/*
MISSION
공격력과 방어력의 합이 120보다 크면 ‘very strong’, 90보다 크면 ‘strong’,
모두 해당 되지 않으면 ‘not strong’를 반환하는 함수 ‘isStrong’을 만들고 사용해주세요.
조건1: attack과 defense를 입력값으로 사용하세요.
조건2: 결과값 데이터 타입은 VARCHAR(20)로 해주세요.

*/

DELIMITER //

CREATE FUNCTION isStrong(attack int, defense int)
		returns VARCHAR(20)
begin	
		DECLARE a INT;
        DECLARE b int;
        DECLARE isstrong VARCHAR(20);
        set a = attack;
        set b = defense;
        select 
        CASE
			WHEN a+b > 120 THEN 'very strong'
			WHEN a+b > 90 THEN 'strong'
            ELSE 'not strong'
		END INTO isstrong;
            
        return isstrong;
END

//
DELIMITER ;



SELECT name, isStrong(attack, defense) AS isStrong
FROM mypokemon;
