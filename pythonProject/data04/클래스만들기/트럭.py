class Truck:

    weight = None
    company = None

    def move(self):
        print(self.weight, '의 짐을 실어나르다.')
    def own(self):
        print(self.company, '회사 소속의 트럭입니다.')
    def __str__(self): # 오버라이딩
        return self.weight + ', ' + self.company

if __name__ == '__main__':
    truck1= Truck() # 객체 생성
    truck1.weight = '1톤'
    truck1.company = 'mega'
    print(truck1.weight)
    print(truck1.company)
    truck1.move()
    truck1.own()
