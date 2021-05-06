def login():
    no2 = no_entry.get()
    print('입력한 id는', no2)
    title2 = title_entry.get()
    print('입력한 pw는', title2)
    cont2 = cont_entry.get()
    print('입력한 pw는', cont2)
    writer2 = writer_entry.get()
    print('입력한 pw는', writer2)


from tkinter import *

w = Tk()
w.geometry('400x250')

i = Label(w, text='항목', font=('고딕', 20), bg='green', fg='black', width='5')
i.grid(row=0, column=0)
j = Label(w, text='입력', font=('고딕', 20), bg='green', fg='black', width='10')
j.grid(row=0, column=1)

no = Label(w, text='번호', font=('고딕', 20), fg='blue', width='5')
no.grid(row=1, column=0)
no_entry = Entry(w, font=('고딕', 20), bg='white', fg='blue', width='10')
no_entry.grid(row=1, column=1)

title = Label(w, text='제목', font=('고딕', 20), fg='blue', width='5')
title.grid(row=2, column=0)
title_entry = Entry(w, font=('고딕', 20), bg='white', fg='blue', width='10')
title_entry.grid(row=2, column=1)

cont = Label(w, text='내용', font=('고딕', 20), fg='blue', width='5')
cont.grid(row=3, column=0)
cont_entry = Entry(w, font=('고딕', 20), bg='white', fg='blue', width='10')
cont_entry.grid(row=3, column=1)

writer = Label(w, text='작성자', font=('고딕', 20), fg='blue', width='5')
writer.grid(row=4, column=0)
writer_entry = Entry(w, font=('고딕', 20), bg='white', fg='blue', width='10')
writer_entry.grid(row=4, column=1)

b = Button(w,
           text='글쓰기 완료.', font=('고딕', 25),
           bg='white', fg='green', width='10',
           command=login)
b.grid(row=5, column=1)

w.mainloop()