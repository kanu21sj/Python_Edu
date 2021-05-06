from tkinter import *
from tkinter import messagebox
#버튼을 눌렀을 때 로그인 기능을 처리해야함.
#특정한 기능은 하나의 함수로 만들어 주면 됨.
#버튼 눌렀을 때 처리하고자 하는 기능하나는 함수하나가 됨.
#함수를 만드는 것을 함수를 정의한다하고 함.
#기능을 프로그래머가 정의하기 때문에 함수를 정의한다라고 표현함.
def login():
    #id입력한 값, pw입력한 값 가지고 와야함.
    #회원가입할 때의 id/pw와 입력한 값을 비교해야함.
    id2 = id_entry.get()
    print('입력한 id는', id2)
    pw2 = pw_entry.get()
    print('입력한 pw는', pw2)
    #pw 입력한 값 가지고와서 프린트
    #원래 id:root // pw:1234
    #원래 id/pw와 입력한 id/pw 동일한지 판별하여 프린트
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '축하합니다.')
        print('로그인 되었습니다.')
    else:
        messagebox.showinfo('로그인 실패', '잘못된 정보입니다.')
        print('잘못된 정보입니다.')

w = Tk()
w.geometry('500x250')

id = Label(w, text='ID입력', font=('궁서', 30)) #id 글자 올라감
id.pack()

id_entry = Entry(w, font=('궁서', 30),
                 bg='blue', fg='white') #id 입력
id_entry.pack()

pw = Label(w, text='PW입력', font=('궁서', 30),
           bg='blue', fg='white') #id 글자 올라감
pw.pack()

pw_entry = Entry(w, font=('궁서', 30),
                 bg='blue', fg='white') #pw 입력
pw_entry.pack()

b = Button(w,
           text='로그인 처리',
           font=('궁서', 30),
           bg='yellow',
           command=login) #클릭버튼
b.pack()

w.mainloop() # 위에 있는 거 다 뜨게해! --> 그러므로 맨 밑에 붙어야 함

# User Interface(UI)
 # Graphic User Interface(GUI): 사용자가 보는 그래픽 화면(윈도우 아이콘, 파이썬 tkinter)을
 # 클릭/입력해서 사용/실행
 # Command Line Interface(CLI): 사용자가 명령어를 쳐서 프로그램을 사용/실행