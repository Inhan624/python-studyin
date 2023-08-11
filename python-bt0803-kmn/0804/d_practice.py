#
#! 교재 p.270
# 다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성
# title, author

# 지시사항
# 0. 해당 객체에 매개 변수값을 전달하는 set_info()메소드를 구현
# 1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를 구현

# 2. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요
#! book1, book2 인스턴스의 생성
# book1 = Book()
# book2 = Book()

#! book1, book2 제목과 저자 정보 저장
# book1.set_info('파이썬','이승아')
# book2.set_info('어린왕자', '생택쥐페리')

# 3. 생성된 인스턴스 book1과 book2를 리스트 book_list에 저장하세요

class Book:
    title = ""
    author = ""

    def set_info(self,title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'Title : {self.title}, Author: {self.author}')
        
book1 = Book()
book2 = Book()

book1.set_info('파이썬','이승아')
book2.set_info('어린왕자', '생택쥐페리')

book_list = [book1, book2]

for book in book_list:
    book.print_info()