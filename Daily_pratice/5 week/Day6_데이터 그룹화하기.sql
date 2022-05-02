## day 6. 데이터 그룹화하

DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
	number  int,
       name	varchar(20),
       type	varchar(10),
       height	float,
       weight	float
);
INSERT INTO mypokemon (number, name, type, height, weight)
VALUES (10, 'caterpie', 'bug', 0.3, 2.9),
	   (25, 'pikachu', 'electric', 0.4, 6),
	   (26, 'raichu', 'electric', 0.8, 30),
          (125, 'electabuzz', 'electric', 1.1, 30),
	   (133, 'eevee', 'normal', 0.3, 6.5),
          (137, 'porygon', 'normal', 0.8, 36.5),
	   (152, 'chikoirita', 'grass', 0.9, 6.4),
          (153, 'bayleef', 'grass', 1.2, 15.8),
          (172, 'pichu', 'electric', 0.3, 2),
          (470, 'leafeon', 'grass', 1, 25.5); 
##---------------------------------------------------------          
SELECT type 
FROM mypokemon
GROUP BY type;

## 그룹에 조건 주기 - HAVING (GROUP의 조건을 지정)

## 그룹 함수
## 예제

SELECT type, COUNT(*), COUNT(1), AVG(height), MAX(weight)
FROM mypokemon
GROUP BY type
HAVING COUNT(1) > 1; 



## 쿼리의 실행순서 알아보기

## FROM - WHERE - GROUP BY - HAVING -  SELECT - ORDER BY

SELECT type, COUNT(1), MAX(weight) #5
FROM mypokemon #1
WHERE name LIKE '%a%' #2
GROUP BY type #3
HAVING MAX(height) > 1 #4
ORDER BY 3; #6 - MAX weight를 기준으로 정렬




## 데이터를 그룹화해서 통계를 내보자.(실습)

##1. 포켓몬 테이블에서 이름(name)의 길이가 5보다 큰 포켓몬들을 타입(type)을 기준으로 그룹화하고, 몸무게(weight)의 평균이 20 이상인 그룹의 타입과, 몸무게의 평균을 가져와 주세요. 이 때, 결과는 몸무게의 평균을 내림차순으로 정렬해 주세요.

SELECT type, AVG(weight) AS avg_weight
FROM mypokemon
WHERE length(name) > 5
GROUP BY type
HAVING AVG(weight) >= 20
ORDER BY 2 DESC;

##2. 포켓몬 테이블에서 번호(number)가 200보다 작은 포켓몬들을 타입(type)을 기준으로 그룹화한 후에, 몸무게(weight)의 최댓값이 10보다 크거나 같고 최솟값은 2보다 크거나 같은 그룹의
## 타입, 키(height)의 최솟값, 최댓값을 가져와 주세요. 이 때, 결과는 키의 최솟값의 내림차순으로 정렬해 주시고,  만약 키의 최솟값이 같다면 키의 최댓값의 내림차순으로 정렬해주세요.

SELECT type, MAX(height), MIN(height), COUNT(1)
FROM mypokemon
WHERE number < 200
GROUP BY type
HAVING MAX(weight) >= 10 AND MIN(weight) >= 2
ORDER BY 3 DESC, 2 DESC;