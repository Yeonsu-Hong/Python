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


