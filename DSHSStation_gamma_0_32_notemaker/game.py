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
n = 3
musicIdx = 0

liness = [0 for i in range(100)]
linesss = [0 for i in range(100)]
highest = [0 for i in range(100)]
points=0
arrmusicstatus = [0 for i in range(100)]

scorefile = open('./doc/score.txt', 'r')
lines=scorefile.readlines()
for i in range(3) :
    liness[i] = float(lines[i])
    linesss[i] = round(liness[i], 2)
    highest[i] = linesss[i]
scorefile.close()

pointfile = open('./doc/point.txt', 'r')
lines2 = pointfile.readline()
points=int(lines2)
pointfile.close()

statusfile = open('./doc/musicstatus.txt', 'r')
lines6 = statusfile.readline()
lines7 = lines6.split()
print(lines7)
for i in range(3) :
    arrmusicstatus[i] = int(lines7[i])
statusfile.close()

BLACK=(0,0,0)
fontObj1 = pygame.font.Font(None,15)
fontObj2 = pygame.font.Font(None,25)
textSurfaceObjPoints = fontObj1.render(str(points) + ' p', True, BLACK)
textRectObjPoints = textSurfaceObjPoints.get_rect();
textRectObjPoints.center = (123,22)
textSurfaceObjScoret1 = fontObj2.render(str(highest[0]) + ' %', True, BLACK)
textRectObjScoret1 = textSurfaceObjScoret1.get_rect();
textRectObjScoret1.center = (180,340)
textSurfaceObjScoret2 = fontObj2.render(str(highest[1]) + ' %',True,BLACK)
textRectObjScoret2 = textSurfaceObjScoret2.get_rect();
textRectObjScoret2.center = (180,340)
textSurfaceObjScoret3 = fontObj2.render(str(highest[2]) + ' %',True,BLACK)
textRectObjScoret3 = textSurfaceObjScoret1.get_rect();
textRectObjScoret3.center = (180,340)

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


def selMusic(screen):
    global n
    global musicIdx
    global points
    global textSurfaceObjPoints
    global textRectObjPoints
    global fontObj1
    global arrmusicstatus
    lines3 = [0 for i in range(100)]
    filemusicstate = open('./doc/musicstate.txt', 'r')
    lines=filemusicstate.readline()
    lines2=lines.split()
    for i in range(3) :
        lines3[i] = int(lines2[i])
    print(lines3)
    filemusicstate.close()
    screen.blit(musicimg1[0], (0, 0))
    screen.blit(textSurfaceObjPoints, textRectObjPoints)
    if musicIdx == 0 :
        screen.blit(textSurfaceObjScoret1, textRectObjScoret1)
    if musicIdx == 1 :
        screen.blit(textSurfaceObjScoret2, textRectObjScoret2)
    if musicIdx == 2 :
        screen.blit(textSurfaceObjScoret3, textRectObjScoret3)
    pygame.display.update()
    selectRunning = True
    while selectRunning:
        if lines3[musicIdx] == 0 :
            screen.blit(musicimg2[musicIdx], (0, 0))
        else :
            screen.blit(musicimg1[musicIdx], (0, 0))
            if musicIdx == 0:
                screen.blit(textSurfaceObjScoret1, textRectObjScoret1)
            if musicIdx == 1:
                screen.blit(textSurfaceObjScoret2, textRectObjScoret2)
            if musicIdx == 2:
                screen.blit(textSurfaceObjScoret3, textRectObjScoret3)
        screen.blit(textSurfaceObjPoints, textRectObjPoints)
        pygame.display.update()
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
                                points -= arrmusicstatus[musicIdx]
                                filepoint = open('./doc/point.txt', 'w')
                                filepoint.write(str(points))
                                filepoint.close()
                                textSurfaceObjPoints = fontObj1.render(str(points) + ' p', True, BLACK)
                                textRectObjPoints = textSurfaceObjPoints.get_rect();
                                textRectObjPoints.center = (123, 22)
                                lines3[musicIdx] = 1
                                filemusicstate = open('./doc/musicstate.txt', 'w')
                                for i in range(3) :
                                    filemusicstate.write(str(lines3[i]))
                                    if i != 2 :
                                        filemusicstate.write(' ')
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

while 1 :
    while introRunning:
        if is_menu:
            game_intro(screen)
    selMusic(screen)
    print(musicIdx)
    play.main(musicIdx)
    introRunning = True
