# chapter 13. 클래스와 객체

# 1. 전역 변수와 지역 변수

# 함수 안에 선언되는 변수 : 지역변수
# 함수 밖에 선언되는 변수 : 전역변수

# 다음 예에서 보이듯이, 함수 안에 선언된 변수는 함수 안에서만 접근이 가능하다. 물론
# 이는 매개 변수도 마찬가지이다. 매개변수도 함수 안에서만 접근 가능하다. 즉 지역 변수의 범주에 매개 변수도 포함이 된다.


def func(n):     # 매개 변수 n도 지역 변수 범주에 포함된다. (지역 변수의 일종이다.)
	lv = n + 1   # 지역 변수 lv의 선언, 그리고 매개 변수 n에 접근
	print(lv)	 # 지역변수 lv에 접근

func(12)


def func(n):
	lv = n + 1   # 지역변수 lv의 선언 
	print(lv)


# print(lv)   # 함수 밖에서 지역변수 lv에 접근, 따라서 오류!



# 지역 변수는 함수 내에서 만들어졌다가 함수를 벗어나면 사라지는 변수이다.


cnt = 100    # 함수 밖에서 선언된 전역변수 cnt
cnt += 1     # 전역 변수 cnt에 접근!

def func():
	print(cnt)    # 함수 내에서 전역변수 cnt에 접근!

func()

# 위의 예에서는 func 함수 내에서 전역변수 cnt에 저장된 값을 출력하였다. 이렇듯 함수 내에서는 얼마든지 함수 밖에 선언된 변수에 접근할 수 있다.

cnt = 100    # 전역변수 cnt 선언

def func():
	cnt = 0    # 어떤 의미로 해석이 될까?
	print(cnt)     # 어떤 cnt의 값을 출력할까??

func()   # 0 출력

print(cnt)     # 전역 변수 cnt의 값 출력 100 출력

# 전역 변수 cnt의 값을 0으로 수정하는 결과로 이어지지 않고 다음 결과로 이어진다.

# 지역 변수 cnt를 선언하고 여기에 0을 저장한다. 변수 하나를 더 만든 셈이다.
# 전역 변수와 동일한 이름의 지역변수가 만들어지면 함수내에서는 지역변수에만 접근하게 된다. 만약에 원하는 바가 지역변수의 선언이 아니라 전역변수에 0을
# 저장하는 것이라면 다음과 같이 global로 시작하는 선언을 해야 한다.


cnt = 100
def func():
	global cnt   # 이 함수 내에서 접근하는 cnt는 전역변수임을 알려줌
	cnt = 0      # 전역변수 cnt에 0 저장
	print(cnt)   # 전역변수 cnt 값 출력

func()

print(cnt)


# 가급적 함수 내에서 전역변수에 접근하는 상황에서는 global 선언을 넣어주자

# 2. 객체지향 프로그래밍 

# c++, Java, c# 같은 것들이 객체지향 프로그래밍이다.
# 물론 Python도 포함 



# 3. 클래스와 객체 이전의 프로그램에 대한 반성

# family_age1.py

fa_age = 39      # 아빠 나이 정보, 현재 39살

def up_fa_age():    # 이 함수를 호출하면 아빠 나이 올라감
	global fa_age   # 이 함수에서 접근하는 fa_age는 전역 변수임을 선언함!
	fa_age += 1     # fa_age의 값 1 증가


def get_fa_age():   # 이 함수 호출하면 아빠 나이 반환함
	return fa_age   # fa_age의 값 반환


def main():
	print('2019년...')
	print('아빠:', get_fa_age())
	print('2020년...')
	up_fa_age()    # 아빠 나이 1살 증가
	print('아빠:', get_fa_age())


main()

# family_age2.py

fa_age = 39    # 아빠 나이 정보

def up_fa_age():     # 아빠 나이 올라감
	global fa_age    # 전역 변수 선언
	fa_age += 1

def get_fa_age():    # 아빠 나이는?
	return fa_age


mo_age = 35   # 엄마 나이 정보


def up_mo_age():  # 엄마 나이 올라감
	global mo_age
	mo_age += 1 

def get_mo_age():   # 엄마 나이는?
	return mo_age


def main():
	print('2019년...')
	print('아빠:', get_fa_age())
	print('엄마:', get_mo_age())
	print('2020년...')

	up_fa_age()
	up_mo_age()

	print('아빠:', get_fa_age())
	print('엄마:', get_mo_age())


main()


# 4. 클래스와 객체의 이해   책 p.227 참조

# 객체란 우리 주변에 존재하는 모든 사물 하나하나를 뜻한다.

# ex> 자동차 설계도 <클래스>
	   # 설계도를 기반으로 만들어진 자동차 <객체>

	  # 에어컨 설계도 <클래스>
	  # 설계도를 기반으로 만들어진 실제 이어컨

# 설계도 작성을 위해서 코드를 수정해보자.

def up_fa_age():
	global up_fa_age
	fa_age += 1

# 위의 원본을 다음과 같이 수정해보자

