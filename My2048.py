import pygame, sys
from pygame.locals import *
import random
from random import *
import pyautogui

BOARDSIZE = 4
TILESIZE = 105
WINDOWSIZE = 500
FPS = 30

BLACK = (0,0,0)
DARKGRAY = (135, 125, 115)
LIGHTGRAY = (160, 150, 140)
COLOR2 = (230,220,210)
COLOR4 = (230, 210, 190)
COLOR8 = (255, 178, 102)
COLOR16 = (255, 153, 51)
COLOR32 = (255, 102, 102)
COLOR64 = (255, 52, 52)
COLOR128 = (255, 255, 102)
COLOR256 = (255, 255, 76)
COLOR512 = (255, 255, 51)
COLOR1024 = (255, 255, 25)
COLOR2048 = (255, 255, 0)
COLOR4096 = (34,139,34)
WHITE = (255,255,255)

BGCOLOR = DARKGRAY
EMPTYTILECOLOR = LIGHTGRAY
TILESTOPLEFT = [(10,10), (135,10), (260,10), (385,10),
               (10,135), (135,135), (260,135), (385,135),
               (10,260), (135,260), (260,260), (385,260),
               (10,385), (135,385), (260,385), (385,385),]


FONTSIZE = 40
TEXTCOLOR = DARKGRAY

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

def main():
    global DISPLAYSURF, FONT, BOARD, nextMove

    pygame.init()
    BOARD = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE),0,32)
    DISPLAYSURF.fill((BGCOLOR))
    pygame.display.set_caption('2048')
    FONT = pygame.font.Font('freesansbold.ttf', FONTSIZE)

    drawEmptyTiles(TILESIZE, TILESIZE)
    addTile(TILESIZE, TILESIZE)
    addTile(TILESIZE, TILESIZE)

    moves = 0
    counter = 0
    nextMove = None

    while True:
        checkForQuit()
        direction = None

        #randomMove(max, moves)
        #testedMove()
        nextMove = looksAheadTwoMoves(counter, nextMove)

        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    direction = LEFT
                elif event.key in (K_RIGHT, K_d):
                    direction = RIGHT
                elif event.key in (K_UP, K_w):
                    direction = UP
                elif event.key in (K_DOWN, K_s):
                    direction = DOWN

                newBoard = slideBoard(BOARD, direction)
                BOARD = newBoard
                drawBoard(newBoard,TILESIZE,TILESIZE )
                addTile(TILESIZE,TILESIZE)
                counter += 1
                print("BOARD: " + str(BOARD))
                print(str(counter))

def drawEmptyTiles(width, height):
    for coordinates in (TILESTOPLEFT):
        pygame.draw.rect(DISPLAYSURF, EMPTYTILECOLOR, (coordinates[0], coordinates[1], width, height))

def addTile(width, height):

    x = randint(0, BOARDSIZE-1)
    y = randint(0,BOARDSIZE-1)
    open = False

    for i in range(len(BOARD)):
        for j in range(len(BOARD[0])):
            if BOARD[i][j] == 0:
                open = True

    if open:
        while BOARD[x][y] != 0:
            x = randint(0, BOARDSIZE-1)
            y = randint(0,BOARDSIZE-1)

        for coordinates in (TILESTOPLEFT):
            if coordinates == TILESTOPLEFT[x*4 + y]:
                value = randint(0, 10)
                if value > 9:
                    value = 4
                    pygame.draw.rect(DISPLAYSURF, COLOR4, (coordinates[0], coordinates[1], width, height))
                    textSurf = FONT.render(str(value),True, TEXTCOLOR)
                    textRect = textSurf.get_rect()
                    textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                    DISPLAYSURF.blit(textSurf, textRect)
                else:
                    value = 2
                    pygame.draw.rect(DISPLAYSURF, COLOR2, (coordinates[0], coordinates[1], width, height))
                    BOARD[x][y] = value
                    textSurf = FONT.render(str(value),True, TEXTCOLOR)
                    textRect = textSurf.get_rect()
                    textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                    DISPLAYSURF.blit(textSurf, textRect)

def drawBoard(board, width, height):
    for i in range(len(board)):
        for j in range(len(board[0])):
            coordinates = TILESTOPLEFT[i*4 + j]
            if board[i][j] == 2:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR2, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 4:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR4, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 8:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR8, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 16:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR16, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 32:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR32, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 64:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR64, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 128:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR128, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 256:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR256, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 512:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR512, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 1024:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR1024, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 2048:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR2048, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            elif board[i][j] == 4096:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, COLOR4096, (coordinates[0], coordinates[1], width, height))
                textSurf = FONT.render(str(value),True, TEXTCOLOR)
                textRect = textSurf.get_rect()
                textRect.center = (coordinates[0] + int(TILESIZE / 2)), (coordinates[1] + int(TILESIZE/ 2))
                DISPLAYSURF.blit(textSurf, textRect)
            else:
                value = board[i][j]
                pygame.draw.rect(DISPLAYSURF, EMPTYTILECOLOR, (coordinates[0], coordinates[1], width, height))

