import tkinter as tk
import random
import time

canvas = tk.Tk()
canvas.geometry("1000x1000")
canvas.title("Card Game by Soumya")
canvas.config(bg='black')

score,time, active = 0, 60, 0
num_lst = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
open_lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
card = tk.PhotoImage(file = 'img_res\\card_bg.png')
random.shuffle(num_lst)
print(num_lst)

img_lst = []
for i in num_lst :
    root = 'img_res\\' + str(i) + '.png'
    img = tk.PhotoImage(file = root)
    img_lst.append(img)

label = tk.Label(canvas, text = f'Time Left : {time}               Score : {score}', fg = 'white', font = ('poppins', 12, 'bold'), bg ='black')
label.pack(anchor = 'center', pady = 15)

def disp(btn) :
    global img_lst, active, open_lst
    if 'clicked' in str(btn['text']) :
        btn['image'] = card
        btn['background'] = 'black'
        stri = str(btn['text']).replace('clicked', '')
        btn['text'] = stri
        open_lst[int(stri) - 1] = 0
        active -=1
    else :
        btn['background'] = 'white'
        pos = int(btn['text'])
        # root = 'img_res\\' + str(num_lst[pos-1]) + '.png'
        # img = tk.PhotoImage(file = root)
        open_lst[pos-1] = 1
        btn['image'] = img_lst[pos-1]
        btn['background'] = 'white'
        stri = str(btn['text'])+'clicked'
        btn['text'] = stri
        active +=1
    if (active == 2):
        chck_game()

def timer():
    global time, score
    if (time > 0 and score < 8) :
        time -= 1
        label.config(text= f'Time Left : {time}               Score : {score}/8', fg = 'white')
        canvas.after(1000, timer)
    else :
        for btn in btn_lst :
            btn['command'] = none_
        if (score == 8) :
           label.config(text= f'Congrats, You Won !!!')
        else :
             label.config(text= f'Time\'s up !! You lost !!!')

def chck_game() :
    global open_lst, score, btn_lst, num_lst, active, btn1_, btn2_
    k, no = 0, 0
    for i in open_lst :
        if (i == 1 and no == 0) :
            btn1_ = btn_lst[k]
            open_lst[k] = 0
            no += 1
        elif (i == 1 and no == 1):
            btn2_ = btn_lst[k]
            open_lst[k] = 0
        else :
            pass
        k += 1
    active = 0
    btn1_['text'] = str(btn1_['text']).replace('clicked', '')
    btn2_['text'] = str(btn2_['text']).replace('clicked', '')
    if (num_lst[int(btn1_['text']) - 1] == num_lst [int(btn2_['text']) - 1]) :
        score += 1
        btn1_['background'] = '#39FF14'
        btn2_['background'] = '#39FF14'
        btn1_['command'] = none_
        btn2_['command'] = none_

    else :
        canvas.after(500, revert)
        
def revert() :
    global btn1_, btn2_
    btn1_['image'] = card
    btn1_['background'] = 'black'
    btn2_['image'] = card
    btn2_['background'] = 'black'

frame1 = tk.Frame(canvas)
frame1.pack(anchor='center')
btn1 = tk.Button(text='1', image=card, background='black')
btn1.pack(side = 'left', in_=frame1)
btn1.config(command = lambda m = btn1 : disp(m))
btn2 = tk.Button(text='2', image=card, background='black')
btn2.pack(side = 'left', in_=frame1)
btn2.config(command = lambda m = btn2 : disp(m))
btn3 = tk.Button(text='3', image=card, background='black')
btn3.pack(side = 'left', in_=frame1)
btn3.config(command = lambda m = btn3 : disp(m))
btn4 = tk.Button(text='4', image=card, background='black')
btn4.pack(side = 'left', in_=frame1)
btn4.config(command = lambda m = btn4 : disp(m))

frame2 = tk.Frame(canvas)
frame2.pack(anchor='center')
btn5 = tk.Button(text='5', image=card, background='black')
btn5.pack(side = 'left', in_=frame2)
btn5.config(command = lambda m = btn5 : disp(m))
btn6 = tk.Button(text='6', image=card, background='black')
btn6.pack(side = 'left', in_=frame2)
btn6.config(command = lambda m = btn6 : disp(m))
btn7 = tk.Button(text='7', image=card, background='black')
btn7.pack(side = 'left', in_=frame2)
btn7.config(command = lambda m = btn7 : disp(m))
btn8 = tk.Button(text='8', image=card, background='black')
btn8.pack(side = 'left', in_=frame2)
btn8.config(command = lambda m = btn8 : disp(m))

frame3 = tk.Frame(canvas)
frame3.pack(anchor='center')
btn9 = tk.Button(text='9', image=card, background='black')
btn9.pack(side = 'left', in_=frame3)
btn9.config(command = lambda m = btn9 : disp(m))
btn10 = tk.Button(text='10', image=card, background='black')
btn10.pack(side = 'left', in_=frame3)
btn10.config(command = lambda m = btn10 : disp(m))
btn11 = tk.Button(text='11', image=card, background='black')
btn11.pack(side = 'left', in_=frame3)
btn11.config(command = lambda m = btn11: disp(m))
btn12 = tk.Button(text='12', image=card, background='black')
btn12.pack(side = 'left', in_=frame3)
btn12.config(command = lambda m = btn12 : disp(m))

frame4 = tk.Frame(canvas)
frame4.pack(anchor='center')
btn13 = tk.Button(text='13', image=card, background='black')
btn13.pack(side = 'left', in_=frame4)
btn13.config(command = lambda m = btn13 : disp(m))
btn14 = tk.Button(text='14', image=card, background='black')
btn14.pack(side = 'left', in_=frame4)
btn14.config(command = lambda m = btn14 : disp(m))
btn15 = tk.Button(text='15', image=card, background='black')
btn15.pack(side = 'left', in_=frame4)
btn15.config(command = lambda m = btn15 : disp(m))
btn16 = tk.Button(text='16', image=card, background='black')
btn16.pack(side = 'left', in_=frame4)
btn16.config(command = lambda m = btn16 : disp(m))

btn_lst = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16]
def none_ ():
    pass
btn1_, btn2_ = btn1, btn2
timer()

canvas.mainloop()