
import pygame, sys
import play
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption("STATION DSHS")

FPS = 60
fpsClock = pygame.time.Clock()

is_menu = True
introRunning = True
n = 7
musicIdx = 0

liness = [0 for i in range(100)]
linesss = [0 for i in range(100)]
highest = [0 for i in range(100)]
points=0
arrmusicstatus = [0 for i in range(100)]
textSurfaceObjScoret=[0 for i in range(100)]
textRectObjScoret=[0 for i in range(100)]
textSurfaceObjLevels = [0 for i in range(100)]
textRectObjLevels = [0 for i in range(100)]

pointfile = open('./doc/point.txt', 'r')
lines2 = pointfile.readline()
points=int(lines2)
pointfile.close()

imgYesNo=pygame.image.load('./image/etc/openmusic.png')

statusfile = open('./doc/musicstatus.txt', 'r')
lines6 = statusfile.readline()
lines7 = lines6.split()
for i in range(n) :
    arrmusicstatus[i] = int(lines7[i])
statusfile.close()

def InputHighest() :
    global highest
    global lines
    global liness
    global linesss
    global n
    scorefile = open('./doc/score.txt', 'r')
    lines = scorefile.readlines()
    for i in range(n):
        liness[i] = float(lines[i])
        linesss[i] = round(liness[i], 2)
        highest[i] = linesss[i]
    scorefile.close()
    levelfile = open('./doc/musiclevel.txt', 'r')
    lineswow = levelfile.readline()
    lines = lineswow.split()
    for i in range(n) :
        liness[i] = int(lines[i])

InputHighest()
BLACK=(0,0,0)
fontObj1 = pygame.font.Font(None,15)
fontObj2 = pygame.font.Font(None,25)
fontObj3 = pygame.font.Font(None,30)
textSurfaceObjPoints = fontObj1.render(str(points) + ' p', True, BLACK)
textRectObjPoints = textSurfaceObjPoints.get_rect();
textRectObjPoints.center = (123,22)
for i in range(n) :
    textSurfaceObjScoret[i] = fontObj2.render(str(highest[i]) + ' %', True, BLACK)
    textRectObjScoret[i] = textSurfaceObjScoret[i].get_rect();
    textRectObjScoret[i].center = (180,340)
for i in range(n) :
    textSurfaceObjLevels[i] = fontObj3.render('LV.' + str(liness[i]), True, BLACK)
    textRectObjLevels[i] = textSurfaceObjLevels[i].get_rect();
    textRectObjLevels[i].center = (254,133)

try:
    startimg = pygame.image.load("./image/starting/gamestart.png")
    tipimg = pygame.image.load("./image/starting/gametip.png")
    musicimg1 = []
    for i in range(n):
        musicimg1.append(pygame.image.load("./image/starting/music" + str(i) + ".png"))
    musicimg2 = []
    for i in range(n) :
        musicimg2.append(pygame.image.load('./image/starting/lmusic' + str(i) + '.png'))
    soundObjKwang = pygame.mixer.Sound('./sound/effects/kwang.wav')
except Exception as err:
    print("파일 로드 실패: ", err)

def PointOnScreen() :
    global textSurfaceObjPoints
    global textRectObjPoints
    global fontObj1
    filepoint = open('./doc/point.txt', 'r')
    lines8 = filepoint.readline()
    lines9 = int(lines8)
    points = lines9
    textSurfaceObjPoints = fontObj1.render(str(points) + ' p', True, BLACK)
    textRectObjPoints = textSurfaceObjPoints.get_rect();
    textRectObjPoints.center = (123, 22)

def tip(screen):
    global is_menu
    screen.blit(tipimg, (0, 0))
    pygame.display.update()
    while not is_menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if mouse[0] in range(275, 325):
                    if mouse[1] in range(425, 475):
                        soundObjKwang.play()
                        is_menu = True
            if event.type == KEYDOWN :
                if event.key == K_x :
                    soundObjKwang.play()
                    is_menu = True

