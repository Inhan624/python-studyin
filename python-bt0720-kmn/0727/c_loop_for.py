
#! 1
#^ (교과서) 1부터 5사이에 존재하는 모든 정수를 역순으로출력하는 프로그램을 구현

n = 5
while n >= 1:
    print(n)
    n-= 1

# range()함수 - 세 개의 인자( 범위 시작점, 범위 끝점, 간격)
for i in range(5, 0, -1):
    print(i)
#! 2
#^ (교과서) 사용자로부터 임의의 양의 정수를 하니 입력받은 뒤
# 그 숫자만큼 '과일 이름'을 입력받아 basketj 리스트에 저장하는 프로그램을 구현


# 사용자로부터 임의의 양의 정수 입력 받기
num_of_fruits = int(input('입력할 과일의 개수를 입력하세요 : '))

# basket 빈 리스트 생성
basket = []

# 입력받은 숫자만큼 반복하면서 과일 이름을 입력 받고 리스트에 추가
for i in range(num_of_fruits):
    fruit =  input('과일이름을 입력하세요 : ')
    basket.append(fruit)

print('과일바구니 : ', basket)

