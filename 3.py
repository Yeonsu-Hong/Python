# chapter 3. 프로그램 사용자로부터의 입력 그리고 코드의 반복

# 1. 입력 받는 함수 "input 함수"


# 앞서 배웠던 것을 복습하면 다음과 같다.

# adder2.py
def adder(num1, num2):
	return num1 + num2   #num1과 num2의 덧셈결과 반환

def main():
	print(adder(5, 3))   # adder 함수 호출 후 반환 되는 값 출력

main()   # 위의 main 함수 호출

# 결과값은 8이 출력

# 하지만 속칭 티카타카라고 하는 다음과 같은 과정이 필요하다.

#  컴퓨터 : 숫자를 입력하라 닝겐
#  사용자 : 100
#  컴퓨터 : 하나 더 입력해라 닝겐
#  사용자 : 20
#  컴퓨터 : 두숫자의 합은 120이다 닝겐.

# 이러한 식으로 사용자로부터 정보를 입력받아서 결과만 출력하는 것이 아닌 티카타카를 실행해주는 것이 input 함수이다.


# str = input("너 몇살이니?: ") # input 함수의 호출

# print(str)

# input함수는 입력된 내용이 하나의 문자열로 묶여서 반환된다는 사실을 주목할 필요가 있다.

# 파이썬은 수와 문자열을 구분한다.

num = "21" + "50"

print(num)

# 결과는 2150

# 연습문제 03 -1
# input함수는 프로그램 사용자가 입력한 내용을 문자열의 형태로 반환한다는 사실을 언급하였다.3이를 근거로 다음 실행 흐름을 보이는 예를 작성해보자.3

# 첫번째 입력 : 12
# 두번째 입력 : 34
# 두입력의 합 : 1234

first = input("첫번째 입력: ")

second = input("두번째 입력: ")

print("두입력의 합:", first + second)


# 2. 문자열을 숫자로 바꾸는 함수 eval

year = input("This year: ") # (1)

year = eval(year)  # (2)  # year에 저장된 내용을 산술 연산이 가능한 '수'로 바꾼다.
year = year + 1

print("Next year:", year)

# 결과 값 : this year : 2021, next year : 2022

year = eval(input("This year: "))  # 위에 (1),(2) 문장 한문장으로 표현


# 예시 : 윈의 넓이 계산

rad = eval(input("radius: "))
radius = 2.5
area = rad * rad * 3.14   # 원의 넓이 공식을 적용함
print(area)

# 2.5를 문자열에서 수로 반환했기 때문에 계산값이 나온 것이다.

# 결괏값: 19.625


# 연습문제 03 -2 
# eval 함수와 input 함수를 잘 묶어서 사용하면 프로그램 사용자로부터 산술 연산이 가능한 '수'를 입력 받을수 있다.

# 첫번째 입력 : 1.32
# 두번째 입력 : 5.01
# 두입력의 합 : 6.33

calc1 = eval(input("num1: "))
calc2 = eval(input("num2: "))
# num1: 1.32
# num2: 5.01

print(calc1 + calc2)


# 3. eval 함수의 위력 ( 그러나 위험하다. )
# eval 함수는 함수 호출시 전달되는 문자열의 내용을 분석해서 그 내용에 따라 무엇을 할지 결정하고 행동하기 때문에 강력한 함수이다.

result = eval(input("뭐든 넣어라 :"))
print(result)

# 문자열 안에 담겨 있는 수식을 계산하고 그 결과만 반환했다. eval은 evaluate의 앞 부분을 딴 것인데, 그 이름 처럼
# 전달된 문자열의 내용을 평가 및 해석해서 무엇을 할지 결정한다.

# 이 함수가 이렇게 범용적인데 왜 주의를 해야하는가?
# eval함수를 호출한 문장을 이용해서, 시키지 않은 일이 내 컴퓨터에서 실행되게끔 할수 있다. 즉, 보안에 취약하다.

def ret():     # ret라는 이름의 함수의 정의, 단순히 12를 반환하는 함수다.
	return 12

result = eval(input("뭐든 넣어요: "))
print(result)

# 뭐든 넣어요에 ret()을 넣으면 12가 print 된다.
# 어디에서도 이 ret함수를 호출하지 않았지만, 함수가 호출되었다.
# 프로그래머가 ret함수 호출을 명령하지 않았음에도 불구하고 ret 함수가 호출되었는데, 이 부분이 보안의 추약점으로 여겨지는 부분이다.
# 그래서 최대한 eval함수의 호출을 자제해야 한다.


