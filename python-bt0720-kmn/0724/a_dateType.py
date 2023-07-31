# 문자열 슬라이싱(Slicing): 문자열 안의 단어를 뽑아내는 역할
# 변수명[시작번호:끝번호] (시작번호와 끝번호는 해당 위치의 인덱스 번호)
# 슬라이싱의 경우 끝번호를 포함하지 않는다.
# ex) word[2:5]
# : 2 <= word <5

word = "I like you!"
print(word[2:5]) # lik
print(word[2:6]) # like

# 3-4.문자열 변경
# 문자열은 immutable 자료형
# : 요솟값을 변경할 수 없는 자료형

word[0:1] # 'I '
word[6:10] # ' you!'
print(word[:2] + 'love' + word[6:])
# 문자열의 슬라이싱의 경우 첫 인덱스번호와 마지막 인덱스 번호는 생략가능

# 3-5.문자열 포매팅
# : 문자열 내에 어떤 값을 삽입하는 방법
# 1) %-포매팅 (파이썬 교재 p.56 - % 연산자)
# %d: 숫자포맷 코드
# %s: 문자열 포맷 코드 (어떤 현태의 값이든 변환해서 삽입가능)
print('Hello, %s' %'python')
print('I have %d apples.' %4)

print('나는 100% 확신해') # 문자열 그 자체의 %를 출력하고 싶은 경우 : %%

# 2) str.format() 사용
print('Hello, {}'.format('python'))
print('I have {} apples'.format(4))
print('{} {} {}'.format('I', 'like', 'you'))

# 3) f-string 포매팅
name = 'python'
age = 20
print(f'My name is {name} and I ame {age} years old')

# f-string 포매팅의 장점: 표현식 지원(문자열 안에서 변수와, +, -의 수식을 함께 사용 가능
a = 5
b = 3
print(f'Five times three is {a * b}')

# 3-6. 문자열 관련 함수(내장 함수)
str = 'icecream'

# 1. 문자열의 길이: len()
print(len(str))

# 2. 문자 개수 세기: count()
print(str.count('c')) # 2

# 3. 문자 위치 알려주기: find()
print(str.find('r')) # 4
print(str.find('k')) # -1 : 문자열안에 해당 문자가 없는 경우 -1을 출력

# 4. 문자 위치 알려주기: index()
print(str.index('r')) # 4
#print(str.index('k')) #존재하지 않을 경우 오류 발생

# 5. 문자열 바꾸기: replace()
str2 = "strawberry chocolate cake"
str3 =str2.replace("strawberry", "banana")
print(str2)
print(str3)

#기타 문자열 내장 함수

#소문자를 대문자로 바꾸기(upper)
#대문자를 소문자로 바꾸기(lower)
str = 'Hello, World!'
print(str.upper()) # 'HELLO, WORLD!'
print(str.lower()) # 'hello, world!'

#문자열 나누기(split)
print(str.split()) # ['Hello,', 'World!']