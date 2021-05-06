class Car:
    # 클래스: 멤버변수(인스턴스변수) + 멤버함수
    speed = None
    color = None

    def run(self): # self: 자바에서 this의 의미
        print(self.color, '색 차가 달리다.')
    def start(self):
        print(self.speed, '속도로 출발하다.')

    def __str__(self): # 오버라이딩
        return str(self.speed) + ', ' + self.color

if __name__ == '__main__':
    car1 = Car() # 객체 생성
    car1.color = '빨강'
    car1.speed = 100
    print(car1)
    print(car1.color)
    print(car1.speed)
    car1.run()
    car1.start()

    car2 = Car() # 객체 생성
    car2.color = '노랑'
    car2.speed = 150
    print(car2)
    print(car2.color)
    print(car2.speed)
    car2.run()
    car2.start()