def up_age(self):   # self가 왜 등장했는지는 모름, 단 self는 매개변수임
	self.age += 1   # age가 아니라 self.age이다. 이렇게 바뀐 이유 아직 모름

# 다음 원본도 수정해보자


def get_fa_age():
	return fa_age

# 수정하기

def get_age(self):  # self가 왜 등장했는지 아직 모름, 단 self가 매개 변수인 건 알고 있음. 
	return self.age   # age가 아니라 self.age이다. 이렇게 바뀐 이유 아직 모름


# 위에 작성된 두함수를 클래스에 담아 보기

class Age_Info:  # 클래스 AgeInfo의 정의
	def up_age(self):   # 클래스 안에 담긴 up_age 함수
		self.age += 1
	def get_age(self):  # 클래스 안에 담긴 get_age 함수
		return self.age

# 실제로 함수를 호출할때 매개 변수 self에 어떤 값을 전달해야 하는 것도 아니다.

# 그런데 클래스 안에 변수 age를 안 담았잖아요.

# 그렇다, 안 담았다. 그런데 파이썬이 알아서 넣어준다. (실제와는 차이가 있는 설명이다, 그러나 일단은 이렇게 이해하자.)


# 다음 문장을 분석해보자.

# class_object.py
class Age_Info:   # 클래스 AgeInfo의 정의
	def up_age(self):
		self.age += 1
	def get_age(self):
		return self.age


def main():
	fa = Age_Info()  # AgeInfo의 객체를 생성하고 이를 변수 fa에 저장
	fa.age = 39    # fa에 저장된 객체의 변수 age에 39를 저장

	print("현재 아빠 나이...")
	print("아빠:", fa.get_age())   # get_age 호출할 때 self에 값 전달하지 않음

	print("1년 뒤...")
	fa.up_age() # up_age를 호출할때 self에 값 전달하지 않음

	print("아빠:", fa.get_age()) # get_age 호출할때 self값 전달하지 않음


main()


# fa = AgeInfo()


# "AgeInfo의 객체가 생성되어서 변수 fa에 저장되었다" 라는 의미

# "AgeInfo의 인스턴스가 생성되어서 변수 fa에 저장되었다."


# 용어 정리

# 인스턴스 변수 : 인스턴스(객체) 안에 존재하는 변수
# 인스턴스 메소드 : 인스턴스(객체) 안에 존재하는 메소드 (함수)


# 5. 나이 정보 관리하는 이전 예제의 수정 결과


#family_age3.py

class AgeInfo:
	def up_age(self):
		self.age += 1
	def get_age(self):
		return self.age


def main():
	fa = AgeInfo()   # 아빠 나이 객체 생성
	mo = AgeInfo()   # 엄마 나이 객체 생성
	me = AgeInfo()   # 내 나이 객체 생성

	fa.age = 39      # 아빠 현재 나이
	mo.age = 35      # 엄마 현재 나이
	me.age = 12      # 내 현재 나이

	sum = fa.get_age()  + mo.get_age() + me.get_age()
	print("가족 나이 합:", sum)

	fa.up_age()      # 아빠 나이 한 살 올림
	mo.up_age()      # 엄마 나이 한 살 올림
	me.up_age()      # 내 나이 한 살 올림

	sum = fa.get_age() + mo.get_age() + me.get_age()

	print("1년 후의 합:", sum)

main()


# 6. self의 정체

# 앞서 생성했던 3개의 객체가 있다.

age = 39
def up_age():
	age += 1
def get_age():
	return age

age = 35
def up_age():
	age += 1
def get_age():
	return age

age = 12
def up_age():
	age += 1
def get_age():
	return age

# 3 객체 안에 있는 up_age, get_age 함수가 완전히 같으니까 이걸 공유할 수 없을까?

# 그 결과 같은 모델이 나온다.

def up_age(self):
	self.age += 1

def get_age(self):
	return self.age


# fa의 메모리 공간에 self라는 이름이 하나 더 붙어서 이 순간 self는 fa가 된다. 이는 10장 마지막 부분에서 리스트를 대상으로 설명했던 내용이다.

# self_test.py

class AgeInfo:
	def up_age(self):
		self.age += 1
	def get_age(self):
		return self.age

def main():
	fa = AgeInfo()
	fa.age = 20   # 인스턴스 변수 age의 값 20으로 초기화

	fa.up_age()   # fa에 저장된 객체의 up_age 함수 호출
	AgeInfo.up_age(fa)   # 위와 동일한 기능의 문장

	print(fa.get_age())   # fa에 저장된 객체의 get_age 함수 호출
	print(AgeInfo.get_age(fa))   # 위와 동일한 기능의 문장

main()

# 결괏값 : 22 두번 출력 


# 위 예제를 통해서 알 수 있듯이 AgeInfo 클래스의 두 함수를 직접 호출하는 방법은 다음과 같다.

# AgeInfo.up_age(...)    AgeInfo의 up_age 메소드 호출 방법
# AgeInfo.get_age(...)    AgeInfo의 get_age 메소드 호출 방법

# 즉, 우리가 다음과 같이 문장을 작성하면, 

