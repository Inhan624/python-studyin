### 리스트 메소드 복습 ###

# 문제 1: 주어진 리스트 numbers에 숫자 5를 추가하고, 결과 리스트를 출력하세요
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

#문제 2: 주어진 두 리스트 list1과 list2를 연결하고, 결과 리스트를 출력하세요.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 문제 3: 주어진 리스트 fruits의 두번쨰 위치에 'banana'를 삽입하고
# , 결과 리스트를 출력하세요.
fruits = ['apple', 'orange', 'grape']
fruits.insert(1, 'banana')
print(fruits)

# 문제 4: 주어진 리스트 numbers에서 마지막 항목을 제거하고
# , 저거된 항목과 결과를리스트를 출력 하세요