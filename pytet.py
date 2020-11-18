from matrix import *
import random

def rotate(blk):
    if blk == [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]:# |
        return [ [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]:# ㅡ
        return [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]
    ###
    elif blk == [ [ 0, 0, 1, 0 ], [ 1, 1, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ(좌우대칭)
        return [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ좌대 1번 
        return [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ좌대 2번 
        return [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ좌대 3번 
        return [ [ 0, 0, 1, 0 ], [ 1, 1, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]
    ### 
    elif blk == [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ
        return [ [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ1
        return [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ2
        return [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]:# ㄴ3
        return [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]   
    ###
    elif blk == [ [ 0, 0, 1, 0 ],
                  [ 0, 1, 1, 1 ], 
                  [ 0, 0, 0, 0 ], 
                  [ 0, 0, 0, 0 ] ]:# ㅗ
        return [ [ 0, 0, 1, 0 ], 
                 [ 0, 0, 1, 1 ], 
                 [ 0, 0, 1, 0 ],
                 [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ], 
                  [ 0, 0, 1, 1 ], 
                  [ 0, 0, 1, 0 ], 
                  [ 0, 0, 0, 0 ] ]:# ㅗ1
        return [ [ 0, 0, 0, 0 ], 
                 [ 0, 1, 1, 1 ], 
                 [ 0, 0, 1, 0 ], 
                 [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], 
                  [ 0, 1, 1, 1 ], 
                  [ 0, 0, 1, 0 ], 
                  [ 0, 0, 0, 0 ] ]:# ㅗ2
        return [ [ 0, 0, 1, 0 ], 
                 [ 0, 1, 1, 0 ], 
                 [ 0, 0, 1, 0 ], 
                 [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ], 
                  [ 0, 1, 1, 0 ], 
                  [ 0, 0, 1, 0 ],
                  [ 0, 0, 0, 0 ] ]:# ㅗ3
        return [ [ 0, 0, 1, 0 ], 
                 [ 0, 1, 1, 1 ], 
                 [ 0, 0, 0, 0 ], 
                 [ 0, 0, 0, 0 ] ]
    ###
    elif blk == [ [ 0, 1, 1, 0 ],
                  [ 0, 0, 1, 1 ],
                  [ 0, 0, 0, 0 ],
                  [ 0, 0, 0, 0 ] ]:#ㄱㄴ
        return [ [ 0, 0, 1, 0 ],
                 [ 0, 1, 1, 0 ],
                 [ 0, 1, 0, 0 ],
                 [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ],
                  [ 0, 1, 1, 0 ],
                  [ 0, 1, 0, 0 ],
                  [ 0, 0, 0, 0 ] ]:#ㄱㄴ1
        return [ [ 0, 1, 1, 0 ],
                 [ 0, 0, 1, 1 ],
                 [ 0, 0, 0, 0 ],
                 [ 0, 0, 0, 0 ] ]
    ###
    elif blk == [ [ 0, 1, 1, 0 ],
                    [ 1, 1, 0, 0 ],
                    [ 0, 0, 0, 0 ],
                    [ 0, 0, 0, 0 ] ]:# ㄱㄴ 대칭
        return [ [ 0, 1, 0, 0 ],
                 [ 0, 1, 1, 0 ],
                 [ 0, 0, 1, 0 ],
                 [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 1, 0, 0 ],
                  [ 0, 1, 1, 0 ],
                  [ 0, 0, 1, 0 ],
                  [ 0, 0, 0, 0 ] ]:# ㄱㄴ 대칭
        return [ [ 0, 1, 1, 0 ],
                 [ 1, 1, 0, 0 ],
                 [ 0, 0, 0, 0 ],
                 [ 0, 0, 0, 0 ] ]
    ###
    elif blk == [ [ 0, 1, 1, 0 ],
                  [ 0, 1, 1, 0 ], 
                  [ 0, 0, 0, 0 ], 
                  [ 0, 0, 0, 0 ] ]:# ㅁ
        return blk
    
def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("!!", end='')
        print()
arrayBlk_lst = [[ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ],# |
                [ [ 0, 0, 1, 0 ], [ 1, 1, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ],# ㄴ 반대
                [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ],# ㄴ
                [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ],# ㅗ
                [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ],#ㄱㄴ
                [ [ 0, 1, 1, 0 ], [ 1, 1, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ],# ㄱㄴ 대칭
                [ [ 0, 1, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]]# ㅁ     
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2
newBlockNeeded = False
arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
cur_blc_lst = arrayBlk_lst[random.randrange(0,7)]
currBlk = Matrix(cur_blc_lst)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

while True:
    newBlockNeeded = False
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate),\'space key\' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a':
        left -= 1
    elif key == 'd':
        left += 1
    elif key == 's':
        top += 1
    elif key == 'w':
        cur_blc_lst = rotate(cur_blc_lst)
        currBlk = Matrix(cur_blc_lst)
    elif key == ' ':
        while(True):
            top += 1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            if tempBlk.anyGreaterThan(1) == True:
                top -= 1
                newBlockNeeded = True
                break
    else:
        print('Wrong key!!!')
        continue
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a':
            left += 1
        elif key == 'd':
            left -= 1
        elif key == 's':
            top -= 1
            newBlockNeeded = True
        elif key == 'w':
            for i in range(3):
                cur_blc_lst = rotate(cur_blc_lst)
            currBlk = Matrix(cur_blc_lst)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        cur_blc_lst = arrayBlk_lst[random.randrange(0,7)]
        currBlk = Matrix(cur_blc_lst)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
