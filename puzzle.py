import math


board = [[0]*9 for i in range(9)]

for i in range(9):
    for j in range(9):
        if (i%2 == 1 and j%2 == 1):
            board[i][j] = 1 # 一是牆

vis = [[False]*9 for i in range(9)]
for i in range(9):
    for j in range(9):
        if (i%2 == 1 and j%2 == 1):
            vis[i][j] = 1
used = [False for i in range(10)]
puzzle = ['' for i in range(10)] 
puzzle[1] = [[6,8,81], [8,2,23], [2,4,45], [4,6,67]] #旋轉 第三維為各點位置
puzzle[2] = [[6,4,5]]#, [2,4,3], [8,2,1], [8,6,7]]
puzzle[3] = [[6,4,45], [8,6,67], [2,8,81], [4,2,23]]
puzzle[4] = [[8,2,4], [2,4,6], [4,6,8], [6,8,2]]
puzzle[5] = [[6,3,34], [8,5,56], [8,3,32], [2,5,54]]
puzzle[6] = [[2,1,18], [4,3,32], [6,5,54], [8,7,76]]#有限制
puzzle[7] = [[8,4,44], [2,6,66]]
puzzle[8] = [[2,1,18], [4,3,32], [6,5,54], [8,7,76]]
puzzle[9] = [[4,3,34], [6,5,56], [8,7,78], [2,1,12]]


def up_down(n):
    if (n == 6 or n == 8):
        return 14 - n
    if (n == 4 or n == 2 or n == 1 or n == 5):
        return 6 - n
    if (n > 10):
        return 10*up_down(math.floor(n/10)) + up_down(n%10)
    return n
    
def left_right(n):
    if (n == 8 or n == 2 or n == 6 or n == 4):
        return 10 - n
    if (n == 3 or n == 7):
        return 10 - n
    if (n > 10):
        return 10*left_right(math.floor(n/10)) + left_right(n%10)
    return n

for i in range(10):
    if (i == 1 or i == 3 or i == 6 or i == 8 or i == 9):
        for p in range(2):
            a = puzzle[i][p][0]
            b = puzzle[i][p][1]
            c = puzzle[i][p][2]
            puzzle[i].append([up_down(a), up_down(b), up_down(c)])
            puzzle[i].append([left_right(a), left_right(b), left_right(c)])

way = [[0, 0], [0, -2], [1, -1], [2, 0], [1, 1],
     #   無       上      右上      右     右下
        [0, 2], [-1, 1], [-2, 0], [-1, -1]]
     #    下      左下      左        左上
