# chapter 12. 딕셔너리

# 1. 딕셔너리의 이해

# 딕셔너리도 리스트나 튜플과 같이 데이터의 한 종류이다.

dc = {'정은호': '010-xxxx-xxxx', '강미나': '010-yyyy-yyyy'}   # 딕셔너리

print(dc)

# 저장된 데이터의 수는 2 개이고, 이 둘은 각각 다음과 같이 이름과 전화번호 정보를 하나의 쌍(pair)으로 해서 이뤄져 있다.

# 딕셔너리는 {..} 으로 감싸서 표현하며 이 안에 저장되는 값의 형태는 다음과 같아야 한다.

# key : value

# 딕셔너리에 저장되는 하나의 값에는 2가지 정보가 담기는데, 그 중 하나를 키(key)라고 하며 다른 하나를 값(value)이라고 한다.
# 위의 예에서 key는 이름 value는 전화번호

# 우리 주변에는 쌍(pari)을 이루는 데이터들이 상당히 많다. 따라서 이러한 것들을 저장하고 관리해야 하는 상황에서는 딕셔너리를 유용하게 사용할 수 있는데, 다음과 같은 예가 있다.

dc = {
	'코카콜라' : 900,
	'바나나맛 우유' : 750,
	'비타 500' : 600,
	'삼다수' : 450
}

print(dc)

# 키와 값은 무엇이든 될수 있지만, (단, list는 key로 둘수 없다. 리스트를 value으로 두는 것은 가능)

dc = {
	'코카콜라' : (900, '탄산음료'),
	'바나나맛 우유' : (750, '유제품'),
	'비타 500' : (600, '비타민 음료'),
	'삼다수' : (450, '생수')
}

print(dc)



dc = {
	'이름': '신민아',   # 값이 문자열
	'나이': 36,         # 값이 정수
	'직업': '배우',		# 값이 문자열
	'키' : 170.9         # 값이 실수

}

print(dc)

# 한가지 주의할 점은 '값(value)'는 중복되어도 괜찮지만, 키(key)는 이름 그대로 값을 꺼내는 열쇠의 의미를 깆기 때문에 중복될수 없다.

dc = {
	'이순동': 21,
	'김순동': 21,
	'박순동': 21	
}

print(dc)

# but 다음과 같이 키의 데이터가 동등한 엉뚱한 결과로 이어진다.

dc = {
	'이순동': 21,   # key가 '이순동''
	'이순동': 22,   # 이것도 key가 '이순동'
	'이순동': 23    # 이것 역시 key가 '이순동' 
}

print(dc)

# 결과는 마지막 것이 덮혀서 23이 나온다.

# 딕셔너리에는 하나의 key만 존재 할수 있다.


# 2. 딕셔너리의 데이터 참조, 수정, 추가, 삭제

dc = {
	'코카콜라': 900,         # 코카콜라 900원
	'바나나맛 우유': 750,    # 바나나맛 우유 750원
	'비타 500': 600,        # 비타 500은 600원
	'삼다수': 450           # 삼다수 450원
	}


v = dc['삼다수']

print(v)

# 450 출력

# 수정

dc['삼다수'] = 550    # 삼다수에 해당하는 값을 550으로 수정

print(dc)

# 다음과 같이 수정해도 된다.

dc['삼다수'] += 100    # 삼다수에 해당하는 값 100 증가

print(dc)


# 데이터의 추가

dc['카페라떼'] = 1300     # 이 경우에는 데이터의 추가로 이어진다.

print(dc)

# 데이터 삭제

del dc['비타 500']   # 비타500에 대한 정보 삭제

print(dc)



# 3. 연산자 ==을 대상으로 관찰하는 딕셔너리의 성격

t1 = [1, 2, 3]
t2 = [1, 2, 3]
t3 = [3, 2, 1]

print(t1 == t2) # t1과 t2가 같은가? 저장 내용과 순서가 같아서 True

print(t1 == t3) # t1과 t3가 같은가? 이경우 저장 순서가 달라서 False


# 두 list의 == 연산의 결과가 True이려면, 저장된 값과 순서가 모두 같아야 한다.


d1 = {1: 'a', 2: 'b'}
d2 = {1: 'a', 2: 'b'}
d3 = {2: 'b', 1: 'a'}

print(d1 == d2)    # d1과 d2가 같은가? 저장 내용이 같아서 True

print(d1 == d3)    # d1과 d3가 같은가? 저장 내용이 같아서 dl 경우에도 True

# 딕셔너리의 데이터는 저장 순서가 의미가 없다.


# 4. in 연산과 not in 연산

dc1 = {'코카콜라':900, '삼다수':450 }   # 음료 정보들의 모음
dc2 = {'새우깡':700, '콘치즈': 850}     # 과자 정보들의 모음

dc2['새우깡'] = 950   # dc2에는 과자 정보가 담겨 있으므로 OK

print(dc2)

# 그런데 실수로 dc1['새우깡'] = 950 이라고 할수도 있다.   # 실수로 음료 정보가 담긴 딕셔너리에 접근함

# in 연산을 통해서 딕셔너리에 특정 키가 있는지 확인 가능

'새우깡' in dc2    # dc2에 새우깡이 키가 있는가?

# True가 출력

if '새우깡' in dc2:   # '새우깡'이라는 키가 dc2에 존재하면,
	dc2['새우깡'] = 950   # 값을 950으로 수정


# not in 연산으로도 가능

if '카페파떼' not in dc1:  # 카페라떼라는 key가 dc1에 존재하지 않으면,
			dc1['카페라떼'] = 1200   # '카페라떼' : 1200 추가



# 5. 딕셔너리의 for loop

dc = {'새우깡': 700, '콘치즈':850, '꼬칼콘': 750}
for i in dc:
	dc[i] += 70

print(dc)

# for loop를 이용해 전품목 가격 70원씩 인상 ( 전부 일일이 수정하지 않아도 된다.)

# 딕셔너리를 대상으로 for loop 구성이 가능하다.

# 실제로는 딕셔너리의 '키'를 대상으로 for loop가 돌아간다!

















