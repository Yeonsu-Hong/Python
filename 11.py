# chapter 11. 모듈의 이해 그리고 수학 모듈 이용하기

# 1. 모듈 만들기


PI = 3.14     # 원주율

def ar_circle(rad):    # 원의 넓이를 계산해서 반환하는 함수
	return rad * rad * PI    # rad * rad * PI를 계산한 다음 그 값을 반환


def ci_circle(rad):    # 원의 둘레를 계산해서 반환하는 함수
	return rad * 2 * PI      # rad * 2 * PI를 계산한 다음 그 값을 반환


print(ar_circle(1.4))   # 반지름이 1.4인 원의 넓이는?


print(ci_circle(1.4))   # 반지름이 1.4인 원의 둘레는?




# 2. 모듈을 가져다 쓰는 방법 (1)

# circle_test1.py

import circle    # circle.py 모듈을 가져다 쓰겠다는 선언!

def main():
	r = float (input("반지름 입력: "))

	ar = circle.ar_circle(r)    # circle.py의 ar_circle 함수 호출 방법
	print("넓이:", ar)

	ci = circle.ci_circle(r)    # circle.py의 ci_circle 함수 호출 방법
	print("둘레:", ci)


main()


# 특정 함수 하나만 가져다 쓰겠다고 선언하는 방법

# circle_test2.py
from circle import ar_circle  # circle.py에서 ar_circle 함수를 가져다 쓰겠다.
from circle import ci_circle  # circle.py에서 ci_circle 함수를 가져다 쓰겠다.

# 위 두문장을 한문장으로 쓰는 방법

from circle import ar_circle, ci_circle  # circle.py에서 ar_circle, ci_circle 함수를 가져다 쓰겠다.

def main():
	r = float(input("반지름 입력: "))
	ar = ar_circle(r)     # circle.py의 ar_circle 함수 호출

	print("넓이:", ar)
	ci = ci_circle(r)     # circle.py의 ci_circle 함수 호출
	print("둘레:", ci)

main()


# 3. 모듈을 가져다 쓰는 방법 (2)

# 새로 만든 program

# circle_simple.py

def ar_circle(rad):    # 원의 넓이를 계산해서 출력
	print("넓이: ", rad * rad * 3.14)

def ci_circle(rad):    # 원의 둘레를 계산해서 출력
	print("둘레: ", rad * 2 * 3.14)

def main():
	r = float(input("반지름 입력: "))
	ar_circle(r)
	ci_circle(r)

main()

# 똑같이 실행이 된다.
# 차이는??

def ar_circle(rad):   # 앞서 정의한 함수
	return rad * rad * PI    # 계산 결과를 반환

# 바로 위에서 만든 함수는 다음과 같이 값을 반환하지 않고 그냥 출력을 한다.

def ar_circle(rad):    # 바로 위의 예에서 정의한 함수
	print("넓이: ", rad * rad * 3.14)    # 계산 결과를 print 함수에 전달해서 출력

# 원의 넓이와 둘레의 합도 계산해야 한다면??

# 앞에서 만들었던 circle.py 끌어다 쓰기

# 그래서 다음과 같은 code를 작성했는데...



# circle_simple2.py

from circle import ar_circle   # circle.py의 ar_circle 함수를 가져다 쓰려고 한 선언
from circle import ci_circle   # circle.py의 ci_circle 함수를 가져다 쓰려고 한 선언


def ar_circle(rad):    # 원의 넓이를 출력, 원래 가지고 있던 함수
	print("넓이: ", rad * rad * 3.14)

def ci_circle(rad):    # 원의 둘레를 출력, 원래 가지고 있던 함수
	print("둘레: ", rad * 2 * 3.14)

def main():
	r = float(input("반지름 입력: "))
	ar_circle(r)       # 위에 있는 함수를 호출하려는 상황
	ci_circle(r)       # 위에 있는 함수를 호출하려는 상황

# sum = ar_circle(r) + ci_circle(r)  # circle.py에 있는 두 함수를 호출하려는 상황
	# print("넓이와 둘레의 합: ", sum)

# main() 


#  오류발생 : IndentationError: unexpected indent
#  이유는 다음과 같다. 예제에서 만든 함수의 이름과 가져다 쓰려는 함수의 이름이 똑같다.

from circle import ar_circle   # circle.py의 ar_circle을 갖다 쓰겠음
from circle import ci_circle   # circle.py의 ci_circle을 갖다 쓰겠음

# 다음과 같이 바꿔주면 문제는 해결된다.

from circle import ar_circle as ac  # circle.py의 ar_circle을 ac라는 이름으로 갖다 쓰겠음
from circle import ci_circle as cc  # circle.py의 ci_circle을 cc라는 이름으로 갖다 쓰겠음


# circle_simple.2py

from circle import ar_circle as ac   # 가져다 쓸 ar_circle을 ac라는 이름으로
from circle import ci_circle as cc   # 가져다 쓸 ci_circle을 cc라는 이름으로 


def ar_circle(rad):       # 원의 넓이를 출력
	print("넓이: ",  rad * rad * 3.14)
def ci_circle(rad):       # 원의 둘레를 출력
	print("둘레: ", rad * 2 * 3.14)

def main():
	r = float(input("반지름 입력: "))
	ar_circle(r)
	ci_circle(r)
	sum = ac(r) + cc(r)    # circle.py에 있는 두 함수 호출
	print("넓이와 둘레의 합: ", sum)

main()


# 4. as로 모듈의 이름 줄이기

# circle_test3.py

import circle as cc   # circle.py 모듈을 cc라는 이름으로 가져다 쓰겠다는 선언!

def main():
	r = float(input("반지름 입력: "))
	ar = cc.ar_circle(r)   # cc라는 이름으로 circle.py의 함수를 호출한다.



# 5. 수학 관련 모듈

# /import 선언 없이 그냥 언제든 호출 가능한 함수를 가리켜 빌트인 함수라고 한다.

# 빌트인 모듈은 import 선언만 하면 언제든 그 안에 있는 함수들을 호출할 수 있다.

# math.pi  π

# math.asin(x)   arcsin x

# math.acos(x)   arcos x

# math.atan(x)   arctan x

# math.log(x)    ln x

# math.fabs(x)   |x|

# math.degrees(x)  convert radians to degrees

# math.radians(x)  convert degrees to radians


import math  # math 모듈 가져다 쓰겠다는 선언

print(math.fabs(-10))   # math 모듈의 fabs함수 호출

# 각도를 나타내야 하는 방법

# (1). 직각에 대한 degree 표현 : 90도
# (2). 직각에 대한 radian 표현 : π/2

# sin 45 cos 45 tan 45

# 1. 다음과 같이 함수에 radian 값을 바로 전달하거나,

import math

print(math.sin(math.pi/4))   # math.pi는 π, 그리고 π는 radian 단위의 값

print(math.cos(math.pi/4))

print(math.tan(math.pi/4))

# 2. 다음과 같이 radians 함수를 이용해서 값을 바꿔서 전달 (import math는 한번 했으면 반복하지 않아도 된다.)

print(math.sin(math.radians(45))) # 45를 radian 단위로 바꿔서 sin 함수의 인자로 전달

print(math.cos(math.radians(45)))

print(math.tan(math.radians(45)))









