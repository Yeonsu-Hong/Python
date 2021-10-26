# main.py

def main():    # main 함수의 정의
	print("simple frame")

main()  # main함수 호출을 명령함



# random 숫자의 범위를 바꿔보라

import random

dice = random.randint(1,6)   # randint() 함수는 입력되는 두 정수 사이의 숫자를 랜덤하게 생성하는 함수로 random.randint(a,b)는 a이상 b이하의 한개의 정수를 만듦

print(dice)


name = '파이썬'

for i in name :
	print(i)


names = ['쵸파', '루피', '상디','조로',]
for name in names :
	print(name, end=' ') # 줄바꿈 대신 빈 공간 넣어라


# for i in range(100):
	# print(i ** 2)

# for i in range(100) :
	# print("메롱")


if 10 > 0:
	print('안녕하세요?')


print('[ 소름 끼치도록 놀라운 심리테스트 ]')
menu = input('당신이 좋아하는 음식을 입력해주세요 :')
if menu =='자장면':
	print('당신은 자장면을 좋아하는 사람입니다.')
elif menu == '아이스크림':
	print('당신은 아이스크림을 좋아하는 사람입니다.')
elif menu == '사탕':
	print('당신은 사탕을 좋아하는 사람입니다.')
else :
	print('당신은 자장면과 아이스크림과 사탕을 좋아하지 않는 사람입니다.')



for i in [0, 1, 2, 3]:
	print (i ** 2)

names = ['쵸파','루피','상디','조로']
for name in names :
	print(name)