### 상속 ###

#!  1. 상속 정의
# :  한 클래스의 속성과 메소드를 다른 클래스에게 전달하는 형태(매커니즘)
# : 새로운 클래스는 기본 클래스의 모든 속성과 메소드를 받아들이고
# : 추가적인 속성이나 메소드를 정의할 수 있다.

# : 상속 받는다 : 다른 캘래스의 기능을 돌려받는다.

#? 부모 클래스(슈퍼 클래스, 상위 클래스)





#! 2. 상속의 필요성
# 2-1. 재사용성
# : 이미 정의된 클래스의 속성과 메소드를 재사용해서 코드 중복을 줄임.

# 2-2. 확장성
# : 기본 클래스를 수정하지 않고 새로운 기능을 추가 & 기본 기능 수정 가능

# 2-3. 모듈화
# : 특정 기능의 집합을 부모 클래스에서 정의,
# : 여러 지식 클래스를 정의하여 모듈화된 설계 가능

#! 3. 상속 관계 구현
# '~은 ~이다'의 관계가 성립
# Vehicle(운송수단) - car(자동차)
# Computer(컴퓨터) - SamSungNoteBook(삼성노트북)

# Rameon(라면) - LeeSeungAh(이승아)

class ParentClass:
    def method_in_parent(self):
        print('이 메소드는 부모 클래스에서 정의 되었습니다.')

# 서브 클래스를 구현할 때는
# 소괄호()안에 어떤 슈퍼 클래스를 상속받는지 명시해야 한다.
class ChildClass(ParentClass):
    pass # 특별한 기능 동작을 하지않을 때 작성

parent = ParentClass()
child = ChildClass

parent.method_in_parent()
child.method_in_parent()