from matrix import *
from random import *
from enum import Enum


class TetrisState(Enum):
    Running = 0
    NewBlock = 1
    Finished = 2


class Tetris():
    nBlockTypes = 0
    nBlockDegrees = 0
    setOfBlockObjects = 0
    iScreenDw = 0   # larget enough to cover the largest block

    @classmethod
    def init(cls, setOfBlockArrays):
        Tetris.nBlockTypes = len(setOfBlockArrays)
        Tetris.nBlockDegrees = len(setOfBlockArrays[0])
        Tetris.setOfBlockObjects = [[0] * Tetris.nBlockDegrees for _ in range(Tetris.nBlockTypes)]
        arrayBlk_maxSize = 0
        for i in range(Tetris.nBlockTypes):
            if arrayBlk_maxSize <= len(setOfBlockArrays[i][0]):
                arrayBlk_maxSize = len(setOfBlockArrays[i][0])
        Tetris.iScreenDw = arrayBlk_maxSize     # larget enough to cover the largest block

        for i in range(Tetris.nBlockTypes):
            for j in range(Tetris.nBlockDegrees):
                Tetris.setOfBlockObjects[i][j] = Matrix(setOfBlockArrays[i][j])
        return
		
    def createArrayScreen(self):
        self.arrayScreenDx = Tetris.iScreenDw * 2 + self.iScreenDx
        self.arrayScreenDy = self.iScreenDy + Tetris.iScreenDw
        self.arrayScreen = [[0] * self.arrayScreenDx for _ in range(self.arrayScreenDy)]
        for y in range(self.iScreenDy):
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][x] = 1
            for x in range(self.iScreenDx):
                self.arrayScreen[y][Tetris.iScreenDw + x] = 0
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][Tetris.iScreenDw + self.iScreenDx + x] = 1

        for y in range(Tetris.iScreenDw):
            for x in range(self.arrayScreenDx):
                self.arrayScreen[self.iScreenDy + y][x] = 1

        return self.arrayScreen
		
    def __init__(self, iScreenDy, iScreenDx):
        self.state = TetrisState.NewBlock
        self.iScreenDy = iScreenDy
        self.iScreenDx = iScreenDx
        self.idxBlockDegree = 0
        arrayScreen = self.createArrayScreen()
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.justStarted = True
        self.top = 0
        self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
        return

    def printScreen(self):
        array = self.oScreen.get_array()

        for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
            for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
                if array[y][x] == 0:
                    print("□", end='')

                elif array[y][x] == 1:
                    print("■", end='')

                else:
                    print("XX", end='')

            print()

    def deleteFullLines(self): #deleteFullLines 함수 완성 (accept 함수에서 호출하는 함수로, 바닥면에 블록 고정시 지워야 할 라인들을 파악해서 지워주는 기능을 완성함)
        oScreen_right_index = self.oScreen.get_dx()-Tetris.iScreenDw
        oScreen_left_index = Tetris.iScreenDw
        oScreen_hight =self.oScreen.get_dy()-Tetris.iScreenDw
        Screen_array = self.oScreen.get_array()
        count = 0
        y_index_list = []
        for y in range(oScreen_hight):
            count = 0
            for x in (oScreen_left_index,oScreen_right_index):
                if(Screen_array[y][x] == 1):
                    count += 1
            if (count >= self.iScreenDx):
                y_index_list.append(y)
                #remove fill line
            for y in y_index_list:
                for x in range(oScreen_left_index,oScreen_right_index):
                    Screen_array[y][x] = 0
                #fill space room
            for y in range(oScreen_hight, 0, -1):
                for x in range(oScreen_left_index,oScreen_right_index):
                    if (Screen_array[y][x] == 1):
                        Screen_array[y+1][x] = 1
                        Screen_array[y][x] = 0
        print()

    def accept(self, key):
        if (self.state == TetrisState.NewBlock): # 0 = 실행중, 1 = 새로운 블럭, 2 = 종료
            self.state = TetrisState.Running #더이상 새로운 블럭이 필요하지 않으므로 변경
            self.iScreen = Matrix(self.oScreen)
            self.idxBlockType = int(key) #main에서 새로운 블럭이 필요할 때 키를 문자열로 줌
            #__init__coordinate
            self.top = 0 
            self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
            #tempBlk 생성과정
            self.currBlk = Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
            self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
            self.tempBlk = self.tempBlk + self.currBlk
        # 일단 충돌 상관없이 현재 블록을 옮겨본다
        if key == 'a':
            self.left -= 1
        elif key == 'd':
            self.left += 1
        elif key == 's':
            self.top += 1
        elif key == 'w':
            print(self.idxBlockDegree)
            if self.idxBlockDegree >2:
                self.idxBlockDegree = 0
            else:
                self.idxBlockDegree +=1
            self.currBlk = Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
        elif key == ' ': 
            while True:
                if (self.tempBlk.anyGreaterThan(1)):
                    self.top -=1
                    self.state = TetrisState.NewBlock
                    self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy() , self.left+self.currBlk.get_dx())
                    self.tempBlk = self.tempBlk + self.currBlk
                    break
                self.top +=1
                self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy() , self.left+self.currBlk.get_dx())
                self.tempBlk = self.tempBlk + self.currBlk
        else: #예외 입력 처리
            print('The command does not exist.')
        # 변경된 블록 tempBlk에 적용
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk 
        if self.tempBlk.anyGreaterThan(1):
            if key == 'a': 
                self.left += 1
            elif key == 'd': 
                self.left -= 1
            elif key == 's':
                self.top -= 1
                self.state = TetrisState.NewBlock
            elif key == 'w':
                self.idxBlockDegree -=1
                self.currBlk = Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
            # Key ' '인 경우는 위에서 한번에 처리하였음.
            #되돌리기한 값 적용하기
            self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
            self.tempBlk = self.tempBlk + self.currBlk
        # 최종적으로 위 과정을 거친 tempBlk 화면에 적용
        self.oScreen = Matrix(self.iScreen)
        self.oScreen.paste(self.tempBlk, self.top, self.left)   
        Tetris.deleteFullLines(self) #마지막으로 함수를 호출하고 종료
        return self.state
