# chapter 9 . 튜플과 레인지

# 1. Tuple

# 이번에 소개하는 '튜플'이라는 것도 파이썬이 인식하는 데이터의 한 종류이다. 리스트와 비슷한 부분이 많으니 예시로 설명

# list 출력

ist = [1 ,2, 3]
print(ist)
print(type(ist))

# tuple 출력

tpl = (1, 2, 3)   # tuple은 이렇게 만든다.
print(tpl)
print(type(tpl))


# 다음과 같은 사실들을 알 수 있다.

# list는 [..]으로 포현하지만 tuple은 (..)으로 표현한다.

# tuple 역시 list와 마찬가지로 python이 인식하는 데이터의 한 종류이다.

# tuple 역시 list와 마찬가지로 하나 이상의 값을 묶는 용도로 사용된다.




# 둘의 차이점

# 1. list 값을 추가하거나

ist = [1, 2]
ist.append(3)    # list 끝에 3을 추가
print(ist)

# 2. 저장된 값을 수정할 수 있다.

ist = [1, 2, 3]
ist[0] = 7   # 맨 앞에 있는 값을 7로 수정
print(ist)


# **** Tuple은 값을 추가하거나 수정할 수 없다. 그러니까 처음 만들어진 상태 그대로 사용해야 한다.
# 문자열처럼 말이다. 

# Tuple은 한번 만들어지면 그 내용을 수정하지 못한다.


tpl = (1, 2, 3)

tpl[0]   # 이렇듯 값을 참조하는 것은 YES!

# tpl[0] = 7 # 이렇듯 값을 수정하는 것은 ERROR!



# 2. Tuple을 어디에다 쓸 것인가?

# 다음과 같은 예시에서 확인하자.

frns = ['사쿠라', 130923, '민주', 134242, '채원', 134256]
print(frns)

print(frns[2])   # 민주의 이름 출력 따로

print(frns[3])   # 민주의 학번 출력 따로

# 이렇게 출력하다보면 값이 밀려서 오해할수도 있다.

# 그래서 '이름이랑 생년월일 정보를 묶어서 관리하는 것이 좋겠다.'는 생각이 든다.

frns = [['사쿠라',130923], ['민주', 134242], ['채원',134256]]

print(frns[1])   # 민주 정보 출력

 # 이러한 정보는 누군가의 실수로 언제든지 바뀔수 있다.

# 그래서 code의 안정성을 부여하기 위해서 사용한다.

frns = [('사쿠라',130923), ('민주', 134242), ('채원',134256)]

print(frns[2])


# 참고로 javascipt에는 tuple이 존재하지 않는다.





# 3. Tuple 관련 함수와 연산들

# len(s)    tuple s의 길이 (s에 저장된 값의 개수) 반환
# min(s)    tuple s에 저장된 값 중에서 가장 작은 값 반환
# max(S)    tuple s에 저장된 값 중에서 가장 큰 값 반환

# 이전에 위의 함수들에 list나 문자열을 전달한 바 있다. 튜플을 대상으로도 동작한다.

nums = (3, 2, 5, 7, 1)
print(len(nums))    # 값의 개수는? 5

print(max(nums))    # 최댓값은? 7 

print(min(nums))    # 최솟값은? 1


# 그리고 tuple도 list나 문자열과 마찬가지로 객체이다. 따라서 tuple이 갖고 있는 함수들도 다음과 같이 존재한다.

# s.count(x)     # tuple s에 저장된 x의 개수 반환

# s.index(X)     # tuple s에 저장된 첫 번째의 x의 index 값 반환

# 예시

nums = [1, 2, 3, 1, 2]

print(nums.count(2))  # 2가 몇번 등장해?

print(nums.index(1))  # 가장 앞에(왼쪽에) 저장된 1의 index 값은? 


# 연산들 연습

nums = [1, 2, 3]
 
print(3 in nums) # nums에 3이 있니? True

print(2 not in nums)   # nums에 2가 없니? False

print(nums + [4, 5])   # nums에 [4, 5]를 덧붙인 결과는?

print(nums * 2)   # nums를 두개 덧붙인 결과는?

print(nums[0:3])   # nums[0] ~ num[2]을 꺼내면?


# Tuple을 대상으로도 똑같이 모든 연산이 가능하다. 물론 결과도 완전히 동일하다.

nums = (1, 2, 3)

print(3 in nums) # nums에 3이 있니? True

