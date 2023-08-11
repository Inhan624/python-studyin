### shapes.py 모듈을 사용###

# 1. import하여
# 변의 길이가 10인 정사각형의 넓이 계산하고 출력
# 반지름이 5만원인 넓이를 계산하고 출력

import shapes
print(shapes.calculate_square_area(10)) # 100
print()
# 2. from import 사용
# shape 모듈에서 calculate_square_area 함수만을
# import 하여 변의 길이가 7인 정사각형의 넓이를
# 계산하고 출력


from shapes import calculate_square_area
print(calculate_square_area(7)) # 49

# 3. import as 사용
# shapes 모듈을 s라는 별칭으로 import하여
# 반지름이 10인 원의 넓이를 계산하고 출력하는 코드 작성

import shapes as s
print(s.calculate_circle_area(10)) # 314.0