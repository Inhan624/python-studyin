### 생성자 & 소멸자 예제 ###

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Service')