print(2 not in nums)   # nums에 2가 없니? False

print(nums + (4, 5))   # nums에 (4, 5)를 덧붙인 결과는?

print(nums * 2)  # nums를 두개 덧붙인 결과는?

print(nums[0:3])  # nums[0] ~ num[2]을 꺼내면?


# Tuple을 한번 만들면 수정을 못하지 않나요? 질문이 들어 올수도 있다.
# 그렇지만, 저장된 튜플이 수정된 것이 아니라 새로운 튜플이 생성된 것이다.


nums + (4, 5)   # nums에 저장된 tuple과 (4, 5)를 합한 새로운 tuple 생성
nums * 2  # nums에 저장된 tuple 두개를 이어 놓은 새로운 tuple 생성
nums[0:3]  # nums에 저장된 tuple의 일부로만 이뤄진 새로운 tuple 생성


# list 기반으로 for loop를 작성할 수 있듯이, Tuple을 기반으로도 다음과 같이 for loop를 작성할 수 있다.

for i in (1, 3, 5, 7, 9):
	print(i, end ='')







# 4. list안에 저장된 data 바꾸기.


frns = [['연아', 131120], ['똘이', 130312], ['망고',130904]]

frns[1] = ['예나', 131110]

print(frns) 

# 여기서 만약 예나의 학번을 131100으로 수정하려면 어떻게 해야 할까??

# 판단을 해보면 frns[1][0]이 의미하는 바는 '예나'이다.
# frns[1][1]이 의미하는 바는 131110 이다.

print(frns[1][0])

print(frns[1][1])

frns[1][1] = 131100

print(frns)

# 수정 된다.

# 위와 같은 접근 방식은 tuple이 저자된 경우에도 달라지지 않는다.

frns =[('선미', 123), ('민주', 456),('유진', 789)]

print(frns[0][0])

print(frns[0][1])

# 튜플에 저장된 데이터가 수정 불가능 한 것이므로 다음과 같이 list에 저장된 튜플 하나를 교체하는 것은 얼마든지 가능하다.


# 5. 범위를 지정하는 레인지

for i in range(1, 11):
	print(i, end = ' ')


r = range(1, 10)  # range 호출로 만들어진 객체를 변수 r에 담는다.
print(type(r))

r = range(1 ,10)

print(9 in r)     # r이 저장한 레인지의 범위에 9가 들어가니?

print(10 in r)     # r이 저장한 레인지에 10이 안 들어가니?


# list(s)   s의 내용으로 채워진 list를 만들어 주겠다.

# tuple(s)   s의 내용으로 채워진 튜플을 만들어 주겠다.

print(list((1,2,3)))   # 튜플을 list로

print(list(range(1,5)))   # range를 list로

print(list("hello"))   # 문자열을 list로


print(tuple([1, 2, 3])) # list를 튜플로

print(tuple(range(1, 5)))  # range를 튜플로

print(tuple("hello"))  # 문자열을 튜플로


# 만들기 실습

ist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15)


ist = list(range(1, 16))    # 레인지를 넘겨서 list를 만듦
print(ist)

tpl = tuple(range(1, 16))    # 레인지를 넘겨서 튜플을 만듦
print(tpl)

print(range(1, 10 ,2))   # 1부터 10 이전까지 2씩 증가하는 레인지

print(range(1, 10, 3))   # 1부터 10 이전까지 3씩 증가하는 레인지

print(list(range(1, 10, 2)))   # 1부터 10 이전까지 2씩 증가하는 list 만들기

print(list(range(1, 10, 3)))   # 1부터 10 이전까지 3씩 증가하는 list 만들기


# 6. range 범위 거꾸로 지정하기

# 레인지 선언은, range(2, 10)
# 이 설정과도 같다. range(2, 10, 1)


print(list(range(10, 2)))   # 10부터 1씩 증가하여 2에 가까워지는 정수는 없다.

print(list(range(10, 2, 1))) # 10부터 1씩 증가하여 2에 가까워지는 정수는 없다.


# 그래서 위에 값들은 텅비게 된다.

# 세번째 전달 인자를 음수로 바꾸면 된다.

print(list(range(10, 2, -1)))   # 10부터 1씩 감소하여 3까지 이르는 정수들

print(list(range(10, 2 , -2)))  # 10부터 2씩 감소하여 3까지 이르는 정수들

print(list(range(10, 2, -3)))   # 10부터 3씩 감소하여 3까지 이르는 정수들









