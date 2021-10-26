# print_age.py

# class AgeInfo:
def printAge ():
	num = int(input("나이 입력: "))
	if 1 <= num <= 19:
		print("미성년자")
	elif 20 <= num <= 64:
		print("성인")
	elif 65 <= num <= 120:
		print("노인")
	else:
		print("출력할 수 없습니다.")
	return n

printAge()