# 4. for loop (for 루프)

for i in [0, 1, 2]:
	print(i)
	print("hi~")


# 출력 : 
# 0
# hi~
# 1
# hi~
# 2
# hi~

# 여기서 i는 변수이고 [0, 1, 2]는 반복의 횟수를 결정짓는 정보이다.
# print(i)와 print("hi~")는 for loop에 속하는 문장들이다.


# for i in [0, 1, 2]:

# 변수 i에 0을 넣어서 for에 속한 문장들을 실행해,
# 그리고 이어서 i에 1을 넣어서, 마지막으로 2를 넣어서 for에 속한 문장들을 각각 실행하라

# 위와 같은 의미라고 보면 된다.
# 또 다른 예시
for i in [1, 3 , 5]:
	print(i)
	print("magic")


# 1부터 10까지 더하기

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + i     # sum의 값을 i 만큼 증가시키는 문장

print(sum) 

# 연습문제 03 -3

# (1). 1, 3, 5, 7, 9의 합을 계산해서 그 결과를 출력하는 코드를 for loop를 기반으로 작성

sum = 0
for i in [1, 3, 5, 7, 9]:
	sum = sum + i

print(sum)

# (2). 1부터 10까지의 곱의 결과를 계산해서 그 결과를 출력하는 코드를 for loop를 기반으로 작성해보자.

sum = 1

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum * i

print(sum)


#(3). 구구단에서 7단 전부를 출력하는 코드를 for loop를 기반으로 작성해보자.

for i in [1, 2, 3, 4, 5, 6, 7, 8 ,9]:
	
	print("7 x", i, '=', 7 * i ) 

#(4). 구구단 7단을 전부 출력하되 거꾸로( 7 * 9 = 63부터) 출력하는 코드를 for loop를 기반으로 작성해보자.

for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:

	print("7 X", i, "=", 7 * i)


# 5. for ~ in (for loop)와 range의 조합

# 앞 chapter에서 했던 1부터 10까지의 합을 간단하게 하는 방법

sum = 0

for i in range (1, 11):    # for loop와 range의 조합
	sum = sum + i

print(sum)


# 55가 출력됨

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    vs.      range(1, 11)

# range(1, 11)
# -> for의 변수 i에 1부터 11 이전의 값까지 넣어서 반복을 진행하라는 의미이다.

# 1부터 100까지 더하기

sum = 0 

for i in range (1, 101):    
	sum = sum + i

print(sum)


#반복의 횟수를 세는 목적으로만 사용된다면, 변수의 값은 1이 아닌 0에서부터 시작하도록 코드를 작성하는 것이 좋다.

for i in range(0, 3):    # 3회 반복이 목적입니다. i에는 0, 1, 2가 들어감.
	print("happy")

# range(0, 3) 대신 range (1, 4) or range (2, 5)를 넣어도 된다. 다만 range()안의 첫번째 숫자를 0으로 두는것이 관례이다.
# 그래야 두번째 숫자를 보고도 몇번 반복한지 알수 있다.

for i in range(3):    # range(3)은 range(0, 3)과 같다. 즉, 3회 반복의 의미를 가짐

	print("happy")


# 변수를 기반으로 반복 횟수 설정

cnt = 12
for i in range(cnt):    #cnt만큼 반복
	print("I love coffee")


# 연습문제 03- 4

#(1). 안녕하세요를 총 5회 출력하는 코드를 for와 range 기반으로 작성

for i in range (0, 5):
	print("안녕하세요")

#(2). 구구단 7단 전부를 출력하는 코드를 for와 range 기반으로 작성

for i in range (0, 10):
	print("7 X", i, "=", 7 * i)


#(3). x^^y (x의 y제곱) ****** 난이도가 좀 높음 생각을 해보자
# 을 계산하는 함수를 for와 range 기반으로 만들어보자. ex) exp(2,3) 2^^3 = 2*2*2 = 8이 되어야 한다.

def exp(x, y):

	rlt = 1
	
	for i in range(y):

		rlt = rlt * x

	return rlt

exp (2, 4)


#(4). 반갑습니다를 여러번 출력하는 greet이라는 함수를 만들어 보자. 단
#  몇번 출력할지는 프로그램 사용자에게 묻고 입력받는 형태로 작성

def greet():
	num = eval(input("인사를 몇번 할까요? "))
	for i in range(num):

		print("반갑습니다.")

greet()