#//////////////////////////////////////////////////////////////////////////////////
count = 0
def dfs(layer, a):
    global count
    # if (count == 10):
    #     return
    if (layer == 10):
        count += 1
        if (a == '1'):
            print('count : ' , count)
            for i in range(9):
                for j in range(9):
                    if (board[i][j] == 1):
                        print('O', end=' ')
                    elif (vis[i][j] != False):
                        print(vis[i][j], end=' ')
                    else:
                        print(' ', end=' ')
                print('')
            print('')
        return
    if (used[layer] == True):
        dfs(layer + 1, a)
    for j in range(9):
        for i in range(9):
            if(vis[j][i] != False):
                continue
            for p in range(len(puzzle[layer])):
                is_possible = True
                for q in range(3):
                    direct = puzzle[layer][p][q]
                    temp = 99
                    bufferX = 0
                    bufferY = 0
                    while (temp != 0):
                        prebufferX = 0 #從哪一格開始走
                        prebufferY = 0
                        if (temp != 99):#代表曾經變過(有二位數)
                            prebufferX = bufferX
                            prebufferY = bufferY
                            direct = temp #方向為之前儲存的temp
                            temp = 0
                            bufferX = bufferX + way[direct][0]
                            bufferY = bufferY + way[direct][1]
                        else:
                            temp = 0#是否有移動的第二步
                            if (direct > 10):
                                temp = direct%10#有的話temp不為0,99
                                direct = math.floor(direct/10)
                            prebufferX = i
                            prebufferY = j
                            bufferX = i + way[direct][0]
                            bufferY = j + way[direct][1]  
                        # print(j, i, bufferY, bufferX,'direct : ' ,direct)
                        if (bufferX > 8 or bufferX <0 or bufferY > 8 or bufferY < 0):
                            is_possible = False
                            break
                        if (vis[bufferY][bufferX] != False):
                            is_possible = False
                            break
                        if (direct == 1 or direct == 5):
                            bufferX = prebufferX + way[direct][0]
                            bufferY = prebufferY + int(way[direct][1]/2)
                            if (layer == 6):
                                if (board[bufferY][bufferX] == 0):#6的中間必須是牆
                                    is_possible = False
                                    break
                            else:
                                if (board[bufferY][bufferX] == 1):#上下遇到牆
                                    is_possible = False
                                    break
                        if (direct == 3 or direct == 7):
                            bufferX = prebufferX + int(way[direct][0]/2)
                            bufferY = prebufferY + way[direct][1]
                            if (layer == 6):
                                if (board[bufferY][bufferX] == 0):#6的中間必須是牆
                                    is_possible = False
                                    break
                            else:
                                if (board[bufferY][bufferX] == 1):#左右遇到牆
                                    is_possible = False
                                    break
                        bufferX = i + way[direct][0]
                        bufferY = j + way[direct][1] 
                    if (is_possible == False):
                        break

                if (is_possible == True):
                    vis[j][i] = layer#將四個點設為vis = layer 分辨數字
                    vis[j + way[puzzle[layer][p][0]][1]][i + way[puzzle[layer][p][0]][0]] = layer
                    vis[j + way[puzzle[layer][p][1]][1]][i + way[puzzle[layer][p][1]][0]] = layer
                    direct = puzzle[layer][p][2]
                    if (direct > 10):
                        temp = direct%10
                        direct = math.floor(direct/10)
                        vis[j + way[direct][1] + way[temp][1]][i + way[direct][0] + way[temp][0]] = layer
                    else:
                        vis[j + way[puzzle[layer][p][2]][1]][i + way[puzzle[layer][p][2]][0]] = layer

                    dfs(layer+1, a)
                    #將四個點vis = False
                    vis[j][i] = False
                    vis[j + way[puzzle[layer][p][0]][1]][i + way[puzzle[layer][p][0]][0]] = False
                    vis[j + way[puzzle[layer][p][1]][1]][i + way[puzzle[layer][p][1]][0]] = False
                    direct = puzzle[layer][p][2]
                    if (direct > 10):
                        temp = direct%10#有的話temp不為0,99
                        direct = math.floor(direct/10)
                        vis[j + way[direct][1] + way[temp][1]][i + way[direct][0] + way[temp][0]] = False
                    else:
                        vis[j + way[puzzle[layer][p][2]][1]][i + way[puzzle[layer][p][2]][0]] = False


# is_using = 5
# used[is_using] = True
# vis[2][5] = is_using
# vis[3][4] = is_using
# vis[5][4] = is_using
# vis[6][5] = is_using

# is_using = 1
# used[is_using] = True
# vis[7][6] = is_using
# vis[8][3] = is_using
# vis[8][5] = is_using
# vis[8][7] = is_using

print('請輸入固定數量 : ',end = '')
n = int(input())

for i in range(n):
    print('請輸入固定編號 : ',end = '')
    is_using = int(input())
    used[is_using] = True
    for j in range(4):
        print('請輸入固定位置 : ',end = '')
        c, d = input().split()
        vis[int(c)][int(d)] = is_using

print('是否顯示答案(輸入1會顯示) : ')
a = input()
dfs(1, a)
print('共', count, '種可能', end = '')
a = input()

