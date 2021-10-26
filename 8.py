#  chapter 8. for loop 와 while loop   






# 1. for loop에 대한 remind

# for loop의 기본 뼈대 

# for <변수> in <번위>:
	# <for에 속하는 문장들>

# "하나 이상의 문장을 정해진 횟수만큼 반복해서 실행한다."

#  for_sum.py

def main():
	sum = 0
	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
		sum = sum + i     # sum에 저장된 값을 i에 저장된 값만큼 증가시킴

	print("sum =", sum, end = ' ' )

main()

# end ='' 이 옵션의 경우 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있습니다. 


# for_sum_range.py

def main():
	sum = 0
	for i in range (1, 11):   # 변수 i에 1부터 11 이전의 값까지 넣어가며 반복
		sum = sum + i

	print("sum =", sum, end =' ')

main()





# 2. True인 동안 반복하는 While loop (False가 될때 멈춘다.)

# While loop는 다음과 같이 생겼다.

# while <조건>:
	# <조건이 True인 경우 반복 실행할 문장들>

#while_basic.py

def main():
	cnt = 0
	while cnt < 3:    # cnt의 값이 3보다 작으면 반복
		print(cnt, end = '  ')
		cnt = cnt + 1    # cnt에 저장된 값을 1 증가


main()



# 3. for loop    vs.   while loop

# 공통점 : code의 반복 실행에 사용된다.
# 차이점 : for loop : 반복의 횟수를 지정, while loop는 반복의 조건을 지정

# 기본 form 

# for <변수> in <반복 범위>:
	# <for에 속하는 문장들>


# while <반복 조건>:
	# <조건이 True인 경우 반복 실행할 문장들>	 

# 대부분의 경우 for loop <-------> while loop 

# while_sum.py

def main():
	i = 1
	sum = 0   # 1부터 10까지의 합이 이 변수에 저장된다.
	while i < 11:   # i의 값이 11보다 작은 동안 반복
		sum = sum + i   # sum의 값을 i만큼 증가
		i = i + 1    # i의 값을 1 증가
	print("sum =", sum, end =' ')

main() 

# 어떨때 while loop로 작성하기에 적당할까?

# ex> "1부터 더해 나가다가 몇을 더했을때 처음으로 100을 넘기게 되는가?"
# 100을 넘길 때까지 덧셈을 계속해 나간다는 '반복 조건'이 있는 상황이므로 이 경우에는 while loop를 쓰는 것이 어울린다.


# while_over100.py

def main():
	i = 1
	sum = 0
	while sum <= 100:    # sum의 값이 100 이하인 경우에만 반복을 해라!
		sum = sum + i
		i = i + 1
	print(i-1, "더했을 때의 합", sum, end ='')

main()

def main():
	i = 1
	sum = 0
	while sum <= 10:    # sum의 값이 100 이하인 경우에만 반복을 해라!
		sum = sum + i
		i = i + 1
	print(i - 1, "더했을 때의 합", sum, end ='')
	# 0부터 시작해서 i - 1 해줌

main()



# 4. break 문

# 조건 : while loop나 for loop 안에서 사용해야 한다. break가 실행되면 이 명령문이 포함된 while loop나 for loop를 빠져나가게 된다.

# while_break.py

def main():
	i = 0
	while i < 100:
		print(i, end = ' ')
		i = i + 1
		if i == 20:
			break     # 이 문장이 속한 while loop를 빠져나간다.

main()


# 한 줄로 표현 :   if i == 20: break 


## while_over100.py와 비교

# while_over100_break.py

def main():
	i = 1
	sum = 0
	while True:
		sum = sum + i
		if sum > 100:    # sum > 100이면 아래의 break가 실행된다.
			print(i, "더했을 때의 합", sum, end = '  ')

			break
		i = i + 1

main()



# while True :
	# <조건이 True인 경우 반복 실행할 문장들>


# 이 경우 <반복 조건>이 항상 True이므로 이는 빠져나가지 못하는 구조의 while loop가 된다. 그리고
# 이러한 구조의 while loop를 가리켜 '무한 loop'라 한다. 물론 절대로 빠져 나가지 못하는 while loop를 만들면 이는 잘못이다.
# 그러나 예제에서는 다음 code를 while loop 안에 둠으로 인해서 빠져나갈 수 있는 길을 마련해 두었다.



# 5. continue 문


for i in range(1, 11):
	print(i, end = ' ')

# 여기서 짝수이면 출력을 건너뛴다.

# code 추가 
  # if i % 2 == 0:     # i가 짝수이면,
  	# continue           # for에 속한 문장들 중 나머지 부분 생략


for i in range(1, 11):
	if i % 2 == 0:
		continue

	print(i, end = '  ')    # 위의 continue가 실행되면 이 문장을 건너뛴다.

# 홀수가 출력된다.


u = 0
while u < 10:
	u = u + 1
	if u % 3 == 0: continue   # u가 3의 배수이면 다음 문장을 건너뛴다.
	print(u, end = '  ')


# 6. 이중 loop

#  for loop안에 또 for loop가 존재할때, 이를 가리켜 이중 for loop 라고 한다.


for i in [1, 2]:      # 바깥쪽 for loop
		for j in ['a', 'b' ,'c']:      # 안쪽 for loop
			print(j * i, end = '')


# 출력 결괏값 : a b c aa bb cc

# 분석

# 분석의 시작은 바깥쪽 for loop에서 시작한다. 바깥쪽 for loop에 의해서 그 안쪽에 위치한 for loop가 반복 실행되는 구조이다. 
# 즉, 변수 i가 1일때 다음의 형태로 안쪽 for loop가 실행이 된다. (그리고 a b c가 출력된다.)

# 그리고 이어서 변수 i가 2가 되어 다음 형태로 안쪽 for loop가 실행이 된다. (그래서 aa bb cc가 출력된다.)

# list안에 담겨 있는 문자열들 안에 문자 'r'이 몇번 등장하는지 세어보는 예제 (분석 철저히 할 필요가 있음)


sr = ['father', 'mother', 'brother']
cnt = 0
for s in sr:
		for c in s:
			if c == 'r':
					cnt += 1

print(cnt)