# fa.up_age()

# 파이썬은 이 문장을 다음 형태로 바꿔서 함수를 호출한다.get_age

# AgeInfo.up_age(fa)


# 7. self 이외의 매개변수를 갖는 메소드들(함수들) 정의해보기

# 앞서 정의한 AgeInfo 클래스의 인스턴스 메소드는 다음과 같이 매개 변수로 self만 가지고 있다.

# class AgeInfo:
	# def up_age(self):   # 매개 변수는 self 하나다.
		# self.age += 1
	# def get_age(self):   # 매개 변수는 self 하나다.

# 그런데 인스턴스 메소드에는 얼마든지 매개변수를 추가 할 수 있다. 그래서 이번에는 self 이외의 매개 변수를 갖는 메소드를(함수를)
# 클래스에 추가하려고 한다. 추가할 메소드의 모습은 다음과 같다.

# def set_age(self, n)   # 매개 변수로 self도 있고 n도 있다.
	# self.age = n


# def set_age(self, age):
	# self.age = age    # age는 매개변수, self.age는 인스턴스 변수

# 이렇게 정의하면 '매개변수'와 '인스턴스 변수'의 이름이 같아지지만, 함수 안에서 그냥 age라고 쓰면 이는 매개 변수가 되고 self.age라 쓰면 
# 이는 인스턴스 변수가 되기 때문에 이렇듯 이름이 같아도 된다. 그럼 이러한 내용을 다음 예를 통해서 확인해보자.



# family_age4.py

class AgeInfo:
	def up_age(self):
		self.age += 1
	def get_age(self):
		return self.age
		self.age = age    # self.age는 인스턴스 변수, age는 매개변수

	def set_age(self, age):
		self.age = age    # self.age는 인스턴스 변수, age는 매개변수

def main():
	fa = AgeInfo()   # 아빠 나이 객체 생성
	fa.set_age(39)   # 아빠 나이 초기화, 매개 변수 age에 39 전달
	fa.up_age()
	print("1년후 아빠 나이:", fa.get_age())

main()


# 13. 생성자 (Initializer)

# *** 용어 정리  

# Java, c++에서는 constructor를 ("생성자")라고 부른다.

# Python에서는 initializer ("초기화")의 역할과 같다.
				# constructor("생성자")가 따로 있지만, 이름만 같지 역할이 다르다.


# 객체 생성 후에 반드시 해줘야 하는 일이 하나 있는데 그것은 다음과 같다.

# "인스턴스 변수의 초기화"

# 앞서 작성한 예제들을 보면 다음과 같이, 또는 set_age 메소드 호출을 통해 객체 생성 이후에 반드시 인스턴스 변수의 초기화를 진행하였음을 알수 있다.

def main():
	fa = AgeInfo()    # AgeInfo 객체 생성
	fa.age = 20       # 인스턴스 변수 age의 값을 20으로 초기화

# 이렇듯 객체 안에 존재하는 모든 변수는 초기화를 해야 한다. 그리고 이러한 초기화는 객체 생성 후에 바로 하는 것이 일반적이다.
# 그래서 파이썬은 객체의 생성과 변수의 초기화를 동시에 진행할 수 있도록 '생성자(constructor)'라는 것을 제공한다.


# ctro1.py

class Const:
	def __init__(self):    # 생성자라 불리는 메소드, 메소드 이름이 __init__ 이다.
		print("new")

def main():
	o1 = Const()
	o2 = Const()

main()


			
# /생성자를 통해서 어떻게 인스턴스 변수를 초기화 할 수 있을까?

# ctor2.py

class Const:
	def __init__(self, n1, n2):
		self.n1 = n1   # self.n1은 인스턴스 변수, n1은 매개변수
		self.n2 = n2   # self.n2은 인스턴스 변수, n2은 매개변수

	def show_data(self):
		print(self.n1, self.n2)

def main():
	o1 = Const(1, 2)  # 생성자에 1과 2를 전달
	o2 = Const(3, 4)  # 생성자에 3과 4를 전달

	o1.show_data()
	o2.show_data()


main()


 # def __init__(self, n1, n2):
 	# self.n1 = n1    # self.n1은 인스턴스 변수, n1은 매개변수
 	# self.n2 = n2    # self.n2은 인스턴스 변수, n2은 매개변수


 # family_age5.py

class AgeInfo:
 	def __init__(self, age):    # AgeInfo의 생성자
 		self.age = age   # 매개 변수 age에 전달된 값으로 인스턴스 변수 age 초기화
 	def up_age(self):
 		self.age += 1
 	def get_age(self):
 		return self.age

def main():
 	fa = AgeInfo(39)     # 객체 생성 그리고 초기화
 	fa.up_age()
 	print("1년 후 아빠 나이:", fa.get_age())

main()


# 이렇듯 클래스를 만들때에는 생성자도 함께 넣어 주어서 객체 생성과 동시에 그 객체의 모든 인스턴스 변수들을 적당한 값으로 초기화하는 것이 좋다.

# 13단원 자체는 무한 반복 하는 것이 좋다.























































