# chapter 14. 예외처리 (오류 처리)

# 1. 예외가 발생하는 상황

# 몇가지 오류 상황을 만들어 보겠다. 다음은 잘못된 인덱싱 연산의 결과이다.

# ist = [1, 2, 3]    # 유효한 인덱스 값의 범위는 0 ~ 2
# ist[3]


# print(3 + "coffee")  # 숫자와 문자열은 더할 수 없음

# print(3/0)

# 위의 예들처럼 오류들이 발생하면 메시지들이 뜨는데 보통

# "ZeroDivisionError 예외"

# "IndexError 예외 : 인덱싱 연산에서 인덱스 값이 범위를 넘어선 예외"

# "TypeError 예외 : 연산이 불가능한 타입의 값으로 연산을 하는 예외

# 이런 예외를 모두 다 알고 있을 필요는 없다. 


# 2. 예외의 처리

# 프로그램 실행 중간에 예외가 발생하면 프로그램은 그냥 종료가 된다.


# 오류를 일부러 발생시키도록 코드를 짜보았다.

# age.py

# def main():
	# print("안녕하세요.")
	# age = int(input('나이를 입력하세요: '))
	# print('입력하신 나이는 다음과 같습니다:', age)
	# print('만나서 반가웠습니다.')

# main()


# "나이를 입력하세요: 에다가 스물이라고 넣으면 예외가 발생한다."

# 문자열 입력하면 int 함수 (실수형 함수) 호출 때 오류가 발생하기 때문이다.

# ValueError가 뜨는데, 한가지 아쉬운 점이 있다. 오류 발생시 "만나서 반가웠습니다. 인사를 하지 않는다는 점이다.

# 오류 유무 발생에 상관없이 실행되면 좋을 문장 아닌가?

# 그래서 예외처리 추가 코드를 넣고자 한다.

# age_expt.py 

def main():
	print("안녕하세요!!")
	try:
		age = int(input("나이를 입력하세요: "))
		print("입력하신 나이는 다음과 같습니다:", age)

	except ValueError:
		print("입력이 잘못되었습니다.")

	print("만나서 반가웠습니다.")

main()


# 예외 처리의 기본 구조

# try: 
	# try 영역

# except ValueError:
	# except 영역


# 책 p.253 참조하기


# 3. 보다 적극적인 예외의 처리

#age_expt_conti.py

def main():
	print("안녕하세요.")
	while True:    # while loop안에 try ~ except가 있다.
		try:
			age = int(input("나이를 입력하세요: "))
			print("입력하신 나이는 다음과 같습니다:", age)
			break    # 입력이 정상적이면 while loop 탈출!

		except ValueError:
			print("입력이 잘못되었습니다.")

	print("만나서 반가웠습니다.")

main()



# 3. 보다 적극적인 예외의 처리

# age_expt_conti.py

def main():
	print("안녕하세요.")
	while True:    # while loop안에 try ~ except가 있다.
		try:
			age = int(input("나이를 입력하세요: "))
			print("입력하신 나이는 다음과 같습니다:", age)
			break   # 입력이 정상적이면 while loop 탈출!
		except ValueError:
			print("입력이 잘못되었습니다.")

	print("만나서 반가웠습니다.")

main()

# 참조 사이트 : (https://wikidocs.net/21) 
# 위의 code에서 while True의 형태는 무한 loop의 기본 형태이다. 때문에 정상적인 입력이 없으면 입력을 계속 요구하게 된다.




# 4. 둘 이상의 예외를 처리하기

# 다음 예제에서 보이듯이 한 영역에서 발새 가능한 예외가 둘 이상인 경우도 있다.

#div.py

def main():
	bread = 10 # 현재 열 개의 빵이 있다!
	people = int(input("몇 명? ")) # Valueerror 예외가 발생할 수 있음 
	print("1인당 빵의 수:", bread / people)  # ZeroDivisionError 예외가 발생할 수 있음
	print("맛있게 드세요.")