def game_intro(screen):
    global is_menu
    global introRunning
    screen.blit(startimg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if mouse[0] in range(70, 285):
                if mouse[1] in range(415, 465):
                    soundObjKwang.play()
                    is_menu = False
                    tip(screen)
            if mouse[0] in range(70, 285):
                if mouse[1] in range(350, 400):
                    soundObjKwang.play()
                    introRunning = False
        if event.type == KEYDOWN :
            if event.key == K_q :
                pygame.quit()
                sys.exit()
            if event.key == K_s :
                soundObjKwang.play()
                introRunning = False
            if event.key == K_t :
                soundObjKwang.play()
                is_menu = False
                tip(screen)


def selMusic(screen):
    global n
    global musicIdx
    global points
    global textSurfaceObjPoints
    global textRectObjPoints
    global fontObj1
    global arrmusicstatus
    global textRectObjScoret
    global textSurfaceObjScoret
    k=0
    lines3 = [0 for i in range(100)]
    filemusicstate = open('./doc/musicstate.txt', 'r')
    lines=filemusicstate.readline()
    lines2=lines.split()
    for i in range(n) :
        lines3[i] = int(lines2[i])
    filemusicstate.close()
    PointOnScreen()
    InputHighest()
    screen.blit(textSurfaceObjScoret[musicIdx], textRectObjScoret[musicIdx])
    screen.blit(textSurfaceObjLevels[musicIdx], textRectObjLevels[musicIdx])
    pygame.display.update()
    selectRunning = True
    while selectRunning:
        if k == 1 :
            if points >= arrmusicstatus[musicIdx]:
                for event in pygame.event.get() :
                    if event.type == QUIT :
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONUP :
                        position = pygame.mouse.get_pos()
                        if position[0] in range(95, 244) :
                            if position[1] in range(228,255) :
                                k = 0
                                points -= arrmusicstatus[musicIdx]
                                filepoint = open('./doc/point.txt', 'w')
                                filepoint.write(str(points))
                                filepoint.close()
                                PointOnScreen()
                                lines3[musicIdx] = 1
                                filemusicstate = open('./doc/musicstate.txt', 'w')
                                for i in range(n):
                                    filemusicstate.write(str(lines3[i]))
                                    if i != n - 1:
                                        filemusicstate.write(' ')
                            if position[1] in range(268,293) :
                                k = 0
        if lines3[musicIdx] == 0 :
            screen.blit(musicimg2[musicIdx], (0, 0))
        else :
            screen.blit(musicimg1[musicIdx], (0, 0))
            InputHighest()
            screen.blit(textSurfaceObjScoret[musicIdx], textRectObjScoret[musicIdx])
        screen.blit(textSurfaceObjLevels[musicIdx], textRectObjLevels[musicIdx])
        screen.blit(textSurfaceObjPoints, textRectObjPoints)
        if k == 1 :
            screen.blit(imgYesNo, (60, 160))
        pygame.display.update()
        if k == 0 :
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    if lines3[musicIdx] == 1 :
                        if mouse[0] in range(120, 400):
                            if mouse[1] in range(365, 450):
                                soundObjKwang.stop()
                                soundObjKwang.play()
                                selectRunning = False
                    if lines3[musicIdx] == 0 :
                        if mouse[0] in range(120, 400):
                            if mouse[1] in range(365, 450):
                                if points >= arrmusicstatus[musicIdx] :
                                    k = 1
                    if mouse[0] in range(5, 60):
                        if mouse[1] in range(190, 245):
                            if musicIdx == 0:
                                musicIdx = n - 1
                            else:
                                musicIdx -= 1
                            soundObjKwang.play()
                    if mouse[0] in range(290, 345):
                        if mouse[1] in range(190, 245):
                            if musicIdx == n - 1:
                                musicIdx = 0
                            else:
                                musicIdx += 1
                            soundObjKwang.play()
                if event.type == KEYDOWN :
                    if event.key == K_p :
                        soundObjKwang.stop()
                        soundObjKwang.play()
                        selectRunning = False
                    if event.key == K_o :
                        if lines3[musicIdx] == 0:
                            if points >= arrmusicstatus[musicIdx]:
                                points -= arrmusicstatus[musicIdx]
                                filepoint = open('./doc/point.txt', 'w')
                                filepoint.write(str(points))
                                filepoint.close()
                                PointOnScreen()
                                lines3[musicIdx] = 1
                                filemusicstate = open('./doc/musicstate.txt', 'w')
                                for i in range(n):
                                    filemusicstate.write(str(lines3[i]))
                                    if i != n - 1:
                                        filemusicstate.write(' ')


while 1 :
    InputHighest()
    for i in range(n):
        textSurfaceObjScoret[i] = fontObj2.render(str(highest[i]) + ' %', True, BLACK)
        textRectObjScoret[i] = textSurfaceObjScoret[i].get_rect();
        textRectObjScoret[i].center = (180, 340)
    while introRunning:
        if is_menu:
            game_intro(screen)
    selMusic(screen)
    play.main(musicIdx,n)
    introRunning = True
