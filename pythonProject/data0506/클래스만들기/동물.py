# class: 틀의 역할! => object(객체): 틀을 가지고 만든 실제 대상(우리가 쓸 수 있는 부품의 역할)

class Dog:
    # 멤버변수
    color = None # null의 뜻
    field = ''

    # 생성자 함수(객체생성시 자동호출되는 함수, 초기화를 담당)
    # 생성자: Constructor
    def __init__(self, color, field): # initialize: 초기화
        self.color = color
        self.field = field
        print('생성자가 호출됨.')

    # 멤버함수
    def jump(self): # 멤버함수안 입력값은 모두 self가 들어감
        print('강아지가 점프한다.')

    def sleep(self):
        print('강아지가 잔다.')

    # 오버라이드(재정의): toString()
    def __str__(self):
        return 'dog의 속성값들>> ' + str(self.color) + ', ' + self.field

if __name__ == '__main__':

    # dog1 = 참조형변수(주소)
    #        : 객체 생성할 때 dog1에 대한 특성을 저장하기 위해 멤버변수들이 복사
    dog1 = Dog('white', '진돗개')

    # 생성자호출(객체 사용할 수 있도록 준비), 자바의 new
    print(dog1)
    dog1.sleep()
    dog2 = Dog('blue', '요크셔테리어')
    print(dog2)
    dog2.jump()
