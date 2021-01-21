import random
import tkinter
import sys
######### 사운드 출력 필요 모듈
import winsound    #'''파이썬에 내장된 패키지<--소리 재생'''
import time    #'''게임 시간 기록에 필요한 패키지'''
from tkinter import messagebox

import pyautogui

#힌트 버튼 클릭 함수
def click_hint():
    global times
    hint_btn["text"] = q
    times-=5


#게임 시작 함수
def GamePlay(event):
    global cor_cnt,q, n

    if(times==60):
        Timer()  

    if(input_word.get()==words[0]):
        winsound.PlaySound(                  
            './sound/good.wav',
            winsound.SND_FILENAME   #'''winsound의 PlaySound라는 클래스로 지정'''
            #'''SND_FILENAME을 직접 넣었음'''
        )
        print(input_word.get())
        cor_cnt += 1
        label_score.configure(text=cor_cnt)
        print('score:',cor_cnt)
    else:
        if(n==1):
            print(">>Start!\n")
        ########### 오답 소리 재생
        else:
            winsound.PlaySound(                  
                './sound/bad.wav',
                winsound.SND_FILENAME
            )
        ##################
            print(">>Wrong!\n")
    
    n+=1
    random.shuffle(words)                   # List shuffle!
    q = words[0]
    k = list(q)
    random.shuffle(k)
    s = "".join(k)
    label.configure(text=s)
    input_word.delete(0,"end")
    hint_btn["text"]="Hint"
    label_name.configure(text="user name\n"+user_name)

def Timer():
    global times,cor_cnt, user_name, n

    if(times> 0):
        times-=1
        label_Tim.configure(text=times)
        label_Tim.after(1000,Timer)
    else:
        best(cor_cnt,user_name)
        aboutUser=[]
        try:
            f=open('./resource/bestScore.txt', 'r',encoding='utf8')
        except IOError:
            print("파일이 없습니다!! 점수를 읽을 수 없습니다!!")
        else:
            aboutUser=(f.readlines())
            name=aboutUser[0].strip()
            score=int(aboutUser[1].strip())
            f.close()

        Retry = messagebox.askquestion('게임 오버','게임을 재시작하시겠습니까?\n'+'이름 :  '+ user_name+'\n'+'점수 : ' + str(cor_cnt)+'\n'+'최고 점수 : '+'{0}({1})'.format(score, name))
        if(Retry == 'yes'):

            cor_cnt = 0
            times = 30

            user_name = pyautogui.prompt('name ', 'Whats your name? ')
            label_Tim.configure(text=times)
            label.configure(text="GameStart")
            label_score.configure(text=cor_cnt)
            n = 1
            user=GameStart(user_name)                     #### GameStart의 user객체 생성
            user.user_info()

        else :
            root.destroy()  

#최고점 함수
def best(cor_cnt,user_name):
    aboutUser=[]
    try:
        f=open('./resource/bestScore.txt', 'r',encoding='utf8')
    except IOError:
        print("파일이 없습니다!! 점수를 읽을 수 없습니다!!")
    else:
        aboutUser=(f.readlines())
        name=aboutUser[0].strip()
        score=int(aboutUser[1].strip())
        f.close()

    if cor_cnt>=score:
        print("최고점수 :",cor_cnt,"  ",user_name)
        score_best=open('./resource/bestScore.txt', 'w',encoding='utf8')
        score_best.write(user_name)
        score_best.write("\n")
        d=str(cor_cnt)
        score_best.write(d)
        score_best.close()
    else:
        print("최고점수 :",score,"  ",name)  
    

############################# 추가 코드 ############################
# GameStart 클래스 생성
class GameStart:
    def __init__(self, user):
        self.user = user
        
    # 유저 입장 알림
    def user_info(self):
        print("User : {}님이 입장하였습니다.".format(self.user))
        print()
#####################################################################3

words = []                                   # 영어 단어 리스트(1000개 로드)

n = 1                                        # 게임 시도 횟수
cor_cnt = 0                                  # 정답 개수
times=60

try:
    word_f=open('./resource/word.txt', 'r') # 문제 txt 파일 로드
except IOError:
    print("파일이 없습니다!! 게임을 진행할 수 없습니다!!")
else:
        for c in word_f:
            words.append(c.strip())
        word_f.close()


if words==[]:                                #파일이 없을때 프로그램 종료
    sys.exit()


user_name = pyautogui.prompt('name ', 'Whats your name? ')
user=GameStart(user_name)                     #### GameStart의 user객체 생성
user.user_info()                              #### user 입장 알림 메서드 호출


#Root

root = tkinter.Tk()
root.title("애너그램 퀴즈")
root.resizable(False,False)

canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

book = tkinter.PhotoImage(file="background1.png")
canvas.create_image(400,300,image=book)

clock = tkinter.PhotoImage(file="clock.png")
canvas.create_image(580,70, image=clock)

score_img = tkinter.PhotoImage(file="score1.png")
canvas.create_image(300,80, image=score_img)

#영어단어 출력 라벨
label = tkinter.Label(root, text="start game",font=("system",50),bg='white' )
label.place(x=200,y=250)

#정답 입력 라벨 
input_word = tkinter.Entry(root,fg='white',font=("sytem",25),borderwidth=10 ,relief="sunken",bg= 'midnightblue')
input_word.place(x=135, y=480) 

#힌트 버튼
hint_btn=tkinter.Button(root,text="Hint",font=("system",25),command=click_hint)
hint_btn.place(x=340,y=390)

#점수 출력 라벨
label_score = tkinter.Label(root,text="Score",font=("system",30),bg='white')
label_score.place(x=350,y=50)

#타이머
label_Tim = tkinter.Label(root, text ="Timer",fg='red',font=("system",30),bg="white")
label_Tim.place(x=630,y=50)

#사용자 이름 라벨
label_name = tkinter.Label(root, text="user name\n"+user_name, fg='blue', font=("system",21), bg='white')
label_name.place(x=50,y=40)

#게임방식 설명 라벨
label_game = tkinter.Label(root, 
    text="Click the input box and press enter", 
    fg='midnightblue',
    font=("system",21), bg='white')
label_game.place(x=150,y=160)    

root.bind('<Return>',GamePlay)

root.mainloop()
