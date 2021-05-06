class Day:
    # 실제값 변수: 인스턴스 변수(동적변수) <-> 정적변수(static)
    subject = ''
    time = ''
    place = ''
    count = 0

    # 생성자 함수(객체 생성시 자동 호출, 초기화 담당)
    def __init__(self, subject, time, place):
        self.subject = subject
        self.time = time
        self.place = place
        Day.count += 1 # 스태틱 변수
        print(str(Day.count) + '개 객체가 생성됨.')

    #멤버함수
    def study(self):
        return self.subject + "를 " + str(self.time) + "시간 하다."

    def where(self):
        return self.place + "에서 " + self.subject + " 공부를 하다."

    def __str__(self):
        return 'day의 속성값들>> ' + self.subject + ', ' + str(self.time) + ', ' + self.place

if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    day2 = Day('자바공부', 11, '신촌')
    day3 = Day('db공부', 12, '종로')

    print(day1)
    print(day2)
    print(day3)

    print(day1.study())
    print(day2.where())
    print(day3.study())
