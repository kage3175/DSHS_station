import pygame, sys
from pygame.locals import *
import random as ran
import time

''' 
제작자가 주석에다가 약을 빨아놨어요!!
뱢뎌ㅑ개벼쟈ㅐ더랴ㅐㅏㅁㄴㅇ
정상적인 주석은 유료! 입니다! 돈 내놔...
얼마?
100마넌... 싫음 말고... 아니면...
하악하악 내게 가르침을 줘
ㅈㅅ...
마약 신고는 117... 아니 113인가? 몰라 114에 물어봐.(127 이랍니다)
26*2 김준* : '네? 그런 전화는 없다구요? 신기하네요.'
사실 시험 기간에 놀고 싶은데 대놓고 못 놀아서 이러고 노는 중 ㅠ.ㅠ
'''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # 이거 인종 차별 아닙니까? discriminatory!!!!!!! 하하하하하하 나 영어 잘하지 하하하하하하핳핳핳...

def ScoreChange(n, d):  # 스코어를 계산해주는 함수 여기에서 perfect, great, miss의 개수도 센다.
    global JudgeNote # 얘네들의
    global score # 쓰임새가
    global great # 궁금하시다구요?
    global miss # main 함수에 가셔서
    global perfect # 일일이 찾아보셔요
    global combo # 매우 귀찮을꺼야 껄껄... 나도 귀찮아서 두 번 안 쓴겁니다.
    k = 0
    if abs(358 - n) >= 10 and abs(358 - n) < 42:  # great의 경우, 오차가 약 0.16초에서 0.7초 사이일 때 판정된다. 점수는 아래와 같이 계산한다.
        score += 100 * (
        (1 / d) * ((((42 - abs(n - 358)) / 42) * 0.65625) + 0.4))  # 오차의 정도에 따라 perfect 점수의 40%~90%를 부여한다.
        great += 1  # great에 1 더해줌
        JudgeNote = 2
        combo += 1
    if abs(358 - n) >= 42:  # 오차가 너무 크면 miss 처리해준다. miss를 해도 감점은 없으나 가점도 없다.
        score += 0
        miss += 1
        JudgeNote = 1
        combo = 0
    if abs(358 - n) < 10:  # 오차가 약 0.16초 미만일 경우 판정된다.
        score += 100 * (1 / d)  # 점수에 (100/(전체 노트 수)) 만큼을 가산한다. ALL PERFECT의 경우 점수는 100%가 된다.
        perfect += 1
        JudgeNote = 3
        combo += 1
    k = round(score, 2)  # 소수점 이하 자릿수가 너무 많을 경우 보기 불편하므로 셋째자리에서 반올림한다.
    return k


def ShowJudgement(x):
    global JudgeNote # miss, great, perfect 에 대한 정보를 담고 있는 int형 글로벌 변수
    global textSurfaceObj3 # 나머지는
    global textRectObj3 # main 함수에
    global textSurfaceObj4 # 친절히
    global textRectObj4 # 아니면 불친절 할수도?
    global combo # 어쨌든 설명 되어 있는 글로벌 변수들이니
    global CountPerfectTime # 거기 가서
    global CountGreatTime # 스스로 찾아보시고
    global CountMissTime # 자기주도적 학습을 하는 대곽인이 됩시다!
    if JudgeNote == 3 : # 얘는 아마 perfect 눌렸으면 일걸요? 위에 ScoreChange에서도 JudgeNote 변수로 장난치니까 스.스.로. 알아 보세요^^
        textSurfaceObj3 = fontObj.render('Perfect', True, BLACK) # Perfect를 출력하는가보네요.
        textRectObj3 = textSurfaceObj3.get_rect();
        textRectObj3.center = (250, 230)
        textSurfaceObj4 = fontObj.render(str(combo) + ' Combo', True, BLACK) # 세상에! 콤보도!
        textRectObj4 = textSurfaceObj4.get_rect();
        textRectObj4.center = (250, 270)
        CountPerfectTime[x]=10 # 얘는 뭐냐구요? 에... 키 눌렀을 때 이펙트 처리 할 때 쓰는 전역 변수 친구랍니다
    elif JudgeNote == 2 :
        textSurfaceObj3 = fontObj.render('Great', True, BLACK)
        textRectObj3 = textSurfaceObj3.get_rect();
        textRectObj3.center = (250, 230)
        textSurfaceObj4 = fontObj.render(str(combo) + ' Combo', True, BLACK)
        textRectObj4 = textSurfaceObj4.get_rect();
        textRectObj4.center = (250, 270)
        CountGreatTime[x]=10
    else :
        textSurfaceObj3 = fontObj.render('Miss', True, BLACK)
        textRectObj3 = textSurfaceObj3.get_rect();
        textRectObj3.center = (250, 230)
        textSurfaceObj4 = fontObj.render(str(combo) + ' Combo', True, BLACK)
        textRectObj4 = textSurfaceObj4.get_rect();
        textRectObj4.center = (250, 270)
        CountMissTime[x]=10


def ShowScore(n): # 참 짧고 좋은 함수죠? 사실 짧은만큼 하는게 없긴 해요... 그냥 score 출력하는 셔틀
    global textRectObj2
    global textSurfaceObj2
    textSurfaceObj2 = fontObj.render('Score : ' + str(n) + ' %', True, BLACK)
    textRectObj2 = textSurfaceObj2.get_rect();
    textRectObj2.center = (250, 200)


