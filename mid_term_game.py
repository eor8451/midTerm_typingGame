import random
import winsound
import sqlite3
import datetime
from tkinter import *
import tkinter.ttk as ttk
import time
import sys

<<<<<<< HEAD
conn = sqlite3.connect('./resource/records.db',isolation_level=None)
=======

######### DB생성 & Autocommit
# 본인 DB 파일 경로
conn = sqlite3.connect('./resource/records.db', isolation_level=None)
>>>>>>> 52b680a76544367762543771e7306cfa88f024bb

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,\
cor_cnt INTEGER, record text, regdate text)"
)

root = Tk()
root.title("단어 맞추기 게임")
root.configure(bg='skyblue')
root.geometry("800x600")

label1=Label(root, text = "user : ",bg='skyblue')
label1.grid(row=0,column=0)
txt=Text(root, width=10,height=1)
txt.grid(row=0,column=1)
txt.insert(END,"")

def change():
    label1.config(text="등록 완료")
    btn.config(state="disabled")
    txt.config(state="disabled")

<<<<<<< HEAD

btn=Button(root,text="등록",command=change,bg='black',fg='white')
btn.grid(row=0,column=2)
btn.config(state="normal")

=======
############################# 추가 코드 ############################
# GameStart 클래스 생성
>>>>>>> 52b680a76544367762543771e7306cfa88f024bb
class GameStart:
    def __init__(self, user):
        self.user = user
        
    def user_info(self):
        label1.config(text="등록 완료")
        btn.config(state="disabled")
        txt.config(state="disabled")

words = []                                   # 영어 단어 리스트(1000개 로드)

n = 1                                        # 게임 시도 횟수
cor_cnt = 0                                  # 정답 개수

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
#print(words)                                 # 단어 리스트 확인

<<<<<<< HEAD
user=GameStart(txt)                     #### GameStart의 user객체 생성
#user.user_info()                            #### user 입장 알림 메서드 호출

label_word=Label(root,text="단어", font = (150),bg='skyblue')
label_word.place(x=350, y= 180)

label_answer=Entry(root, font=(50), bg='white',justify='left')
label_answer.place(x=300,y=350)
label_answer.focus_set()

start = time.time()                          # Start Time

while n <= 5:                                # 5회 반복
    
    random.shuffle(words)                    # List shuffle!
    q = random.choice(words)                 # List -> words random extract!

    label_word["text"]=q

    answer=Entry.get(label_answer)
    label_answer.delete(0,END)
    label_answer.insert(0,answer)

    random.shuffle(words)
    label_word.configure(text=words[0])
    label_answer.delete(0,END)

    def startGame(event):
=======

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
        print("최고점 :",cor_cnt,"  ",user_name)
        score_best=open('./resource/bestScore.txt', 'w',encoding='utf8')
        score_best.write(user_name)
        score_best.write("\n")
        score_best.write(str(cor_cnt))
        score_best.close()
    else:
        print("최고점 :",score,"  ",name)


user_name=input("Ready? Input Your name>> ")             # Enter Game Start! 
user=GameStart(user_name)                     #### GameStart의 user객체 생성
user.user_info()                              #### user 입장 알림 메서드 호출

start = time.time()                          # Start Time

while True:                                # 5회 반복
    random.shuffle(words)                    # List shuffle!
    q = random.choice(words)                 # List -> words random extract!

    remainTime = 10 -(int(time.time()-start))
    if(remainTime<=0):
        print('Game Over')
        break

    k = list(q)
    random.shuffle(k)
    s = "".join(k)
    print(q) #답

    print("{}번 문제>>".format(n),s)         # 문제 출력
    
    x = input("타이핑 하세요>> ")            # 타이핑 입력
>>>>>>> 52b680a76544367762543771e7306cfa88f024bb

        if label_answer.get()==label_word['text']:     # 입력 확인(공백제거)
            ########### 정답 소리 재생
            winsound.PlaySound(                  
                './sound/good.wav',
                winsound.SND_FILENAME   #'''winsound의 PlaySound라는 클래스로 지정'''
            #'''SND_FILENAME을 직접 넣었음'''
            )
        ############
            cor_cnt += 1                         # 정답 개수 카운트

        else:
            ########### 오답 소리 재생
            winsound.PlaySound(                  
                './sound/bad.wav',
                winsound.SND_FILENAME
            )
            ##################

        n += 1                                   # 다음 문제 전환



end = time.time()                            # End Time
et = end - start                             # 총 게임 시간

et = format(et, ".3f")                       # 소수 셋째 자리 출력(시간)

print()
print('--------------')


if cor_cnt >= 3:                             # 3개 이상 합격
    print("결과 : 합격")
else:
    print("불합격")

######### 결과 기록 DB 삽입
    '''data삽입 전에 먼저 기록테이블 구조 열어보기'''
cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
)
'''ID는 오토 인크리먼트이므로 입력안해줘도 자동으로 db에서 연속된 숫자형으로 넣어줌'''
'''strftime('%Y-%m-%d %H:%M:%S') : 포맷 변환'''

'''게임 실행해서 db기록되는지 확인'''
######### 접속 해제
conn.close()

#최고점 함수 호출
best(cor_cnt,user_name)

# 수행 시간 출력
print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

label_time=Label(root, text="제한시간 : ",font=(100),bg='skyblue')
label_time.place(x =550, y=80)

label_score=Label(root, text="맞춘 개수 : ", font= (100),bg='skyblue')
label_score.place(x=550,y=500)

random.shuffle(words)
label_word.configure(text=words[0])
label_answer.delete(0,END)

root.bind('<Return>',startGame)
root.mainloop()