def slideBoard(board, direction):

    if direction == LEFT:
        board = slide(board, direction)
    if direction == RIGHT:
        board = slide(board, direction)
    if direction == UP:
        board = slide(board, direction)
    if direction == DOWN:
        board = slide(board, direction)
    BOARD = board
    return(board)

def slide(board, direction):
    if direction == LEFT:
        board = reposition(board)
        board = merge(board)
        board = reposition(board)

    if direction == RIGHT:
        board = reverse(board)
        board = reposition(board)
        board = merge(board)
        board = reposition(board)
        board = reverse(board)

    if direction == UP:
        board = transpose(board)
        board = reposition(board)
        board = merge(board)
        board = reposition(board)
        board = transpose(board)

    if direction == DOWN:
        board = transpose(board)
        board = reverse(board)
        board = reposition(board)
        board = merge(board)
        board = reposition(board)
        board = reverse(board)
        board = transpose(board)

    return board

def reverse(board):
    new = []
    for i in range(len(board)):
        new.append([])
        for j in range (len(board[0])):
            new[i].append(board[i][len(board[0])-j-1])
    return new

def transpose(board):
    new=[]
    for i in range(len(board[0])):
        new.append([])
        for j in range(len(board)):
            new[i].append(board[j][i])
    return new

def reposition(board):
    new = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        count = 0
        for j in range(4):
            if  board[i][j] != 0:
                new[i][count] = board[i][j]
                count += 1
    return new

def merge(board):
    for i in range(len(board)):
        for j in range(len(board) - 1):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] = board[i][j] * 2
                board[i][j+1] = 0
    return board

def terminate():
    print('quit')
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

def isValidMove(board, direction):
    newBoard = slideBoard(board, direction)
    if newBoard == board:
        return False
    else:
        return True

def randomMove(max, moves):
    if max <= 128:
        if isValidMove(BOARD, LEFT):
            pyautogui.press(LEFT)
            moves += 1
            if isValidMove(BOARD, DOWN):
                pyautogui.press(DOWN)
                moves += 1
        elif isValidMove(BOARD, DOWN):
            pyautogui.press(DOWN)
            moves += 1
            if isValidMove(BOARD, LEFT):
                pyautogui.press(LEFT)
                moves += 1
        else:
            pyautogui.press(RIGHT)
            moves += 1
    else:
        pyautogui.press(LEFT)
        pyautogui.press(DOWN)
        pyautogui.press(RIGHT)
        pyautogui.press(DOWN)

def testedMove():

    leftBoardScore = getScore(slideBoard(BOARD, LEFT))
    rightBoardScore = getScore(slideBoard(BOARD, RIGHT))
    downBoardScore = getScore(slideBoard(BOARD, DOWN))

    print("Left: " + str(leftBoardScore) + " Right: " + str(rightBoardScore) + " Down: " + str(downBoardScore))

    if leftBoardScore >= rightBoardScore and leftBoardScore >= downBoardScore:
        print("First")
        if isValidMove(BOARD, LEFT):
            pyautogui.press(LEFT)
        else:
            if downBoardScore >= rightBoardScore:
                if isValidMove(BOARD, DOWN):
                    pyautogui.press(DOWN)
                else:
                    pyautogui.press(RIGHT)
            else:
                if isValidMove(BOARD, RIGHT):
                    pyautogui.press(RIGHT)
                else:
                    if isValidMove(BOARD, DOWN):
                        pyautogui.press(DOWN)
                    else:
                        pyautogui.press(UP)
    elif rightBoardScore >= leftBoardScore and rightBoardScore >= downBoardScore:
        print("Second")
        if isValidMove(BOARD, RIGHT):
            pyautogui.press(RIGHT)
        else:
            if leftBoardScore >= downBoardScore:
                if isValidMove(BOARD, LEFT):
                    pyautogui.press(LEFT)
            else:
                if isValidMove(BOARD, DOWN):
                    pyautogui.press(DOWN)
                else:
                    if isValidMove(BOARD, LEFT):
                        pyautogui.press(LEFT)
                    else:
                        pyautogui.press(UP)
    elif downBoardScore >= rightBoardScore and downBoardScore >= leftBoardScore:
        print("Third")
        if isValidMove(BOARD, DOWN):
            pyautogui.press(DOWN)
        else:
            if leftBoardScore >= rightBoardScore:
                if isValidMove(BOARD, LEFT):
                    pyautogui.press(LEFT)
            else:
                if isValidMove(BOARD, RIGHT):
                    pyautogui.press(RIGHT)
                else:
                    if isValidMove(BOARD, LEFT):
                        pyautogui.press(LEFT)
                    else:
                        pyautogui.press(UP)
    else:
        pyautogui.press(UP)