main()


# 위의 예에서 몇 명이냐고 물었을때 잘못된 입력을 하면 Valueerror 예외가 발생한다. 그리고 0을 입력할 경우 나눗셈을 하는 과정에서
# ZeroDivisionError 예외가 발생한다. 따라서 이 경우에는 다음과 같이 예외처리를 해야 한다.



# div_expt1.py

def main():
	bread = 10 # 열개의 빵
	try:
		people = int(input("몇 명? "))
		print("1인당 빵의 수: ", bread / people)
	except ValueError:
		print("입력이 잘못되었습니다.")
	except ZeroDivisionError:
		print("0으로는 나눌 수 없습니다.")
	print("맛있게 드세요.")

main()

# 위의 code에서 빵을 나눠주지 못한 상황에서도 맛있게 드세요라는 인사를 하게 된다.


# div_expt2.py

def main():
	bread = 10    # 열개의 빵
	try :
		people = int(input("몇 명? "))
		print('1인당 빵의 수: ', bread / people)
		print("맛있게 드세요.")
	except ValueError:
		print("입력이 잘못되었습니다.")

	except ZeroDivisionError:
		print("0으로는 나눌 수 없습니다.")

main()



# 5. 예외 메시지 출력하기와 finally

# 예외가 발생해서 except 영역이 실행될 때, 파이썬은 예외 발생 원인에 대한 메시지를 전달한다. 
# 그리고 그 메시지를 확인하고 싶다면 다음과 같이 하면 된다.


# div_expt3.py

def main():
	bread = 10   # 10개의 빵

	try:
		people = int(input("몇 명? "))
		print('1인당 빵의수: ', bread / people)
		print("맛있게 드세요.")

	except ValueError as msg:    # 변수 msg에 오류 메시지가 담긴다.
		print('입력이 잘못되었습니다.')
		print(msg)   # 오류 메시지 출력

	except ZeroDivisionError as msg:   # 변수 msg에 오류 메시지가 담긴다.
		print("0으로 나눌 수 없습니다.")
		print(msg)   # 오류 메시지 출력

main()


# 그리고 예외 발생 유무에 상관없이 try 영역으로 진입하면 무조건 실행해야 하는 내용이 있다면, 다음예에서 보이듯이 except 여역에 이어서 
# finally 영역을 구성하면 된다. (except 영역 없이 finally 영역만 구성할수도 있다.)


# div_expt4.py

def main():
	bread = 10    # 10개의 빵
	try:
		people = int(input("몇 명? "))
		print('1인당 빵의 수: ', bread / people)
		print("맛있게 드세요.")

	except ValueError:
		print("입력이 잘못되었습니다.")
	
	finally:
		print("어쨋든 프로그램은 종료합니다.")

main()


# 위의 실행 결과를 보면 try 영역 안에서 ZeroDivisionError 예외가 발생했고, 이 예외를 처리할 수 있는 except 영역은 존재하지 않는 상태이다.
# 따라서 그냥 프로그램이 종료되어야 하는데 이런 상황에서도 finally 영역은 실행되었음을 알 수 있다.



# 6. 모든 예외 그냥 무시하기

# ignore_expt.py

def main():
	bread = 10 # 10개의 빵
	try:
		people = int(input("몇 명? "))
		print("1인당 빵의 수: ", bread / people)
		print("맛있게 드세요.")
	except:   # 이렇게 하면 모든 예외가 다 걸려든다.
		print("뭔지는 몰라도 예외가 발생햇군요.")

main()


# 문자열 조차 출력하고 싶지 않다면, 다음과 같이 pass를 써넣으면 된다.

	try:

	except:  # 이렇게 하면 모든 예외가 다 걸려든다.
		pass # pass 라고 써 놓으면 아무 일도 하지 않는 except영역 만들어짐


# 기초편 끝




















