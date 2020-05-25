import time
import random
import copy
import pygame as pg
from pygame import mixer
from solver import *
from boards import giveBoard

pg.init()

# DO NOT CHANGE WIDTH AND HEIGHT (HARD CODED) {600, 800}
screenWidth = 600
screenHeight = 800

screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("~SUDOKU~")


def getColor(color):
    if color == 'green':
        return (40, 160, 30)
    if color == 'black':
        return (20, 20, 20)
    if color == 'white':
        return (240, 240, 240)
    if color == 'dimWhite':
        return (150, 150, 150)
    if color == 'red':
        return (170, 10, 10)
    if color == 'orange':
        return (190, 80, 20)
    if color == 'grey':
        return (80, 80, 80)
    if color == 'dimGrey':
        return (40, 40, 40)
    if color == 'veryDimGrey':
        return (30, 30, 30)
    else:
        return (0, 0, 0)


### TEXTS instance ####################################
#######################################################
# sudoku (white)
sudokuFont = pg.font.Font("SEASRN__.ttf", 100)
sudokuText = sudokuFont.render("SUDOKU", True, getColor('white'))
# main menu
mainMenuFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
mainMenuText = mainMenuFont.render("[main menu]", True, getColor('white'))
mainMenuInvertedFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
mainMenuInvertedText = mainMenuInvertedFont.render(
    "[main menu]", True, getColor('black'))
# play
playFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
playText = playFont.render("-: PLAY :-", True, getColor('white'))
playBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
playBigText = playBigFont.render("-: PLAY :-", True, getColor('white'))
# easy
easyFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
easyText = easyFont.render("-: EASY :-", True, getColor('white'))
easyBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
easyBigText = easyBigFont.render("-: EASY :-", True, getColor('white'))
# medium
mediumFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
mediumText = mediumFont.render("-: MEDIUM :-", True, getColor('white'))
mediumBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
mediumBigText = mediumBigFont.render("-: MEDIUM :-", True, getColor('white'))
# hard
hardFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
hardText = hardFont.render("-: HARD :-", True, getColor('white'))
hardBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
hardBigText = hardBigFont.render("-: HARD :-", True, getColor('white'))
# hard
veryHardFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
veryHardText = veryHardFont.render("-: VERY HARD :-", True, getColor('white'))
veryHardBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
veryHardBigText = veryHardBigFont.render(
    "-: VERY HARD :-", True, getColor('white'))
# SPACE to autosolve
spaceToSolveFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
spaceToSolveText = spaceToSolveFont.render(
    "Press [SPACE] to Autosolve", True, getColor('grey'))
# solver
solverFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
solverText = solverFont.render("-: SOLVER :-", True, getColor('white'))
solverBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
solverBigText = solverBigFont.render("-: SOLVER :-", True, getColor('white'))
# scoreBoard
scoreBoardFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
scoreBoardText = scoreBoardFont.render(
    "-: SCORE BOARD :-", True, getColor('white'))
scoreBoardBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
scoreBoardBigText = scoreBoardBigFont.render(
    "-: SCORE BOARD :-", True, getColor('white'))
# pop UP window text (inGamePlay)
# queryText
popUpQueryFont = pg.font.Font("RobotoSlab-Bold.ttf", 25)
popUpQueryText = popUpQueryFont.render(
    "Are you sure? You will lose your progress !", True, getColor('white'))
# Ok
okFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
okText = okFont.render("[OK]", True, getColor('white'))
okInvertedFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
okInvertedText = okInvertedFont.render("[OK]", True, getColor('black'))
# Cancel
cancelFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
cancelText = cancelFont.render("[CANCEL]", True, getColor('white'))
cancelInvertedFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
cancelInvertedText = cancelInvertedFont.render(
    "[CANCEL]", True, getColor('black'))
# pop Up window (inAutoSolve)
# autoSolveQueryText
autoSolveQueryFont = pg.font.Font("RobotoSlab-Bold.ttf", 24)
autoSolveQueryText = autoSolveQueryFont.render(
    "Are you sure? You don't want to solve on your own!", True, getColor('white'))
# autoSolveDirect
autoSolveDirectFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
autoSolveDirectText = autoSolveDirectFont.render(
    "[SOLUTION]", True, getColor('white'))
autoSolveDirectInvertedFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
autoSolveDirectInvertedText = autoSolveDirectInvertedFont.render(
    "[SOLUTION]", True, getColor('black'))
# autoSolveAnimation
autoSolveAnimationFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
autoSolveAnimationText = autoSolveAnimationFont.render(
    "[ANIMATION]", True, getColor('white'))
autoSolveAnimationInvertedFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
autoSolveAnimationInvertedText = autoSolveAnimationInvertedFont.render(
    "[ANIMATION]", True, getColor('black'))
# exit
exitFont = pg.font.Font("RobotoSlab-Bold.ttf", 50)
exitText = exitFont.render("-: EXIT :-", True, getColor('white'))
exitBigFont = pg.font.Font("RobotoSlab-Bold.ttf", 65)
exitBigText = exitBigFont.render("-: EXIT :-", True, getColor('white'))
# time
clockFont = pg.font.Font("TypeWrongSmudgedBold.ttf", 35)
# Numbers Text
# 1 (one)
oneFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
oneText = oneFont.render('1', True, getColor('white'))
oneBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
oneBigText = oneBigFont.render('1', True, getColor('grey'))
oneRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
oneRedText = oneRedFont.render('1', True, getColor('red'))
# 2 (two)
twoFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
twoText = twoFont.render('2', True, getColor('white'))
twoBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
twoBigText = twoBigFont.render('2', True, getColor('grey'))
twoRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
twoRedText = twoRedFont.render('2', True, getColor('red'))
# 3 (three)
threeFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
threeText = threeFont.render('3', True, getColor('white'))
threeBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
threeBigText = threeBigFont.render('3', True, getColor('grey'))
threeRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
threeRedText = threeRedFont.render('3', True, getColor('red'))
# 4 (four)
fourFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
fourText = fourFont.render('4', True, getColor('white'))
fourBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
fourBigText = fourBigFont.render('4', True, getColor('grey'))
fourRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
fourRedText = fourRedFont.render('4', True, getColor('red'))
# 5 (five)
fiveFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
fiveText = fiveFont.render('5', True, getColor('white'))
fiveBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
fiveBigText = fiveBigFont.render('5', True, getColor('grey'))
fiveRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
fiveRedText = fiveRedFont.render('5', True, getColor('red'))
# 6 (six)
sixFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
sixText = sixFont.render('6', True, getColor('white'))
sixBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
sixBigText = sixBigFont.render('6', True, getColor('grey'))
sixRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
sixRedText = sixRedFont.render('6', True, getColor('red'))
# 7 (seven)
sevenFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
sevenText = sevenFont.render('7', True, getColor('white'))
sevenBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
sevenBigText = sevenBigFont.render('7', True, getColor('grey'))
sevenRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
sevenRedText = sevenRedFont.render('7', True, getColor('red'))
# 8 (eight)
eightFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
eightText = eightFont.render('8', True, getColor('white'))
eightBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
eightBigText = eightBigFont.render('8', True, getColor('grey'))
eightRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
eightRedText = eightRedFont.render('8', True, getColor('red'))
# 9 (nine)
nineFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
nineText = nineFont.render('9', True, getColor('white'))
nineBigFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 45)
nineBigText = nineBigFont.render('9', True, getColor('grey'))
nineRedFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
nineRedText = nineRedFont.render('9', True, getColor('red'))
# ' '
emptyFont = pg.font.Font('TypeWrongSmudgedBold.ttf', 35)
emptyText = emptyFont.render(' ', True, getColor('black'))

### SOUND #############################################
#######################################################
# background music
mixer.music.load("backgroundMusic.ogg")
mixer.music.play(-1)
# loading different sounds
clickSound = mixer.Sound(
    "click.ogg")
moveSound = mixer.Sound("move.ogg")
congratulationSound = mixer.Sound("congratulation.ogg")
gameStartSound = mixer.Sound("gameStart.ogg")
gameOverSound = mixer.Sound("gameOver.ogg")

### initialization of switches ########################
#######################################################
# for grid in intro
gridSwitch = True
# for grid in gameplay
gameGridSwitch = True
# for moving from entry screen to [main menu]
introClick = False
# for locations
inMainMenu = False
inPlay = False
inSolver = False
inScoreBoard = False
inGamePlay = False
inPopUp = False
inSolvePopUp = False
# to reset start time
resetTime = True
# switch to start the clock in gameplay
timerOn = False
# for playing move and wrong move sound (one time)
madeMove = False
# congratulations Sound played or not
congratesPlayed = False
# to reset Boards in solver
resetSolverBoards = False

### FOR GAME PLAY ######################################
########################################################

# position of shells in sudoku board
shellPosList = [[], [], [], [], [], [], [], [], []]
i = 0
# +25 in x and +15 in y, to display the number in middle of shell
for y in range(100, 629, 66):
    for x in range(2, 531, 66):
        shellPosList[i].append((x, y))
    i += 1
