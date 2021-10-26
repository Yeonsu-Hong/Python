#  chapter 10. 함수에 대한 추가적인 내용


# 1. 함수 복습 (2장 내용)


# 아무 값도 전달받지 않는 함수
# 값을 전달받는 함수
# 값을 반환하는 함수 (return 명령을 갖는 함수)

def greet():
	print("Hi")
	print("Python")


greet()


# 값을 전달받으면서 값을 반환도 하는 함수

def adder(n1, n2):    # 전달되는 값을 매개변수 n1, n2로 받은
	r = n1 + n2
	return r   # r에 저장된 값을 반환


print(adder(3, 4))

for i in (1, 3, 5, 7, 9):
	print(i, end = ' ')   # 두번째로 전달한 end = ' '의 정체는? 줄바꿈 대신에 뒤쪽에 공백


# 2. 이름을 지정해서 값 전달

def who_are_you(name, age):   # name과 age를 가리켜 매개변수라 한다.
	print("이름:", name)
	print("나이:", age)

who_are_you("홍연수", 12)   # 이름을 첫 번째 값으로 나이는 두 번째 값으로 전달

# 만약에 값의 전달 순서가 뒤틀리면 다음과 같이 엉뚱한 결과를 보게 된다.
who_are_you(22, "홍연수") 

# 그런데 필요하다면, 그리고 매개변수의 이름을 알고 있다면 다음과 같이 함수를 호출할 수도 있다.
who_are_you(name = '홍연수', age = 22)

# 이는 매개 변수 name에 "홍연수", 매개변수 age에 22를 지정해서 전달하는 방법이다. 이렇듯 매개변수의 이름을 지정해서 값을 전달하면 전달 순서는 상관이 없어진다.
# 즉. 다음과 같이 이름과 나이 경로를 전달하는 순서가 바뀌어도 된다.

who_are_you(age = 22, name ="홍연수")

# 매개변수 sep
# print 함수의 매개변수 sep에 전달된 내용은 출력 내용들 사이사이에 출력이 되어 출력 내용을 구분하는 용도로 사용이 된다.

print(1, 2, 3, sep =',') # 출력 내용 사이사이에 ','을 출력

# 물론 다음과 같이 매개 변수 sep와 end에 값을 동시에 전달할 수도 있다.

print(1, 2, 3, sep= '_', end = ' 우주로')


# 3. default 값

# 함수를 만들때 매개 변수에 다음과 같이 '디폴트 값'이라는 것을 지정해 둘 수 있다.

def who_are_you(name, age = 0):       # age의 디폴트 값은 0
	print("이름:", name)
	print("나이:", age)


# def who_are_you(name, age = 0):   # age에 디폴트 값 0이 지정되었다.

# age를 채울 값이 전달되지 않으면 0을 대신 전달해주겠다.

who_are_you("오케이")    # 디폴트 값으로 나이가 0으로 출력된다. 직접 입력하지 않으면

who_are_you("노우", 35)


# def who_are_you(age = 0, name):   # 디폴트 값이 있는 매개변수의 위치 오류
	# print("이름:", name)
	# print("나이:", age)

#  오류가 생긴다.

# def who_are_you(name, age = 0)    # OK

# def who_are_you(age = 0, name )    # Error

# 함수를 만들때 디폴트 값을 갖는 매개변수와 갖지 않는 매개 변수가 함께 존재한다면, 반드시 디폴트 값을 갖는 매개변수가 뒤에 와야 한다.

def have_default_value(n1, n2, n3 = "df1", n4 = "df2"):
	print(n1, n2, n3 ,n4)

have_default_value(1, 2, 3, 4)

have_default_value(1, 2)   # default값이 3 4 위치에서 출력된다. 아무것도 넣지 않았는데....



# 4. 함수의 매개변수 참조 관계

def func(s):     # 전달되는 값이 list라고 가정하고 정의한 함수
	s[0] = 0     # list의 첫번째 값을 0으로 수정
	s[-1] = 0    # list의 마지막 값을 0으로 수정


st = [1, 2, 3]
func(st)

print(st)        # 함수 호출 후에 st가 [1, 2, 3]에서 [0, 2, 0]으로 바뀌었다.

# 파이썬은 매개 변수를 위해 별도의 메모리 공간을 할당하지 않는다. 대신에 다음과 같이 메모리 공간에 하나의 이름을 더 붇이는 방식으로
# "매개변수로 전달되는 값"을 처리한다.
# 쉽게 얘기해서 func함수가 호출되면 변수 st에 이름이 하나 더 붙게 된다.
# 그래서 함수 내에서 다음과 같이 list의 값을 수정하면, 변수 st에 담긴 list값이 실제로 바뀌게 되는 것이다.















 

