from tkinter import *
import threading
import time
import random

# 스레드 클래스
class Thread:

    # 자동차 변수 생성 및 초기화
    car = None
    # 스레드 설정 및 초기화
    thread = None

    # init, tkinter 실행
    # self: 자바에서 this의 의미
    # 기타 파라메터 값으로 가짐
    def __init__(self, w, img, x1, y1):

        # 이미지 할당
        self.car = Label(w)  # tk창에 w라벨 생성, 멤버변수로 할당
        icon = PhotoImage(file = img)  # photoimage 변수에 파일 경로 설정하여 icon 변수설정
        self.car.configure(image = icon)  # configure, text 속성을 변경해주는 변수(이미지 형태로 변경)
        self.car.image = icon  # 가져온 이미지를 라벨에 넣어줌

        # 스레드 설정
        self.thread = threading.Thread(target = self.run, args=(self.car, x1, y1))

        # threading.Thread() = 스레드 설정
        # target, 스레드에서 실행시킬 함수 파라미터 self.run 으로 지정
        # args = target 반드시 튜플형태로 만들어져야 함

        self.thread.start()

    # 스레드 실행 함수
    # self: 자바에서 this의 의미
    def run(self, car, x1, y1):
        speed = 0

        # while true, 딱히 조건없이 계속 참이라는 뜻
        while True:

            # random.randrange, 범위가 10이상 50미만의 난수를 생성하는 함수
            speed = random.randrange(10,50)  # 한 번에 10~50 사이로 움직임
            if x1 >= 500:  # 골인 지점
                break  # x1>= 500 일 경우 while문 종료

            # x1 값이 500 미만일때 실행
            x1 = x1 + speed
            # car 변수의 위치를 x = x1, y = y1로 이동
            self.car.place(x = x1,  y = y1)
            time.sleep(0.5) # 대기시간

# 자동차 배치
def Cars():
    # 창, 파일명, x좌표, y좌표
    car1 = Thread(w,'carimage1.png',10,70)  # 스레드 클래스 생성과 동시에 함수 실행
    car2 = Thread(w,'carimage2.png',10,180)
    car3 = Thread(w,'carimage3.png',10,300)

# 메인코드
if __name__ == '__main__':

    # 윈도우 배치
    # Tk() tkinter
    w = Tk()
    w.title('자동자 경주')
    w.geometry('500x400')

    # 버튼 배치
    # 버튼의 text명 생성, command 실행 시 시작할 함수
    startbutton = Button(w, text='경기 시작', command=Cars)

    # 버튼 위치 설정
    # side 위치, fill 버튼 크기 윈도우 x축에 맞게, y는 top에 맞게
    # ipdax = 버튼 안 가로/세로축 여백
    # padx, pady 버튼 바깥 가로/세로축 여백
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5)

    # 윈도우 내부에서 수행되는 마우스 클릭 같은 이벤트들이 발생 하게끔 유지해주는 함수
    # 윈도우 실행 후 사용자의 입력을 기다리게 하려는 목적
    w.mainloop()