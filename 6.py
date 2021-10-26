# chapter 6. list와 함수들

st = [1, 2, 3, 4, 5]

num = len(st) # len 함수는 list에 저장된 값의 개수를 반환

print(num)

# 이러한 유형의 함수 몇을 len 함수와 더불어 소개하면 다음과 같다.

# len(s)   list s의 길이(저장된 값의 수) 반환
# min(s)   list s에 저장된 값 중에서 가장 작은 값 반환
# max(s)   list s에 저장된 값 중에서 가장 큰 값 반환


st = [2, 5, 3 ,9, 1]
ex = min(st)

print(ex)
# 최솟값 출력


ff = [1, 34, 12, 15, 11111]
ex = max(ff)

print(ex)
# 최댓값 출력

# remove 함수의 호출

st = [1, 2, 3, 4]
st.remove(1)

print(st)

# st.remove(1) 에서 변수 이름 옆에 점이 찍혀 있다는 것을 주목해라.
# 이 의미는 "st(변수)에 담겨있는 객체의 remove함수를 호출하면서 1이라는 값을 전달하라"

# st[1, 2, 3]

# 이 list 안에는 사실 1,2,3의 값만 존재하는게 아니라 함수도 존재한다. (여러가지의 함수들)
# 위와 같이 데이터(값)과 함수가 묶여서 존재하는 덩어리를 가리켜 객체(object)라고 한다. 그러니까 사실 리스트는 객체이다.

# 리스트는 함수와 데이터가 함께 존재하는 객체이다.

# "객체 안에 존재하는 함수는 같은 객체에 있는 데이터를 대상으로 일을 한다."

# 이외에 list에 여러가지 함수들이 존재한다.
# (모두 외울 필요는 없고 필요할 때 참고 할 수 있는 정도로만 기억해 두면 된다.)

# s.append(x) list s의 끝에 x를 추가
# s.extend(t) list s의 끝에 list t의 내용 전부를 추가
#  s.clear()  list s의 내용물 전부 삭제
# s.insert(i, x) s[i]에 x를 저장
# s.pop(i)  s[i]를 반환 및 삭제
# s.remove(x) list s에서 제일 앞에 등장하는 x를 하나만 삭제
# s.count(x)  list s에 등장하는 x의 개수 반환
# s.index(x) list s에 처음 등장하는 x의 index값 반환

# 예시

st = [1, 2, 3]
st.append(4)   # st의 끝에 4 추가
st.extend([5, 6])   #st의 끝에 [5, 6]의 내용 추가
print(st)


st = [1, 2, 4]
st.insert(2, 3)    # index 값 2의 위치에 3 저장
print(st)

# [1, 2, 3, 4]가 출력된다.

st.clear()    # list 내용 전부 삭제
print(st)

st = [] # 빈 list 생성

st.append(1)   # list에 1 추가
st.append(3)   # list에 3 추가

print(st)


# pop, remove  # 둘의 차이점은 pop은 삭제할 때 삭제된 값을 되돌려주고, remove는 삭제 후의 값을 명시한다.

st = [1, 2, 3, 4, 5, 6]
st.pop(0)   # index 값 0의 위치에 저장된 데이터 삭제
# prompt창에서는 1이 출력된다.
# 위와 같이 pop이 호출되자 삭제한 내용이 출력되는데 이유는 pop이 삭제한 대상을 반환하기 때문에 나타난 결과이다.
# 반면 remove는 삭제한 대상을 반환하지 않기 때문에 별다른 출력으로 이어지지 않았다.


print(st)
# [2, 3 , 4, 5] 가 출력된다.

st.remove(5)    # list에서 5 삭제 (위치 지정된 값을 지우는 것이 아니라 삭제할 값을 바로 지운다.)

print(st)

st = [1, 2, 3, 4, 5]
st.count(1)    # 1이 몇번 등장하는지 세어라

st.index(2)    # 처음 2가 등장하는 위치의 index 값은?

print(st)