pygame.init() # pygame 시작은 해야 코드가 돌아가던 눕던 뒤집어지던 하겄죠잉?
screen = pygame.display.set_mode((350, 500)) # 스크린 크기가 350,500 이랍니다.
pygame.display.set_caption('DSHSStation_gamma_0.24_revised') # 크~ 뭔가 간지 '안' 나는 이름

fps = 60  # fps 값을 60으로 맞춘다. 컴퓨터의 성능이 그닥 좋지 않을 경우 플레이가 힘들 수도 있다. --- 근데 60 이하로 하면 게임이 너무 뚝뚝 끊겨서 할 맛이 안남... 그럼 무슨 맛이 나냐고? 시큼한 맛임
fpsClock = pygame.time.Clock() # 이거 기능 아직도 모르겠다 손! 사실 나도 모르거든...ㅎㅎ

def main(idx) : # 드디어! 100줄만에! main 함수 입성!
    global score # 게임 후 스코어 입출력에 필요한 변수
    global fontObj # 기본 폰트(큰 폰트)
    global textRectObj2 # 스코어 표시하는 텍스트 창
    global textSurfaceObj2 # 위와 마찬가지
    global combo # 콤보수 입출력에 필요한 변수
    global JudgeNote # 타격한 노트가 perfect 인지 great 인지 miss 인지 판별할 때 쓰이는 변수
    global great # 그 게임 동안의 great 수를 세준다
    global perfect # 위 변수와 유사
    global miss # 위 변수와 유사
    global textSurfaceObj3 # 노트 판정을 화면에 보여주는(오른쪽에)데 필요한 변수
    global textRectObj3 # 위와 마찬가지
    global textSurfaceObj4 # 콤보수를 화면에 보여주는데 필요한 변수
    global textRectObj4 # 위와 마찬가지
    global CountPerfectTime # perfect 이펙트를 출력할 때 중요한 리스트 변수이다.
    global CountGreatTime # great 이펙트를 출력할 때 중요한 리스트 변수이다.
    global CountMissTime # miss 이펙트를 출력할 때 중요한 리스트 변수이다.
    global CountNothingTime # 위 세 개의 이펙트가 아닐 때 타격하면 출력되는 이펙트를 출력할 때 중요한 리스트 변수이다.
    global cnt
    CountMissTime=[0 for i in range(3)]
    CountGreatTime=[0 for i in range(3)]
    CountPerfectTime=[0 for i in range(3)]
    CountNothingTime=[0 for i in range(3)] # 요 네 개는 글로벌 변수에 설명 붙어있다.
    LeftOrder=1
    RightOrder=1
    DownOrder=1 # 이 세 개의 변수는 키를 한 번 누를 때 타격 판정이 한 번만 이루어지도록 할 때 필요한 변수들이다.
    Pausei = 0
    global Quiti
    Quiti = 0
    aaa=1 # 특수 노트 생성 시 랜덤 수 생성에 쓰일 변수
    JudgeNote = 1 # 글로별 변수 부분에 설명이 쓰여있다.
    i = 0
    n = 0
    pausecheck = 0
    k = 0
    kk=0
    temp = 0
    j = 0 # 여기저기에 쓰일 temp 변수들이다. 주로 for문...
    SongDictionary = 0 # 곡 목록에서 곡을 선택할 때 쓰일 변수이다.
    running=True #말 안해도 알겠지?
    great = 0 # 더 이상의 자세한 설명은 생략한다.
    perfect = 0 # 우후훗
    SongSelect1="./sound/songs/" # 곡 선택에 쓰일 변수이다.
    miss = 0  # great, miss, perfect의 개수를 셀 변수들이다.
    combo = 0  # 콤보 계산에 쓰일 변수이다.
    score = 0.00  # score 계산에 필요한 변수이다.
    LEFT = 1 # 마우스 클릭 위치 판별에 쓰이는 고정값
    highest=[0 for i in range(100)] # 해당 곡의 최고점수를 받아올 때 필요한 리스트이다.
    imgg = [0 for i in range(1000)]  # 노트의 이미지를 불러오는 리스트이다.
    x = [10 for i in range(1000)]  # 노트의 x좌표 위치를 가리킬 리스트이다.
    y = [10 for i in range(1000)]  # 노트의 y좌표 위치를 가리킬 리스트이다.
    z = [0 for i in range(1000)] # 특수 노트일 경우 포인트를 추가시킬 때 쓰이는 리스트이다.
    m = [1 for i in range(3)]  # 1,2,3 각 레인의 노트의 순번(?)과 타격 시 판정에 중요한 리스트이다.
    di = [0 for i in range(600)] # 특정 곡의 딕셔너리
    c = [0 for i in range(1000)] # 나도 뭔지 모르겠다. 일단 건드리지 말자.
    liness=[0 for i in range(100)] # 외부에서 스코어 불러올 때 쓰이는 변수
    linesss=[0 for i in range(100)] # 위와 마찬가지(사실 이름 짓기 귀찮아서 s 늘려가는 거 ㅋㅋ)
    track3note=[0 for i in range(100000)]
    zz=[0 for i in range(3)]
    string1=''
    temp2=0

    '''di[0] = {'n': 87}  # 4n꼴로 시작. 노트의 수에 관한 딕셔너리이다.
    di[1] = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 2, 7: 0, 8: 0, 9: 1, 10: 1, 11: 0, 12: 0, 13: 2, 14: 1, 15: 0, 16: 2,
             17: 2, 18: 1, 19: 1, 20: 1, 21: 0, 22: 1, 23: 2, 24: 0, 25: 1, 26: 2, 27: 0, 28: 1, 29: 2, 30: 0, 31: 1, 32: 2,
             33: 0, 34: 1, 35: 2, 36: 0, 37: 1, 38: 2, 39: 0, 40: 1, 41: 2, 42: 0, 43: 1, 44: 2, 45: 0, 46: 1, 47: 2, 48: 0,
             49: 1, 50: 2, 51: 0, 52: 1, 53: 2, 54: 0, 55: 1, 56: 2, 57: 0, 58: 1, 59: 2, 60: 0, 61: 1, 62: 2, 63: 0, 64: 1,
             65: 2, 66: 0, 67: 1, 68: 2, 69: 0, 70: 1, 71: 2, 72: 0, 73: 1, 74: 2, 75: 0, 76: 1, 77: 2, 78: 0, 79: 1, 80: 2,
             81: 0, 82: 1, 83: 2, 84: 0, 85: 1, 86: 2}  # 노트의 레인 정보에 관한 딕셔너리이다.
    di[2] = {0:1, 1:1, 2:2, 3:1, 4:3, 5:4, 6:2, 7:2, 8:3, 9:5, 10:6, 11:4, 12:5, 13:3, 14:7, 15:6, 16:4,
             17:5, 18:8, 19:9, 20:10, 21:8, 22:11, 23:6, 24:9, 25:12, 26:7, 27:10, 28:13, 29:8, 30:11, 31:14, 32:9,
             33:12, 34:15, 35:10, 36:13, 37:16, 38:11, 39:14, 40:17, 41:12, 42:15, 43:18, 44:13, 45:16, 46:19, 47:14, 48:17,
             49:20, 50:15, 51:18, 52:21, 53:16, 54:19, 55:22, 56:17, 57:20, 58:23, 59:18, 60:21, 61:24, 62:19, 63:22, 64:25,
             65:20, 66:23, 67:26, 68:21, 69:24, 70:27, 71:22, 72:25, 73:28, 74:23, 75:26, 76:29, 77:24, 78:27, 79:30, 80:25,
             81:28, 82:31, 83:26, 84:29, 85:32, 86:27} # 각 번호의 노트가 해당 레인에서 몇 번째 노트인지에 대한 딕셔너리이다.
    di[3] = {0: 355, 1: 374, 2: 392, 3: 409, 4: 425, 5: 442, 6: 460, 7: 476, 8: 493, 9: 509, 10: 527, 11: 544, 12: 560,
             13: 576, 14: 592, 15: 610, 16: 626, 17: 642, 18: 657, 19: 674, 20: 691, 21: 707, 22: 725, 23: 755, 24: 820,
             25: 836, 26: 853, 27: 869, 28: 887, 29: 903, 30: 919, 31: 936, 32: 952, 33: 968, 34: 983, 35: 999, 36: 1014,
             37: 1031, 38: 1039, 39: 1057, 40: 1073, 41: 1081, 42: 1148, 43: 1155, 44: 1164, 45: 1172, 46: 1180, 47: 1187,
             48: 1191, 49: 1198, 50: 1205, 51: 1214, 52: 1222, 53: 1230, 54: 1238, 55: 1245, 56: 1253, 57: 1261, 58: 1270,
             59: 1278, 60: 1286, 61: 1293, 62: 1303, 63: 1321, 64: 1328, 65: 1338, 66: 1352, 67: 1340, 68: 1348, 69: 1356,
             70: 1365, 71: 1371, 72: 1378, 73: 1388, 74: 1396, 75: 1404, 76: 1422, 77: 1429, 78: 1437, 79: 1447, 80: 1456,
             81: 1462, 82: 1471, 83: 1479, 84: 1489, 85: 1506, 86: 1513}  # 노트가 떨어지는 시점에 관한 딕셔너리이다.
    di[4] = {'n' : 31}
    di[5] = {0: 0, 1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0, 7: 1, 8: 2, 9: 0, 10: 1, 11: 2, 12: 0, 13: 1, 14: 2, 15: 0, 16: 1,
             17: 2, 18: 0, 19: 1, 20: 2, 21: 0, 22: 1, 23: 2, 24: 0, 25: 1, 26: 2, 27: 0, 28: 1, 29: 2, 30: 0}
    di[6] = {0:1, 1:1, 2:1, 3:2, 4:2, 5:2, 6:3, 7:3, 8:3, 9:4, 10:4,11:4, 12:5, 13:5, 14:5, 15:6, 16:6,
             17:6, 18:7, 19:7, 20:7, 21:8, 22:8, 23:8, 24:9, 25:9, 26:9, 27:10, 28:10, 29:10, 30:11}
    di[7] = { 0: 242, 1 : 253, 2: 264, 3: 275, 4: 372, 5: 383, 6: 394, 7: 426, 8: 437,
             9 : 448, 10: 459, 11: 490, 12: 501, 13: 512, 14: 523, 15: 555, 16: 566, 17: 577, 18: 588, 19: 621, 20: 632,
             21: 643, 22: 654, 23: 685, 24: 717, 25: 748, 26: 763, 27: 778, 28: 809, 29: 841, 30: 872}'''
    di[8] = {'n' : 1}
    di[9] = {0 : 0}
    di[10] = {0 : 1}
    di[11] = {0 : 50000}
    di[0] = {'n' : 1}
    di[1] = {0 : 0}
    di[2] = {0 : 1}
    di[3] = {0 : 50000}
    di[4] = {'n' : 1}
    di[5] = {0 : 0}
    di[6] = {0 : 1}
    di[7] = {0 : 50000}
