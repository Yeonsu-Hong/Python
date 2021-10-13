# chapter 4. int형 데이터, float형 데이터

# 1. 파이썬에서의 실수형과 정수형 데이터

data1 = 2     #정수 2를 변수 data1에 저장
data2 = 2.4	   # 실수 2.4를 변수 data2에 저장

#파이썬의 입장에서 정수 저장은 문제가 없으나, 실수의 저장은 문제가 생긴다.

# 2.1 이상 2.2이하의 모든 실수를 저장한다면, 2.1 ~ 2.2 사이에 존재하는 실수의 수는 무한대이기 때문이다.

#파이썬은 실수를 정수만큼 잘 표현하지 못한다.

num = 2
print(num)


num1 = 1.0000000000000000000001
num2 = 3.1

print( num1 + num2 )

# 결괏값 : 4.1

# 위의 예에서 num2에 저장된 값은 정확히 3.1이 아니다. 3.1에 가까운 값일 뿐이다.

# 다음과 같은 특성을 인지해야 한다.



# 파이썬이 '정수를 표현 및 저장하는 방법'과 '실수를 표현 및 저장하는 방법'은 다르다.
# 파이썬은 정수를 아주 정확히 표현하고 저장할 수 있다.
# 파이썬은 실수를 오차없이 표현하고 저장하지 못한다. 실수에는 약간의 오차가 있다.

#이러한 실수의 표현 및 저장의 한계는 파이썬의 능력 부족이 아니라 컴퓨터가 갖는 한계이다. 다른 언어에서도 마찬가지이다.

# 2. int형과 float형을 대상하는 기본적인 산술 연산

# int형 data : 정수형 데이터
# float형 data : 실수형 데이터

type(3) 
# REPL에서 출력이 되지 않는다. anaconda prompt에서는 출력이 된다.
# 출력 : <<class 'int'>>
type(3.1)
# 출력 : <<class 'float'>>
type(3.0)
# 출력 : <<class 'float'>>


# 기본적인 산술 정리!! 
# ( 연산자 정리!! )

# + 덧셈
# - 뺄셈
# * 곱셈
# ** 거듭제곱
# / 실수형 나눗셈
#  // 정수형 나눗셈
#  % 나머지가 얼마??


# 예시

print(3**2)

# 실수형 나눗셈
print(5/2)

# 정수형 나눗셈 
print(5//2)
# 결괏값 : 2 ; 나눗셈의 몫을 계산

print(5 % 2)
# 결괏값 : 1 ; 나눗셈의 나머지 계산




# 3. 변환 ( int형 <-> float형 )

num = 10
num = float (num)    # num의 값을 float 형으로
type(num)

# 결괏값 : <class 'float'> 정수형을 실수형으로 

num = float("3.14")
type(num)   # 아래의 출력 결과는 num에 저장된 값이 float형임을 의미함

# 결괏값 : <class 'float'> 정수형을 실수형으로 : 위의 결괏값과 동일하다
 
# eval 함수를 float함수 호출 형태로 전환

height = eval(input("키 정보 입력: "))   # eval 함수 호출
print(height)


height = float(input("키 정보 입력: "))   # float 함수 호출 (결과는 위와 똑같다.)
print(height)


num = int(3.14)     # 3.14를 int형으로 변환
print(num)

# 소숫점이 사라진 결괏값이 출력


height = eval(input("키 정보 cm 단위로 입력: "))  #eval 함수 호출
print(height)


# int 함수를 호출하는 형태로 바꾸기

height = int(input("키 정보 cm 단위로 입력: "))    # int 함수 호출
print(height)

# 여기서는 소숫점을 입력하면 에러가 발생한다.



# 4. 복합 대입 연산자

num = 10

num = num + 1   # num의 값을 1 증가
print(num)

# 11 출력

num = 10
num += 1   # num = num + 1을 줄인 표현

print(num)

# num = num + 1    vs    num += 1

# num = num - 1    vs    num -= 1

# num = num * 3    vs    num *= 3

# 5. 소괄호 계산

print(3 + 4 / 2)

print((3 + 4) / 2) 

# 결과가 다르게 나온다.




# 연습문제 4-1
# (1). 정수형 나눗셈의 결과를 출력하는 함수를 만들어 보자.

def int_div(n1, n2):

	print("몫:", n1 // n2)
	print("나머지:", n1 % n2)

int_div(5, 2)


# (2). 두수 사이의 모든 정수의 합을 구하는 코드를 작성하되 함수 형태로 정의해서
# 다음의 실행 결과를 보이도록 해보자. (함수 이름이 bet_sum이라고 가정.)

def bet_sum(n1, n2):
	sum = 0
	for i in range (n1+1, n2):
		sum += i
		print(sum)

bet_sum(2, 5)

# bet_sum(1, 5)




