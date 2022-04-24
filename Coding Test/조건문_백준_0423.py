#Conditional Statement

##1. 두 수 비교하기
> - 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

##2. 시험 성적
> - 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

##3. 윤년
> - 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

> - 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

> - 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.


year = int(input())

forth_num = year % 4 == 0
hund_num = year % 100 != 0
four_hund_num = year % 400 == 0

cond = (forth_num and hund_num) or (four_hund_num)

if cond:
    print(1)
else:
    print(0)

##4. 사분면 고르기

x = int(input())
y = int(input())

qd_1_cond = (x > 0) and (y > 0)
qd_2_cond = (x < 0) and (y > 0)
qd_3_cond = (x < 0) and (y < 0)
qd_4_cond = (x > 0) and (y < 0)

if qd_1_cond:
    print(1)
elif qd_2_cond:
    print(2)
elif qd_3_cond:
    print(3)
else:
    print(4)


##5. 알람 시계

H, M = map(int, input().split())

to_min = H * 60 + M
sub_45 = to_min - 45

if sub_45 < 0:
    sub_45 = 24 * 60 + sub_45

print(sub_45 // 60, sub_45 % 60)

## 6. 오븐시계

A, B = map(int, input().split())
C = int(input())

to_min = A * 60 + B
end_time = to_min + C

if end_time >= 24*60:
    end_time = end_time - 24*60

print(end_time // 60, end_time % 60)

##7. 주사위 세개

lst = [1,2,3]
max(lst)

a, b, c = map(int, input().split())

lst = [a, b, c]

if (a == b) and (b == c):
    print(a * 1_000 + 10_000)
elif (a != b) and (a != c) and (b != c):
    print(max(lst) * 100)
else:
    if (a == b) or (a == c):
        print(a * 100 + 1_000)
    else:
        print(b * 100 + 1_000)




