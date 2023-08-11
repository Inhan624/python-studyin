### 예외처리 & 클래스 ###

# 교재 p.306
# 우리나라의 모든 도를 맞히는 퀴즈

# 지시사항
# * 1. Quiz 클래스는 다음과 같은 클래스 변수를 가지고 있습니다.
# 클래스 변수 answer 작성
# answer = ['경기도', '강원도', '충청남도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']
# 클래스 메서드 challenge()작성
answer = ['경기도', '강원도', '충청남도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']

class Quiz:
    answer = ['경기도', '강원도', '충청남도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']

    # 클래서 메서드 challenge() 작성
    @classmethod
    def challenge(cls):
        user_input = input('도를 입력하세요:')
        if user_input in cls.answer:
            cls.answer.remove(user_input)
            print('정답입니다.')
            if len(cls.answer) == 0:
                pirnt('모든 도를 맞혔습니다. 성공입니다.')
                return
            cls. challenge()
        else:
            raise Exception('틀렸습니다')
        
try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈 입니다. 하나씩 대답하세요')