# boundary of shells in sudoku board
shellBoundaryList = [[], [], [], [], [], [], [], [], []]
i = 0
# +25 in x and +15 in y, to display the number in middle of shell
for y in range(100, 629, 66):
    for x in range(2, 531, 66):
        shellBoundaryList[i].append((x, x+66, y, y+66))
    i += 1

# cordinate of selected shell
selectedShell = 0


sudokuBoard = [  # EMPTY
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

userBoard = [  # EMPTY
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

currentBoard = [  # EMPTY
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

emptyBoard = [  # EMPTY
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def cursor(text):

    x, y = pg.mouse.get_pos()

    if text == 'onMainMenuText':
        if 50 < x < 250 and 35 < y < 80:
            return True
        return False

    elif text == 'onGamePlayMainMenuText':
        if 20 < x < 220 and 15 < y < 60:
            return True
        return False

    elif text == 'onPlayText' or text == 'onEasyText':
        if 180 < x < 400 and 300 < y < 360:
            return True
        return False

    elif text == 'onSolverText' or text == 'onMediumText':
        if 150 < x < 500 and 400 < y < 460:
            return True
        return False

    elif text == 'onScoreBoardText':
        if 80 < x < 500 and 500 < y < 560:
            return True
        return False

    elif text == 'onHardText':
        if 180 < x < 400 and 500 < y < 560:
            return True
        return False

    elif text == 'onVeryHardText':
        if 100 < x < 480 and 600 < y < 660:
            return True
        return False

    elif text == 'onCancel':
        if 130 < x < 270 and 415 < y < 460:
            return True
        return False

    elif text == 'onOk':
        if 400 < x < 460 and 415 < y < 460:
            return True
        return False

    elif text == 'onAutoSolveDirect':
        if 320 < x < 490 and 385 < y < 420:
            return True
        return False

    elif text == 'onAutoSolveAnimation':
        if 310 < x < 510 and 480 < y < 520:
            return True
        return False

    elif text == 'onExitText':
        if 180 < x < 400 and 600 < y < 660:
            return True
        return False

    # Gives cordinates of current shell
    elif text == 'onGameBoard':

        global shellBoundaryList
        global sudokuBoard
        posList = copy.deepcopy(shellBoundaryList)

        posRow = 0
        pos = 0
        for rows in sudokuBoard:
            for item in rows:
                if item != 0:
                    posList[posRow][pos] = (1000, 1010, 1000, 1010)
                pos += 1
            pos = 0
            posRow += 1

        for rows in posList:
            for item in rows:
                x1, x2, y1, y2 = item
                if x1 < x < x2 and y1 < y < y2:
                    return (x1, y1)
        return False


def gridAnimation(screen, where):
    global screenHeight, screenWidth
    if where == 'main':
        screen.fill(getColor('black'))
        thickLineX, thinLineX, thickLineY, thinLineY = 0, 0, 0, 0
        thickness = 6
        thinness = 3
        for thinY in range(0, screenHeight+1, 15):
            # vertical thin line horizontal positions
            for verThinPos in range(4, screenWidth-thickness, screenWidth//9):
                pg.draw.line(screen, getColor('dimGrey'),
                             (verThinPos, 0), (verThinPos, thinY), thinness)
                pg.display.update()
        for thinX in range(0, screenWidth+1, 15):
            # horizontal thin line veritcal positions
            for horThinPos in range(100, screenHeight-100, screenWidth//9):
                pg.draw.line(screen, getColor('dimGrey'),
                             (0, horThinPos), (thinX, horThinPos), thinness)
                pg.display.update()
        for thickY in range(0, screenHeight+1, 6):
            # vertical thick line horizontal positions
            for verThickPos in range(4, screenWidth-thickness, 200 - 4):
                pg.draw.line(screen, getColor('grey'), (verThickPos, 0),
                             (verThickPos, thickY), thickness)
                pg.display.update()
        for thickX in range(0, screenWidth+1, 6):
            # horizontal thick line vertical positions
            for horThickPos in range(100, screenHeight-100, 200 - 2):
                pg.draw.line(screen, getColor('grey'),
                             (0, horThickPos), (thickX, horThickPos), thickness)
                pg.display.update()
        time.sleep(0.5)

    if where == 'gamePlay':
        # 594px dimension of board, 198px dim of box and 66px dim of shell
        screen.fill(getColor('black'))
        thickLineX, thinLineX, thickLineY, thinLineY = 0, 0, 0, 0
        thickness = 6
        thinness = 3
        for thinY in range(100, 698+1, 12):
            # vertical thin line horizontal positions
            for verThinPos in range(2, 596+1, 66):
                pg.draw.line(screen, getColor('dimGrey'),
                             (verThinPos, 100), (verThinPos, thinY), thinness)
                pg.display.update()
        for thinX in range(2, 600+1, 12):
            # horizontal thin line veritcal positions
            for horThinPos in range(100, 694+1, 66):
                pg.draw.line(screen, getColor('dimGrey'),
                             (2, horThinPos), (thinX, horThinPos), thinness)
                pg.display.update()
        for thickY in range(100, 694+1, 6):
            # vertical thick line horizontal positions
            for verThickPos in range(2, 596+1, 198):
                pg.draw.line(screen, getColor('grey'), (verThickPos, 100),
                             (verThickPos, thickY), thickness)
                pg.display.update()
        for thickX in range(2, 596+1, 6):
            # horizontal thick line vertical positions
            for horThickPos in range(100, 694+1, 198):
                pg.draw.line(screen, getColor('grey'),
                             (2, horThickPos), (thickX, horThickPos), thickness)
                pg.display.update()


def gridView(screen):
    global currentBoard
    global greyGridLines
    greyGridLines = True

    if isFull(currentBoard):
        greyGridLines = False
        for y in range(9):
            for x in range(9):
                if not possible(currentBoard, x, y, currentBoard[y][x]):
                    greyGridLines = True
                    break

    if greyGridLines:
        # 594px dimension of board, 198px dim of box and 66px dim of shell
        thickLineX, thinLineX, thickLineY, thinLineY = 0, 0, 0, 0
        thickness = 6
        thinness = 3
        # vertical thin lines
        for verThinPos in range(2, 596+1, 66):
            pg.draw.line(screen, getColor('dimGrey'),
                         (verThinPos, 100), (verThinPos, 698), thinness)
        # horizontal thin lines
        for horThinPos in range(100, 694+1, 66):
            pg.draw.line(screen, getColor('dimGrey'),
                         (2, horThinPos), (600, horThinPos), thinness)
        # vertical thick lines
        for verThickPos in range(2, 596+1, 198):
            pg.draw.line(screen, getColor('grey'), (verThickPos, 100),
                         (verThickPos, 694), thickness)
        # horizontal thick lines
        for horThickPos in range(100, 694+1, 198):
            pg.draw.line(screen, getColor('grey'),
                         (2, horThickPos), (596, horThickPos), thickness)

    if not greyGridLines:
        # 594px dimension of board, 198px dim of box and 66px dim of shell
        thickLineX, thinLineX, thickLineY, thinLineY = 0, 0, 0, 0
        thickness = 6
        thinness = 3
        # vertical thin lines
        for verThinPos in range(2, 596+1, 66):
            pg.draw.line(screen, getColor('green'),
                         (verThinPos, 100), (verThinPos, 698), thinness)
        # horizontal thin lines
        for horThinPos in range(100, 694+1, 66):
            pg.draw.line(screen, getColor('green'),
                         (2, horThinPos), (600, horThinPos), thinness)
        # vertical thick lines
        for verThickPos in range(2, 596+1, 198):
            pg.draw.line(screen, getColor('green'), (verThickPos, 100),
                         (verThickPos, 694), thickness)
        # horizontal thick lines
        for horThickPos in range(100, 694+1, 198):
            pg.draw.line(screen, getColor('green'),
                         (2, horThickPos), (596, horThickPos), thickness)


def intro(screen):

    global gridSwitch
    # sudoku RED font for Intro
    sudokuFont = pg.font.Font("SEASRN__.ttf", 100)
    sudokuText = sudokuFont.render("SUDOKU", True, getColor('red'))

    lineFont = pg.font.Font("RobotoSlab-Bold.ttf", 30)
    lineText = lineFont.render("press [ENTER]", True, getColor('green'))

    # Grid Animation in beginning
    if gridSwitch:
        gridAnimation(screen, 'main')
        gridSwitch = False

        screen.blit(sudokuText, (60, 120))
        pg.display.update()
        time.sleep(0.5)
        screen.blit(lineText, (200, 600))


def mainMenu(screen):
    global inMainMenu
    screen.fill(getColor('black'))
    screen.blit(sudokuText, (60, 120))

    if inMainMenu and not cursor('onPlayText'):
        screen.blit(playText, (180, 300))
    elif inMainMenu and cursor('onPlayText'):
        screen.blit(playBigText, (150, 280))

    if inMainMenu and not cursor('onSolverText'):
        screen.blit(solverText, (150, 400))
    elif inMainMenu and cursor('onSolverText'):
        screen.blit(solverBigText, (110, 380))

    if inMainMenu and not cursor('onScoreBoardText'):
        screen.blit(scoreBoardText, (80, 500))
    elif inMainMenu and cursor('onScoreBoardText'):
        screen.blit(scoreBoardBigText, (15, 480))

    if inMainMenu and not cursor('onExitText'):
        screen.blit(exitText, (185, 600))
    elif inMainMenu and cursor('onExitText'):
        screen.blit(exitBigText, (155, 580))


def play(screen):
    global inPlay
    screen.fill(getColor('black'))
    screen.blit(sudokuText, (60, 120))

    if inPlay and not cursor('onMainMenuText'):
        screen.blit(mainMenuText, (50, 40))
    elif inPlay and cursor('onMainMenuText'):
        pg.draw.rect(screen, getColor('white'), ((50, 45), (180, 40)))
        screen.blit(mainMenuInvertedText, (50, 40))

    if inPlay and not cursor('onEasyText'):
        screen.blit(easyText, (180, 300))
    elif inPlay and cursor('onEasyText'):
        screen.blit(easyBigText, (150, 280))

    if inPlay and not cursor('onMediumText'):
        screen.blit(mediumText, (145, 400))
    elif inPlay and cursor('onMediumText'):
        screen.blit(mediumBigText, (100, 380))

    if inPlay and not cursor('onHardText'):
        screen.blit(hardText, (180, 500))
    elif inPlay and cursor('onHardText'):
        screen.blit(hardBigText, (150, 480))

    if inPlay and not cursor('onVeryHardText'):
        screen.blit(veryHardText, (110, 600))
    elif inPlay and cursor('onVeryHardText'):
        screen.blit(veryHardBigText, (60, 580))


def scoreBoard(screen):
    global inScoreBoard
    screen.fill(getColor('black'))
    screen.blit(sudokuText, (60, 80))

    if inScoreBoard and not cursor('onMainMenuText'):
        screen.blit(mainMenuText, (50, 40))
    elif inScoreBoard and cursor('onMainMenuText'):
        pg.draw.rect(screen, getColor('white'), ((50, 45), (180, 40)))
        screen.blit(mainMenuInvertedText, (50, 40))


def displaySudokuNums(screen, sudokuBoard):
    global shellPosList

    posRow = 0
    pos = 0
    for rows in sudokuBoard:
        for item in rows:
            p, q = shellPosList[posRow][pos]
            a, b = p+25, q+15
            if item == 1:
                screen.blit(oneBigText, (a, b))
            elif item == 2:
                screen.blit(twoBigText, (a, b))
            elif item == 3:
                screen.blit(threeBigText, (a, b))
            elif item == 4:
                screen.blit(fourBigText, (a, b))
            elif item == 5:
                screen.blit(fiveBigText, (a, b))
            elif item == 6:
                screen.blit(sixBigText, (a, b))
            elif item == 7:
                screen.blit(sevenBigText, (a, b))
            elif item == 8:
                screen.blit(eightBigText, (a, b))
            elif item == 9:
                screen.blit(nineBigText, (a, b))
            pos += 1
        pos = 0
        posRow += 1


def displayUserNums(screen, userBoard):
    global shellPosList
    global madeMove

    posRow = 0
    pos = 0
    for rows in userBoard:
        for item in rows:
            x = rows.index(item)
            y = userBoard.index(rows)
            if possible(currentBoard, x, y, item):
                p, q = shellPosList[posRow][pos]
                a, b = p+25, q+15
                if item == 1:
                    screen.blit(oneText, (a, b))
                elif item == 2:
                    screen.blit(twoText, (a, b))
                elif item == 3:
                    screen.blit(threeText, (a, b))
                elif item == 4:
                    screen.blit(fourText, (a, b))
                elif item == 5:
                    screen.blit(fiveText, (a, b))
                elif item == 6:
                    screen.blit(sixText, (a, b))
                elif item == 7:
                    screen.blit(sevenText, (a, b))
                elif item == 8:
                    screen.blit(eightText, (a, b))
                elif item == 9:
                    screen.blit(nineText, (a, b))
            if not possible(currentBoard, x, y, item):
                p, q = shellPosList[posRow][pos]
                a, b = p+25, q+15
                if item == 1:
                    screen.blit(oneRedText, (a, b))
                elif item == 2:
                    screen.blit(twoRedText, (a, b))
                elif item == 3:
                    screen.blit(threeRedText, (a, b))
                elif item == 4:
                    screen.blit(fourRedText, (a, b))
                elif item == 5:
                    screen.blit(fiveRedText, (a, b))
                elif item == 6:
                    screen.blit(sixRedText, (a, b))
                elif item == 7:
                    screen.blit(sevenRedText, (a, b))
                elif item == 8:
                    screen.blit(eightRedText, (a, b))
                elif item == 9:
                    screen.blit(nineRedText, (a, b))

            pos += 1
        pos = 0
        posRow += 1


def directlyAutoSolvedBoard(sudokuBoard, userBoard, currentBoard):
    global inSolvePopUp, inSolver

    if inSolver:
        currentBoard = copy.deepcopy(userBoard)

    else:
        currentBoard = copy.deepcopy(sudokuBoard)

    autosolve(currentBoard)

    for y in range(9):
        for x in range(9):
            if currentBoard[y][x] != sudokuBoard[y][x]:
                userBoard[y][x] = currentBoard[y][x]


def animationAutoSolveBoard(screen, sudokuBoard, userBoard, currentBoard):
    global inGamePlay, inSolver

    findSwitch = True
    emptyList = []

    if inGamePlay:
        currentBoard = copy.deepcopy(sudokuBoard)
    if inSolver:
        currentBoard = copy.deepcopy(userBoard)

    while not isFull(currentBoard):

        if findSwitch:
            emptyList.append(findEmpty(currentBoard))
        (y, x) = emptyList[-1]
        prevNum = currentBoard[y][x]
        num = prevNum + 1
        if num == 10:
            currentBoard[y][x] = 0
            emptyList.pop(-1)
            findSwitch = False
        while num < 10:
            if possible(currentBoard, x, y, num):
                currentBoard[y][x] = num
                findSwitch = True
                break
            if num == 9:
                currentBoard[y][x] = 0
                emptyList.pop(-1)
                findSwitch = False
            num += 1

        for j in range(9):
            for i in range(9):
                if currentBoard[j][i] != sudokuBoard[j][i]:
                    userBoard[j][i] = currentBoard[j][i]

        time.sleep(0.01)
        gamePlay(screen)
        pg.display.update()


def highLight(screen, where, sudokuBoard):

    # highlight shell GREY when cursor on shell
    if where == 'inGameHover':

        if cursor('onGameBoard'):
            (a, b) = cursor('onGameBoard')
            pg.draw.rect(screen, getColor('veryDimGrey'),
                         ((a+6, b+6), (56, 56)))

    # higlight shell WHITE when clicked
    elif where == 'inGameClicked':

        if selectedShell != 0:
            (a, b) = selectedShell
            pg.draw.rect(screen, getColor('grey'), ((a+6, b+6), (56, 56)))


def updateBoard(sudokuBoard, userBoard):
    global currentBoard
    currentBoard = copy.deepcopy(sudokuBoard)

    rowPos = 0
    pos = 0
    for rows in userBoard:
        for item in rows:
            if item != 0:
                currentBoard[rowPos][pos] = item
            pos += 1
        pos = 0
        rowPos += 1


def insertNum(num):
    global screen, userBoard, selectedShell, shellPosList

    posRow = 0
    pos = 0
    for rows in shellPosList:
        for item in rows:
            if item == selectedShell:
                userBoard[posRow][pos] = num
            pos += 1
        pos = 0
        posRow += 1


def solver(screen):
    global inSolver
    global gameGridSwitch
    global sudokuBoard
    global resetSolverBoards
    global userBoard, sudokuBoard, currentBoard
    screen.fill(getColor('black'))

    # Grid animation inSolver
    if gameGridSwitch:
        gridAnimation(screen, 'gamePlay')
        gameGridSwitch = False

    gridView(screen)

    if not resetSolverBoards:
        # board reset for personal sudoku
        sudokuBoard = copy.deepcopy(emptyBoard)
        userBoard = copy.deepcopy(emptyBoard)
        currentBoard = copy.deepcopy(emptyBoard)

        resetSolverBoards = True

    # solver working part
    updateBoard(sudokuBoard, userBoard)
    highLight(screen, 'inGameHover', sudokuBoard)
    highLight(screen, 'inGameClicked', sudokuBoard)
    displayUserNums(screen, userBoard)

    # go to main menu
    if inSolver and not cursor('onGamePlayMainMenuText'):
        screen.blit(mainMenuText, (20, 20))
    elif inSolver and cursor('onGamePlayMainMenuText'):
        pg.draw.rect(screen, getColor('white'), ((20, 25), (180, 40)))
        screen.blit(mainMenuInvertedText, (20, 20))

    # press [space] to autosolve
    screen.blit(spaceToSolveText, (110, 725))


def gamePlay(screen):
    global inGamePlay
    global gameGridSwitch
    screen.fill(getColor('black'))

    # Grid animation inGamePlay
    if gameGridSwitch:
        gridAnimation(screen, 'gamePlay')
        gameGridSwitch = False

    gridView(screen)

    updateBoard(sudokuBoard, userBoard)
    highLight(screen, 'inGameHover', sudokuBoard)
    highLight(screen, 'inGameClicked', sudokuBoard)
    displaySudokuNums(screen, sudokuBoard)
    displayUserNums(screen, userBoard)

    # go to main menu
    if inGamePlay and not cursor('onGamePlayMainMenuText'):
        screen.blit(mainMenuText, (20, 20))
    elif inGamePlay and cursor('onGamePlayMainMenuText'):
        pg.draw.rect(screen, getColor('white'), ((20, 25), (180, 40)))
        screen.blit(mainMenuInvertedText, (20, 20))

    # press [space] to autosolve
    screen.blit(spaceToSolveText, (110, 725))


def surePopUp(screen):
    global inPopUp

    # pop up window
    if inPopUp:
        pg.draw.rect(screen, (0, 0, 0), ((0, 300), (600, 200)))
        screen.blit(popUpQueryText, (50, 340))

        if not cursor('onCancel'):
            screen.blit(cancelText, (130, 420))
        elif cursor('onCancel'):
            pg.draw.rect(screen, getColor('white'), ((130, 420), (140, 45)))
            screen.blit(cancelInvertedText, (130, 420))

        if not cursor('onOk'):
            screen.blit(okText, (400, 420))
        elif cursor('onOk'):
            pg.draw.rect(screen, getColor('white'), ((400, 420), (60, 45)))
            screen.blit(okInvertedText, (400, 420))


def autoSolvePopUp(screen):
    global inSolvePopUp

    if inSolvePopUp:
        pg.draw.rect(screen, (0, 0, 0), ((0, 300), (600, 250)))
        screen.blit(autoSolveQueryText, (10, 320))

        if not cursor('onCancel'):
            screen.blit(cancelText, (130, 420))
        elif cursor('onCancel'):
            pg.draw.rect(screen, getColor('white'), ((130, 420), (140, 45)))
            screen.blit(cancelInvertedText, (130, 420))

        if not cursor('onAutoSolveDirect'):
            screen.blit(autoSolveDirectText, (320, 380))
        elif cursor('onAutoSolveDirect'):
            pg.draw.rect(screen, getColor('white'), ((320, 385), (170, 35)))
            screen.blit(autoSolveDirectInvertedText, (320, 380))

        if not cursor('onAutoSolveAnimation'):
            screen.blit(autoSolveAnimationText, (310, 470))
        elif cursor('onAutoSolveAnimation'):
            pg.draw.rect(screen, getColor('white'), ((310, 480), (200, 40)))
            screen.blit(autoSolveAnimationInvertedText, (310, 475))


def clockTime(screen):
    global resetTime, startTime
    global greyGridLines
    global timeSnap

    pauseTimeList = [1]

    if resetTime:
        secSpend, minSpend, totalTime = 0, 0, 0
        startTime = time.time()
        resetTime = False

    if greyGridLines:
        timeSnap = int(time.time() - startTime)

    totalTime = timeSnap
    minList = [x for x in range(0, 61)]
    minList = minList[::-1]
    for num in minList:
        if totalTime >= 60*num:
            secSpend = totalTime - 60*num
            minSpend = num
            break

    clockText = clockFont.render(
        f"{minSpend}:{secSpend}", True, getColor('white'))

    screen.blit(clockText, (450, 30))


# in Solver, checking if its possible to solve or not
def checkBoardSolver():
    global currentBoard

    for y in range(9):
        for x in range(9):
            if currentBoard[y][x] != 0:
                if not possible(currentBoard, x, y, currentBoard[y][x]):
                    return False

    return True


startTime = time.time()

while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN:
            if (inGamePlay or inSolver) and selectedShell != 0:
                if event.key == pg.K_1:
                    moveSound.play()
                    insertNum(1)
                    madeMove = True
                elif event.key == pg.K_2:
                    moveSound.play()
                    insertNum(2)
                    madeMove = True
                elif event.key == pg.K_3:
                    moveSound.play()
                    insertNum(3)
                    madeMove = True
                elif event.key == pg.K_4:
                    moveSound.play()
                    insertNum(4)
                    madeMove = True
                elif event.key == pg.K_5:
                    moveSound.play()
                    insertNum(5)
                    madeMove = True
                elif event.key == pg.K_6:
                    moveSound.play()
                    insertNum(6)
                    madeMove = True
                elif event.key == pg.K_7:
                    moveSound.play()
                    insertNum(7)
                    madeMove = True
                elif event.key == pg.K_8:
                    moveSound.play()
                    insertNum(8)
                    madeMove = True
                elif event.key == pg.K_9:
                    moveSound.play()
                    insertNum(9)
                    madeMove = True
                elif event.key == pg.K_0:
                    insertNum(0)

        if event.type == pg.KEYUP:
            # inIntro
            if not introClick:
                if event.key == pg.K_RETURN:
                    clickSound.play()
                    introClick = True
                    inMainMenu = True
            if event.key == pg.K_SPACE:
                # inGamePlay
                if inGamePlay:
                    clickSound.play()
                    inSolvePopUp = True
                # inSolver
                if inSolver:
                    clickSound.play()
                    if checkBoardSolver():
                        inSolvePopUp = True

        if event.type == pg.MOUSEBUTTONDOWN:
            # inMainMenu
            if inMainMenu and cursor('onSolverText'):
                clickSound.play()
                inSolver = True
                inMainMenu = False
            if inMainMenu and cursor('onExitText'):
                pg.quit()
            # inPlayScreen
            if inPlay and cursor('onEasyText'):
                sudokuBoard = giveBoard('easy')
                clickSound.play()
                mixer.music.pause()
                gameStartSound.play()
                inGamePlay = True
                inPlay = False
                timerOn = True
            if inPlay and cursor('onMediumText'):
                sudokuBoard = giveBoard('medium')
                clickSound.play()
                mixer.music.pause()
                gameStartSound.play()
                inGamePlay = True
                inPlay = False
                timerOn = True
            if inPlay and cursor('onHardText'):
                sudokuBoard = giveBoard('hard')
                clickSound.play()
                mixer.music.pause()
                gameStartSound.play()
                inGamePlay = True
                inPlay = False
                timerOn = True
            if inPlay and cursor('onVeryHardText'):
                sudokuBoard = giveBoard('veryHard')
                clickSound.play()
                mixer.music.pause()
                gameStartSound.play()
                inGamePlay = True
                inPlay = False
                timerOn = True
            # in gamePlay
            if inGamePlay or inSolver:
                if cursor('onGameBoard'):
                    selectedShell = cursor('onGameBoard')
                elif not cursor('onGameBoard'):
                    selectedShell = 0
            # inPopUp
            if inPopUp and cursor('onCancel'):
                clickSound.play()
                inPopUp = False
            if inPopUp and cursor('onOk'):
                clickSound.play()
                inPopUp = False
                inGamePlay = False
                inMainMenu = True
                gameGridSwitch = True
                timerOn = False
                resetTime = True
                mixer.music.play(-1)
            # inSolvePopUp
            if inSolvePopUp and cursor('onCancel'):
                clickSound.play()
                inSolvePopUp = False
            if inSolvePopUp and cursor('onAutoSolveDirect'):
                clickSound.play()
                directlyAutoSolvedBoard(sudokuBoard, userBoard, currentBoard)
                inSolvePopUp = False
            if inSolvePopUp and cursor('onAutoSolveAnimation'):
                clickSound.play()
                inSolvePopUp = False
                animationAutoSolveBoard(
                    screen, sudokuBoard, userBoard, currentBoard)

        if event.type == pg.MOUSEBUTTONUP:
            # inMainMenu
            if inMainMenu and cursor('onPlayText'):
                clickSound.play()
                inPlay = True
                inMainMenu = False
            if inMainMenu and cursor('onScoreBoardText'):
                clickSound.play()
                inScoreBoard = True
                inMainMenu = False
            # inPlayScreen
            if inPlay and cursor('onMainMenuText'):
                clickSound.play()
                inPlay = False
                inMainMenu = True
            # inScoreBoardScreen
            if inScoreBoard and cursor('onMainMenuText'):
                clickSound.play()
                inScoreBoard = False
                inMainMenu = True
            # inGamePlayScreen
            if inGamePlay and cursor('onGamePlayMainMenuText'):
                clickSound.play()
                inPopUp = True
            # inSolverScreen
            if inSolver and cursor('onGamePlayMainMenuText'):
                clickSound.play()
                gameGridSwitch = True
                inSolver = False
                inMainMenu = True

    # GAME LOGIC
    if not introClick:
        intro(screen)
    if introClick and inMainMenu:
        mainMenu(screen)
        resetSolverBoards = False
    if inPlay:
        currentBoard = copy.deepcopy(emptyBoard)
        userBoard = copy.deepcopy(emptyBoard)
        congratesPlayed = False
        play(screen)
    if inScoreBoard:
        scoreBoard(screen)
    if inGamePlay:
        gamePlay(screen)
        if timerOn:
            clockTime(screen)
        if isFull(currentBoard) and not congratesPlayed:
            congratulationSound.play()
            congratesPlayed = True
    if inSolver:
        solver(screen)
    if inPopUp:
        surePopUp(screen)
    if inSolvePopUp:
        autoSolvePopUp(screen)

    pg.display.update()
