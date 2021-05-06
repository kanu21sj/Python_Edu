from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day):
# 파이썬: 클래스간 다중 상속이 가능하다.
# 자바: 클래스간 단일상속만 가능하다.

    # 부모가 파라메터가 있는 생성자이면, 부모의 생성자를 불러주어야 한다.
    def __init__(self, subject, time, place):

        # 단일 상속인 경우 super.__init__(self, 파라메터값 나열)
        # 다중 상속일 때는 클래스명.__init__
        my.Day.__init__(self, subject, time, place)

    def free(self):
        print('쉬다.!')

    def __str__(self):
        return self.subject + ', ' + str(self.time) + ', ' + self.place

if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 20, '마포구')
    woman_day1.free()
    woman_day1.eat()
    print(woman_day1)