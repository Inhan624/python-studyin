# 클래스 변수 & 클래스 메소드 & 정적 메소드 #

# 교재 p.282
# 가방을 만들 때마다, 현재 만들어진 가방이 몇개인지 계산하는 Bag 클래스

class Bag:

    count = 0 # 초기화

    def __init__(self):
        Bag.count += 1 # 생성자가 호출될 때마다 count가 1씩 증가

        @classmethod
        def sell(cls):
            cls.count -= 1 # 가방이 판매 될 때마다 count가 1씩 감소

        @classmethod
#        def remain_


# print('현재 가방: {}개'.format(Bag.remain_bag()))
# bag1 = Bag()
# bag2 = Bag()
# ㅠㅁㅎㄷ