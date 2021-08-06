# -*- coding: utf-8 -*-
import sys, time, os, pygame
from pygame.locals import *
pygame.init()

os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (130, 60)
canvas = pygame.display.set_mode((1000, 600))
canvas.fill((0, 0, 0))

pygame.display.set_caption("时间掌控者")

# 添加背景图片
bg = pygame.image.load("imgs/bg.jpg")
# 添加按钮图片
button = pygame.image.load("imgs/button.png")
# 添加倒计时图片
n1 = pygame.image.load("imgs/n1.jpg")
n2 = pygame.image.load("imgs/n2.jpg")
n3 = pygame.image.load("imgs/n3.jpg")
n4 = pygame.image.load("imgs/n4.jpg")
n5 = pygame.image.load("imgs/n5.jpg")
# 添加感知等级图片
king = pygame.image.load("imgs/king.png")
diamond = pygame.image.load("imgs/diamond.png")
bronze = pygame.image.load("imgs/bronze.png")

def handleEvent():  
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()
        click(event)
a = 0


def click(event):
    global a
    global startTime
    global lastTime 
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        canvas.blit(bg, (0, 0))
        canvas.blit(button, (350, 330))
        if a == 0:        
            fillText('世界上最快而又最慢，', (200, 150))
            fillText('最长而又最短，', (580, 150))
            fillText('最平凡而又最珍贵，', (350, 200))
            fillText('最易被忽视而又最令人后悔的是什么？', (200, 250))
            a = a + 100  
        elif a == 100:
            fillText('时    间', (420, 200))
            a = a + 100
        elif a == 200:
            fillText('接下来敢不敢接受挑战测试一下你的时间的感知度呢？', (40, 200))
            a = a + 100 
        elif a == 300:
            fillText('游戏规则：', (35, 100))
            fillText('游戏开始屏幕进行计时显示，当显示到5后，提示消失，', (35, 150))
            fillText('根据自己对时间的感知判断，当时间到达20按下按钮', (35, 200))
            fillText('真正的勇士敢于按下这个按钮', (250, 450))
            a = a + 100 
        elif a == 400:
            fillText('游戏开始', (420, 100))  
            startTime = time.time()
            canvas.blit(n1, (0, 0))
            pygame.time.delay(1000)        
            pygame.display.update() 
            canvas.blit(n2, (0, 0))
            pygame.time.delay(1000)
            pygame.display.update() 
            canvas.blit(n3, (0, 0))
            pygame.time.delay(1000)
            pygame.display.update() 
            canvas.blit(n4, (0, 0))
            pygame.time.delay(1000)
            pygame.display.update() 
            canvas.blit(n5, (0, 0))
            pygame.time.delay(1000)
            pygame.display.update()  
            canvas.blit(bg, (0, 0))
            canvas.blit(button, (350, 330))
            fillText('游戏继续', (420, 100))
            pygame.time.delay(1000)
            pygame.display.update() 
            a = a + 100    
        elif a == 500:
            canvas.blit(bg, (0, 0))
            lastTime = time.time()    
            isIntervalTime(lastTime)
                                
def fillText(text, position):
    # 设置字体
    TextFont = pygame.font.Font('fonts/font3.ttf', 40)
    # 设置字体其他样式
    newText = TextFont.render(text, True, (255, 255, 255))
    canvas.blit(newText, position)  

canvas.blit(bg, (0, 0))
canvas.blit(button, (350, 330))
startTime = 0
endTime = 0
interval = 20
def isIntervalTime(lastTime):
    if int(lastTime - startTime) >= interval - 5 and int(lastTime - startTime) <= interval + 5:
        fillText('你的感知时间为：'+ str(int(lastTime - startTime)), (330, 100))
        fillText('这么接近是魔鬼吧！', (320, 150))
        canvas.blit(king , (400, 200))
    if int(lastTime - startTime) >= interval - 10 and int(lastTime - startTime) <= interval + 10:
        fillText('你的感知时间为：'+ str(int(lastTime - startTime)), (330, 100))
        fillText('还行吧！', (320, 150))
        canvas.blit(diamond , (400, 200))
    if int(lastTime - startTime) >= interval - 15 and int(lastTime - startTime) <= interval + 15:
        fillText('你的感知时间为：'+ str(int(lastTime - startTime)), (330, 100))
        fillText('继续加油！', (320, 150))
        canvas.blit(bronze , (400, 200))
while True:
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    # 延时1秒 
    pygame.time.delay(1000)
    
    
