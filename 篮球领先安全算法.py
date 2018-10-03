score = float(input('领先的分数='))
ball = int(input('控球输入1，不控球输入0\n'))
score = score-3
if ball>=1:
    score = score + 0.5
else:
    score = score - 0.5
if score<0:
    score = 0
else:
    score = score**2
seconds = float(input('比赛剩余的秒数='))
if score>seconds:
    print("safe")
else:
    print("not safe")
        