#111 122 133 144 242 253 264 275 372 383 394 426 437 448 459
#490 501 512 523 555 566 577 588 621 632 643 654 685 717 748
#763 778 809 841 872 14.5초 부근까지


    for i in range(di[idx*4+0]['n']):  # 총 노트의 수만큼 for문을 돌려서 각 노트의 x 좌표값을 알맞게 바꿔준다.
        x[i] = 10 + 60 * (di[idx*4+1][i])

    infilescore=open("./doc/score.txt","r") # 파일을 읽어들여 각 곡의 스코어를 읽는다.
    lines=infilescore.readlines() # 더 이상의
    for i in range(3) :
        liness[i]=float(lines[i]) # 자세한 설명은
        linesss[i]=round(liness[i],2) # 생략하겠네
        highest[i] = linesss[i]  # main 함수 내에서, 최고 점수보다 높은 점수를 기록 했을 경우에만 종전 기록을 말소하고 이번 기록을 넣을 수 있게 판정하는 데에 쓰인다.
    infilescore.close() # 어리석은 중생들이여

    infilepoint=open("./doc/point.txt", "r") # 파일을 읽어들여 현재 가지고 있는 포인트를 불러온다.
    lines2=infilepoint.readline() # 여기 포함 이하 3줄은
    points=int(lines2) # 알아서 해석하게나
    infilepoint.close() # 어리석은 중생들이여
    infilenotenum=open('./doc/notenum.txt', 'r')
    linesnum=infilenotenum.readline()
    linesnum2=linesnum.split()
    n=int(linesnum2[idx])
    infilenoteinf=open('./doc/track'+str(idx+1)+'_note.txt')
    linesinf=infilenoteinf.readline()
    linesinf2=linesinf.split()
    infilenoteinf.close()

    for i in range(1):  # imgg 리스트에 노트의 이미지를 불러와준다.
        aaa=ran.randint(1,1000) # 랜덤 자연수 생성임을 모르는 무지한 이가 있겠는가
        if aaa > 3 : # 매우 큰 확률이라네. 대충 997/1000 쯤? 맞나? 랜덤 생성 메커니즘은 몰라서...
            imgg[i] = pygame.image.load('./image/note/t1.png')
            z[i] = 0 # 이미지는 윗줄에서 바꿨지만 그걸 컴퓨터가 인식할 수는 없으니까... 이짓 추가로 해줘서 판별하게 해야함. 나중가면 알게 될 거 ㅇㅇ
        elif aaa>0 :
            imgg[i] = pygame.image.loae('./image/note/t2.png')
            z[i] = 3
        else : # 위에꺼의 여집합이니까... 알지? 그냥 확률 *되게 작은 거야. 난 너희에게 포인트 많이 주기 싫거든
            imgg[i] = pygame.image.load('./image/note/t3.png')
            z[i] = 1 # 난 두 번 설명하는 걸 정말 싫어하지

    cnt = 0  # 시간 정보(지나간 프레임을 이용한)를 담고 있는 변수이다. 노트 낙하, 점수 판정 등에 쓰일 것이다.
    imgPerfect_1=pygame.image.load('./image/effect/perfect_1.png') # 퍼펙트 판정 시 출력될 이펙트이다.
    imgPerfect_2=pygame.image.load('./image/effect/perfect_2.png') # 대충 보고 눈치 까셈 ㅇㅋ?
    imgPerfect_3=pygame.image.load('./image/effect/perfect_3.png') # 내가
    imgPerfect_4=pygame.image.load('./image/effect/perfect_4.png')
    imgMiss_1 = pygame.image.load('./image/effect/miss_1.png') # 굳이
    imgMiss_2 = pygame.image.load('./image/effect/miss_2.png') # 이 많은
    imgMiss_3 = pygame.image.load('./image/effect/miss_3.png') # 변수들을
    imgMiss_4 = pygame.image.load('./image/effect/miss_4.png')
    imgGreat_1 = pygame.image.load('./image/effect/great_1.png') # 하나하나
    imgGreat_2 = pygame.image.load('./image/effect/great_2.png') # 설명해줄
    imgGreat_3 = pygame.image.load('./image/effect/great_3.png') # 필요는
    imgGreat_4 = pygame.image.load('./image/effect/great_4.png')
    imgNothing_1 = pygame.image.load('./image/effect/nothing_1.png') # 없어보이지?
    imgNothing_2 = pygame.image.load('./image/effect/nothing_2.png') # 나도 좀 편하게 살자
    imgNothing_3 = pygame.image.load('./image/effect/nothing_3.png') # 후
    imgNothing_4 = pygame.image.load('./image/effect/nothing_4.png')
    descriptionImg=pygame.image.load("./image/description/t1_description"+str(idx)+".png") # 요건 곡에 대한 설명 사진 불러오는 거
    imgPause = pygame.image.load('./image/etc/ingamepause.png')
    imgPaused = pygame.image.load('./image/etc/ingamepaused.png')

    fontObj = pygame.font.Font(None, 26) # 기본 폰트 1
    fontObj2 = pygame.font.Font(None, 15) # 기본 폰트 2
    fontObj3 = pygame.font.Font(None, 40)
    textSurfaceObj1 = fontObj.render('Press Q to Quit', True, BLACK) # 그냥 설명해주는 거 출력. Q 누르면 나간다고
    textRectObj1 = textSurfaceObj1.get_rect();
    textRectObj1.center = (250, 150)
    textSurfaceObj2 = fontObj.render('Score : ' + str(score) + ' %', True, BLACK)  # 점수를 나타내는 텍스트이다.
    textRectObj2 = textSurfaceObj2.get_rect();
    textRectObj2.center = (250, 190)
    textSurfaceObj3 = fontObj.render('-', True, BLACK) # 자세한 설명은 글로벌 변수쪽에
    textRectObj3 = textSurfaceObj3.get_rect();
    textRectObj3.center = (250, 230)
    textSurfaceObj4 = fontObj.render(' Combo', True, BLACK) # 얘도 글로벌 변수쪽에
    textRectObj4 = textSurfaceObj4.get_rect();
    textRectObj4.center = (250, 270)
    textSurfaceObj5 = fontObj2.render('La Campanella', True, BLACK) # 곡명 친절히 출력해주고... 가 아니라 0.22? 0.21? 버전부턴 이 변수 안 쓰입니다. 그냥 추억으로 남겨둡시다.
    textRectObj5 = textSurfaceObj5.get_rect();
    textRectObj5.center = (85,60)
    textSurfaceObj5_1 = fontObj2.render(str(linesss[0])+' %',True,BLACK) # 얘도 안 쓰이는데... 난 한다 좋아하는 추억 둔다 본다 남겨서 두고두고... Waldo 체 머단해
    textRectObj5_1=textSurfaceObj5_1.get_rect();
    textRectObj5_1.center = (160,60)
    while 1 : # 설명문 출력해주는 겁나 간단한 코드임. 짧으니까 알아서 해석해
        screen.fill(WHITE) # 라고 윗줄에서 말해놓곤 찔려서 주석 추가로 답니다. 저 일 열심히 해요... ㅎㅎ
        for event in pygame.event.get() :
            if event.type==MOUSEBUTTONDOWN and event.button==LEFT : # 마우스 왼쪽 클릭하면
                position=pygame.mouse.get_pos() # 위치 받아와서
                if (position[0] in range(120,230)) and (position[1] in range(430,480)) : #position[0]>=120 and position[0]<=230 and position[1]>=430 and position[1]<=480 : # 그 위치가 요 정도 되어주시면 아래 있는 코드 실행해주시고
                    SongSelect = SongSelect1 + "track" + str(idx+1) + ".wav"  # 곡 선택에 쓰일 변수이다.
                    SongDictionary=idx
                    print(SongDictionary)
                    j=1
                    break
                else :
                    continue
            if event.type==KEYDOWN : # 여기서 나갈 사람 얼마나 있겠냐만은... 일단 탈출구는 만들어둬야지
                if event.key == K_q:  # pygame 창을 종료한다.
                    print("PERFECT : " + str(perfect) + " GREAT : " + str(great) + " MISS : " + str(miss))
                    pygame.quit()
                    sys.exit()
                else :
                    continue
            if event.type==QUIT : # Q랑 같은 역할이다. 나도 왜 이걸 따로 만들었는지 기억이 가물가물... 아... 0.1 버전 때는 버그 때문에 이거 안 먹어서 Q를 따로 만든거였어용ㅎㅎ 지금은 잘 먹음
                print("PERFECT : " + str(perfect) + " GREAT : " + str(great) + " MISS : " + str(miss))
                pygame.quit()
                sys.exit()
        if j==1 :
            j=0
            break
        screen.blit(descriptionImg, (0,0)) # 설명 사진 출력해주시고
        pygame.display.flip() # 화면 업데이트... 맞나? 나도 몰라. 걍 씀.

    pygame.mixer.music.load(SongSelect)  # 재생할 음악을 받아온다. 지금은 '라 캄파넬라'이다.
    pygame.mixer.music.play() # 음악 고고씽~

    while running : # running은 뭐다? TRUE다!<< 어허 이 사람 큰 일 낼 사람일세... True 지 TRUE 가 아니라우. TRUE 쓰면 오류남... ㄹㅇ? 사실 나도 모름 ㅎㅎ;; 걍 1 쓰는 것보다 깐지나 보여서 running 쓰는 거임... 딱히 의미 없고
        screen.fill(WHITE) # 화면은 흰색으로 채우는 게 정신병원 벽면 같아서 보기 좋잖어?
        pygame.draw.line(screen, BLACK, (0, 362), (350, 362), 1)  # 노트의 판정 기준선이다.
        if Pausei == 0 :
            for i in range(1):
                if y[i] <= 420 and cnt >= di[SongDictionary*4+3][i]: # 아무 일도 일어나지 않으면
                    y[i] += 3 # y좌표 3씩 추가
                if y[i] > 420 and y[i] != 500:  # 노트의 y좌표가 420을 넘어가면 노트를 게임 밖으로 내보내고, miss 처리한다.
                    CountMissTime[di[4*SongDictionary+1][i]] = 10 # miss 이펙트 처리를 위해 해당 변수에 10 대입
                    y[i] = 500  # miss, great, perfect 처리된 노트는 y좌표 500으로 이동시킨다.
                    miss += 1
                    combo=0
                    if di[4*SongDictionary+1][i]==0 : # 사실 여기부터는 나도 무슨 의미인지 잘 모르는 코드가 많음... 떠오른 거 그냥 써놓고는 주석 안 달아놔서... 이 얘기를 왜 지금하냐고? 이 줄이 무슨 의미인지 나도 잘 모르니까! 깔깔깔깔깔깔
                        m[0]+=1
                    elif di[4*SongDictionary+1][i]==1:
                        m[1]+=1
                    else :
                        m[2]+=1
        for event in pygame.event.get(): # 입력 이벤트를 받는다. 사랑 Waldo체. Waldo가 뭐냐고? 나무위키 ㄱㄱ. 참신한 어체임. 프로그래밍이랑도 관련 있으니까 찾아보셈.
            if event.type==MOUSEBUTTONUP and event.button==LEFT : # 마우스 왼쪽 클릭하면
                position=pygame.mouse.get_pos() # 위치 받아와서
                if position[0] >= 300 and position[0] <= 340 and position[1] >= 0 and position[1] <= 40 :
                    if Pausei == 0 :
                        print('paused')
                        pygame.mixer.music.pause()
                        Pausei = 1
                    elif Pausei == 1 :
                        print('unpaused')
                        pygame.mixer.music.unpause()
                        Pausei = 0
            if event.type == KEYUP: # 손을 키에서 떼고 나서 그 다음에 같은 키가 눌릴 때 그것을 제대로 수행할 수 있도록
                if Pausei == 0 :
                    if event.key == K_RIGHT and RightOrder==0 : # 오른쪽 방향키를 눌렀을 때 RightOrder가 0이면(즉, 오른쪽 방향키가 눌린 상태에서 떨어지는 경우라면)
                        m[2]+=1 # 해당 레인의 노트 순번 관련해서... 여백이 부족하므로 자세한 설명은 생략한다.
                        RightOrder=1 # 이미 떨어진 상태인데 여기를 다시 오면 안되므로 변수에 저장된 값을 바꿔준다.
                    if event.key == K_LEFT and LeftOrder==0: # 내가 뭐라고 했드라
                        m[0] +=1
                        LeftOrder=1
                    if event.key == K_DOWN and DownOrder==0: # 같.은.설.명.은.두.번.하.지.않.는.다.
                        m[1] +=1
                        DownOrder=1
            if event.type == KEYDOWN: # 키를 눌렀을 때
                if Pausei == 0 :
                    if event.key == K_RIGHT: # 방향키 오른쪽
                        if RightOrder == 1 :
                            zz[2] += 1
                            track3note[temp] = cnt - 116
                            track3note[temp+1] = 2
                            track3note[temp+2] = zz[2]
                            temp+=3
                        for i in range(di[4*SongDictionary+0]['n']) : # 모든 노트를 일일이 다 검사함... 사실 귀찮아서 그러는 거긴 한데 프로그램 돌아가는 속도 저하의 가장 큰 원인이 이 줄에 있당
                            if di[4*SongDictionary+1][i] == 2 and y[i] >= 280 and y[i] <= 420:# 오른쪽 키를 눌렀을 때 세 번째 레인에서, y좌표가 280과 420 사이일 때 해당 순번의 노트를 처리하는 이벤트이다.
                                if m[2]==di[4*SongDictionary+2][i] : # 해당 순번의 노트에 대해서만 액션을 취하도록 해주는 행
                                    ShowScore(ScoreChange(y[i], di[4*SongDictionary+0]['n'])) # 위에 가서 어떤 함수인지 보고 오셔용. 참 쉽죠?
                                    ShowJudgement(2) # 얘도
                                    if z[i] : # 특수 노트인 경웅에
                                        if JudgeNote==3 or JudgeNote==2 : # perfect나 great에 성공하면
                                            points+=z[i] # 포인트를 줍니다! 참 좋죠?
                                    y[i] = 500 # 저 멀리 황천으로 보내버리고(가...가버렷!!)
                                    RightOrder=0 # 이 키가 눌렸었다!는 사실을 알리기 위해 변수를 0으로 설정해줍니다. 바로 밑 줄에서도 중요한 역할을 함
                        if RightOrder == 1 : # 음... 눌렸는데 아무 일도 일어나지 않을 때... 그러니까 노트가 없는 허공에서 방향키를 누르면 실행시킬 수 있도록
                            CountNothingTime[2]=10 # 글로벌 변수 설명하는데에 설명 되어있음
                    if event.key == K_LEFT: # 난 절대로 네버 에버 두.번.말.하.지.않.는.다.
                        if LeftOrder == 1 :
                            zz[0] += 1
                            track3note[temp] = cnt - 116
                            track3note[temp + 1] = 0
                            track3note[temp + 2] = zz[0]
                            temp += 3
                        for i in range(di[4*SongDictionary+0]['n']):
                            if di[4*SongDictionary+1][i] == 0 and y[i] >= 280 and y[i] <= 420:
                                if m[0]==di[4*SongDictionary+2][i] :
                                    ShowScore(ScoreChange(y[i], di[4*SongDictionary+0]['n']))
                                    ShowJudgement(0)
                                    if z[i] :
                                        if JudgeNote==3 or JudgeNote==2 :
                                            points+=z[i]
                                    y[i] = 500
                                    LeftOrder=0
                        if LeftOrder == 1 :
                            CountNothingTime[0]=10
                    if event.key == K_DOWN: # 난 두번만 말하지 않는 게 아니지. 세 번 말하지도 않지.
                        if DownOrder == 1 :
                            zz[1] += 1
                            track3note[temp] = cnt - 116
                            track3note[temp + 1] = 1
                            track3note[temp + 2] = zz[1]
                            temp += 3
                        for i in range(di[4*SongDictionary+0]['n']):
                            if di[4*SongDictionary+1][i] == 1 and y[i] >= 280 and y[i] <= 420:
                                if m[1]==di[4*SongDictionary+2][i] :
                                    ShowScore(ScoreChange(y[i], di[4*SongDictionary+0]['n']))
                                    ShowJudgement(1)
                                    if z[i] :
                                        if JudgeNote==3 or JudgeNote==2 :
                                            points+=z[i]
                                    y[i] = 500
                                    DownOrder = 0
                        if DownOrder == 1 :
                            CountNothingTime[1]=10
                if event.key == K_p :
                    if Pausei == 0 :
                        print('paused')
                        pygame.mixer.music.pause()
                        Pausei = 1
                    elif Pausei == 1 :
                        print('unpaused')
                        pygame.mixer.music.unpause()
                        Pausei = 0
                if event.key == K_o :
                    if Pausei == 1 :
                        if score > 90:
                            points += 2
                        if score > highest[idx]:  # 이번 기록이 종전 최고기록보다 높을 경우 최고기록을 변경해준다.
                            highest[idx] = score
                            outfilescore = open('./doc/score.txt', "w")
                            for i in range(3):
                                outfilescore.write(str(highest[i]))
                                outfilescore.write('\n')
                            outfilescore.close()
                        outfilepoint = open('./doc/point.txt', 'w')
                        outfilepoint.write(str(points))
                        outfilepoint.close()
                        pygame.mixer.music.stop()
                        Quiti = 1
                if event.key == K_q:  # pygame 창을 종료한다.
                    print("PERFECT : " + str(perfect) + " GREAT : " + str(great) + " MISS : " + str(miss))
                    outfilenoteinf = open('./doc/track' + str(idx+1) + '_note.txt', 'w')
                    temp2=temp//3
                    print(temp2)
                    print(track3note)
                    for i in range(temp2) :
                        if i != temp2 - 1 :
                            string1=string1+str(track3note[i*3])+' '+str(track3note[3*i+1])+' '+str(track3note[3*i+2])+' '
                        else :
                            string1 = string1 + str(track3note[i * 3]) + ' ' + str(track3note[3 * i + 1])+' '+str(track3note[3*i+2])
                    print(string1)
                    outfilenoteinf.write(string1)
                    outfilenoteinf.close()
                    if score>90 :
                        points+=2
                    if score>highest[idx] : # 이번 기록이 종전 최고기록보다 높을 경우 최고기록을 변경해준다.
                        highest[idx]=score
                        outfilescore = open('./doc/score.txt', "w") # score 파일을 열어서
                        for i in range(3) :
                            outfilescore.write(str(highest[i])) # 스코어 전체를 입력해주고
                            outfilescore.write('\n')
                        outfilescore.close() # 닫아준다. 오류 차단. ㅇㅋ?
                    outfilepoint = open('./doc/point.txt', 'w') # 포인트 파일 열어서
                    outfilepoint.write(str(points)) # 창을 닫는 순간까지 모았던 포인트를 기록해준다.
                    outfilepoint.close() # 그리고 닫아
                    pygame.quit() # 파이게임 나가고
                    sys.exit() # 시스템 꺼버려
            if event.type == QUIT : # Q랑 같은 친구야. 사이좋게 지내려무나.
                print("PERFECT : " + str(perfect) + " GREAT : " + str(great) + " MISS : " + str(miss))
                if score>90 :
                    points+=2
                if score>highest[idx] : # 이번 기록이 종전 최고기록보다 높을 경우 최고기록을 변경해준다.
                    highest[idx]=score
                    outfilescore=open('./doc/score.txt', "w")
                    for i in range(3) :
                        outfilescore.write(str(highest[i]))
                        outfilescore.write('\n')
                    outfilescore.close()
                outfilepoint = open('./doc/point.txt', 'w')
                outfilepoint.write(str(points))
                outfilepoint.close()
                pygame.quit()
                sys.exit()
        if (combo % 25) == 0 and kk != combo and combo != 0: # 콤보가 25의 배수인 경우, 강조를 위해 화면의 중앙에 콤보수를 띄워준당게. kk는 버그 발생 방지용인디, combo수가 전이랑 안 바뀌었으면(1 프레임 동안 콤보수에 변화 없으면, 즉 별다른 이벤트가 없었으면)
            kk = combo
            k = 9
            textSurfaceObjComboOnMiddle = fontObj3.render(str(combo) + 'Combo', True,
                                                BLACK)
            textRectObjComboOnMiddle = textSurfaceObjComboOnMiddle.get_rect();
            textRectObjComboOnMiddle.center = (85, 170)
        if Pausei == 0 :
            for i in range(3):  # While문이 1회 돌 때마다 Count[_____]Time을 1씩 감소시켜 총 3?4? 프레임 동안만 [______]_1, 나머지 3 프레임 동안 [______]_2, 나머지 프레임 동안 [_______]_3 이펙트가 나타나도록 한다.
                if CountPerfectTime[i] > 0:
                    CountPerfectTime[i] -= 1
                if CountMissTime[i] > 0:
                    CountMissTime[i] -= 1
                if CountGreatTime[i] > 0:
                    CountGreatTime[i] -= 1
                if CountNothingTime[i] > 0:
                    CountNothingTime[i] -= 1
            for i in range(3):  # 레인이 3개니까 3번 돌리는 거겠지?
                if CountPerfectTime[i] > CountMissTime[i] and CountPerfectTime[i] > CountGreatTime[i] and CountPerfectTime[i] > CountNothingTime[i]:  # 그 레인에서 CountPerfectTime이 가장 크면(perfect 이후로 다른 이벤트가 없었다면)
                    if CountPerfectTime[i] > 7:
                        screen.blit(imgPerfect_1, (10 + i * 60, 297))
                    elif CountPerfectTime[i] > 5:
                        screen.blit(imgPerfect_2, (10 + i * 60, 297))
                    elif CountPerfectTime[i] > 3:
                        screen.blit(imgPerfect_3, (10 + i * 60, 297))
                    elif CountPerfectTime[i] > 1:
                        screen.blit(imgPerfect_4, (10 + i * 60, 297))  # ㅇㅋ?
            for i in range(3):  # 같은 설명은 두 번 다 시 설 명 하 지 않 는 다
                if CountGreatTime[i] > CountMissTime[i] and CountGreatTime[i] > CountPerfectTime[i] and CountGreatTime[
                    i] > CountNothingTime[i]:
                    if CountGreatTime[i] > 7:
                        screen.blit(imgGreat_1, (10 + i * 60, 297))
                    elif CountGreatTime[i] > 5:
                        screen.blit(imgGreat_2, (10 + i * 60, 297))
                    elif CountGreatTime[i] > 3:
                        screen.blit(imgGreat_3, (10 + i * 60, 297))
                    elif CountGreatTime[i] > 1:
                        screen.blit(imgGreat_4, (10 + i * 60, 297))
            for i in range(3):  # 나 는 너 희 가 하 나 를 설 명 하 면 3 개 를 알 아 듣 는 다 고 믿 어 의 심 치 않 는 다
                if CountMissTime[i] > CountPerfectTime[i] and CountMissTime[i] > CountGreatTime[i] and CountMissTime[
                    i] > CountNothingTime[i]:
                    if CountMissTime[i] > 7:
                        screen.blit(imgMiss_1, (10 + i * 60, 297))
                    elif CountMissTime[i] > 5:
                        screen.blit(imgMiss_2, (10 + i * 60, 297))
                    elif CountMissTime[i] > 3:
                        screen.blit(imgMiss_3, (10 + i * 60, 297))
                    elif CountMissTime[i] > 1:
                        screen.blit(imgMiss_4, (10 + i * 60, 297))
            for i in range(3):  # 왜냐하면 너희는 영재니까! 눈이 빤짝빤짝하구나!
                if CountNothingTime[i] > CountPerfectTime[i] and CountNothingTime[i] > CountGreatTime[i] and \
                                CountNothingTime[i] > CountMissTime[i]:
                    if CountNothingTime[i] > 7:
                        screen.blit(imgNothing_1, (10 + i * 60, 297))
                    elif CountNothingTime[i] > 5:
                        screen.blit(imgNothing_2, (10 + i * 60, 297))
                    elif CountNothingTime[i] > 3:
                        screen.blit(imgNothing_3, (10 + i * 60, 297))
                    elif CountNothingTime[i] > 1:
                        screen.blit(imgNothing_4, (10 + i * 60, 297))
        for i in range(di[4*SongDictionary+0]['n']): # 노트 위치를 상시 출력해준다. 오버
            screen.blit(imgg[i], (x[i], y[i]))
        screen.blit(imgPause, (300,0))
        if k >= 1 :
            screen.blit(textSurfaceObjComboOnMiddle, textRectObjComboOnMiddle)
            k -= 1
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj2, textRectObj2)
        screen.blit(textSurfaceObj3, textRectObj3)
        screen.blit(textSurfaceObj4, textRectObj4) # 텍스트 다 출력 해준당. 귀찮당. 사실 복붙하고 숫자만 바꾼거당 ㅎㅎ
        if Pausei == 1 :
            screen.blit(imgPaused, (60,160))
            if event.type==MOUSEBUTTONUP and event.button==LEFT : # 마우스 왼쪽 클릭하면
                position=pygame.mouse.get_pos() # 위치 받아와서
                if position[0] in range(95,246) : #(position[0] >= 95 or position[0] <= 246) and (position[1] >= 227 or position[1] <= 254) :
                    if position[1] in range(227,254) :
                        Pausei = 0
                        print('unpaused')
                        pygame.mixer.music.unpause()
                if position[0] in range(95, 246) :#(position[0] >= 95 or position[0] <= 246) and (position[1] >= 267 or position[1] <= 295) :
                    if position[1] in range(267,295) :
                        if score > 90:
                            points += 2
                        if score > highest[idx]:  # 이번 기록이 종전 최고기록보다 높을 경우 최고기록을 변경해준다.
                            highest[idx] = score
                            outfilescore = open('./doc/score.txt', "w")
                            for i in range(3):
                                outfilescore.write(str(highest[i]))
                                outfilescore.write('\n')
                            outfilescore.close()
                        outfilepoint = open('./doc/point.txt', 'w')
                        outfilepoint.write(str(points))
                        outfilepoint.close()
                        Quiti = 1
        pygame.display.update() # 화면 업데이트는 해줘야징. 안 해주면? 나도 모름
        if Pausei == 0 :
            cnt += 1 # 프레임 1씩 증가 했을 때... 노트 내려올 타이밍을 알아야되니까...
        if Quiti == 1 :
            print("PERFECT : " + str(perfect) + " GREAT : " + str(great) + " MISS : " + str(miss))
            cnt = 0
            return Quiti
        fpsClock.tick(fps) # 사실 이거 의미 아직도 모르겠다 손!