def looksAheadTwoMoves(counter, nextMove):
    if counter % 2 == 0:
        print("First Move")
        leftBoard = slideBoard(BOARD, LEFT)
        rightBoard = slideBoard(BOARD, RIGHT)
        downBoard = slideBoard(BOARD, DOWN)

        LLscore = getScore(slideBoard(leftBoard, LEFT)), "LLscore"
        LRscore = getScore(slideBoard(leftBoard, RIGHT)), 'LRscore'
        LDscore = getScore(slideBoard(leftBoard, DOWN)), 'LDscore'

        RLscore = getScore(slideBoard(rightBoard, LEFT)), 'RLscore'
        RRscore = getScore(slideBoard(rightBoard, RIGHT)), 'RRscore'
        RDscore = getScore(slideBoard(rightBoard, DOWN)), 'RDscore'

        DLscore = getScore(slideBoard(downBoard, LEFT)), 'DLscore'
        DRscore = getScore(slideBoard(downBoard, RIGHT)), 'DRscore'
        DDscore = getScore(slideBoard(downBoard, DOWN)), 'DDscore'

        Scores = [LLscore, LRscore, LDscore, RLscore, RRscore, RDscore, DLscore, DRscore, DDscore]
        scoresDescending = [score[0] for score in Scores]

        for i in range(len(scoresDescending)):
            for j in range (len(scoresDescending)):
                if (scoresDescending[i] > scoresDescending[j] and i != j):
                    temp = scoresDescending[j]
                    scoresDescending[j] = scoresDescending[i]
                    scoresDescending[i] = temp

                    temp = Scores[j]
                    Scores[j] = Scores[i]
                    Scores[i] = temp

        #print(str(Scores[0]))

        for score in Scores:
            if score[1] == LLscore[1]:
                pyautogui.press(LEFT)
                nextMove = LEFT
            elif score[1] == LRscore[1]:
                pyautogui.press(LEFT)
                nextMove = RIGHT
            elif score[1] == LDscore[1]:
                pyautogui.press(LEFT)
                nextMove = DOWN
            elif score[1] == RRscore[1]:
                pyautogui.press(RIGHT)
                nextMove = RIGHT
            elif score[1] == RLscore[1]:
                pyautogui.press(RIGHT)
                nextMove = LEFT
            elif score[1] == RDscore[1]:
                pyautogui.press(RIGHT)
                nextMove = DOWN
            elif score[1] == DLscore[1]:
                pyautogui.press(DOWN)
                nextMove = LEFT
            elif score[1] == DRscore[1]:
                pyautogui.press(DOWN)
                nextMove = RIGHT
            elif score[1] == DDscore[1]:
                pyautogui.press(DOWN)
                nextMove = DOWN
            else:
                print("UP")
                pyautogui.press(UP)
            break

        return nextMove

    elif counter % 2 == 1:
        print("Second Move")
        if nextMove == LEFT:
            pyautogui.press(LEFT)
        elif nextMove == RIGHT:
            pyautogui.press(RIGHT)
        elif nextMove == UP:
            pyautogui.press(UP)
        elif nextMove == DOWN:
            pyautogui.press(DOWN)

        moveOne = True
        moveTwo = False

def getScore(board):
    return (findMax(board) + findZeros(board) + incentive(board) + incentive2(board)) # + incentive4(board))#+ incentive3(board))
    # Zeros: 2 Incentive: 50 Incentive2: -1

def findMax(board):
    max = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > max:
                max = board[i][j]
    return max

def findZeros(board):
    zeros = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                zeros += 3
    return zeros

def incentive(board):
    incentive = 0
    if findMax(board) == board[3][0] or findMax(board) == board[3][3]:
        incentive += 100
        return incentive
    else:
        return incentive

def incentive2(board):
    diagonals= 0
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == board[i+1][j+1]:
                diagonals -= 1
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i+1][j] == board[i][j+1]:
                diagonals -= 1

    return diagonals

def incentive3(board):
    ordered = 0
    for i in range(len(board)):
        for j in range(len(board)-1):
            if board[i][j+1] == (2 * board[i][j]): #Directly to Right 2*bigger
                ordered += 1
            if board[i][j+1] == (board[i][j]/2): #Directly to Right Half size
                ordered += 1
    return ordered

def incentive4(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 32:
                total += 2
            elif board[i][j] == 64:
                total += 4
            elif board[i][j] == 128:
                total += 8
            elif board[i][j] == 256:
                total += 16
            elif board[i][j] == 512:
                total += 32
            elif board[i][j] == 1024:
                total += 64
            elif board[i][j] == 2048:
                total += 128
            else:
                total += 0
    return total

if __name__ == '__main__':
    main()
