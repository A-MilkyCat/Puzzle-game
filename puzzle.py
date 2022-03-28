import math


board = [[1]*9 for i in range(9)]

for i in range(9):
    for j in range(9):
        if ((i+j)%2 == 0):
            if (i == 0 or i == 8 or j == 0 or j == 8):
                continue
            board[i][j] = 0

vis = [[False]*9 for i in range(9)]
for i in range(9):
    for j in range(9):
        if ((i+j)%2 == 0):
            if (i == 0 or i == 8 or j == 0 or j == 8):
                continue
            vis[i][j] = 1

puzzle = ['' for i in range(10)] 
puzzle[1] = [[6,8,81], [8,2,23], [2,5,45], [4,6,67]] #旋轉 第三維為各點位置
puzzle[2] = [[6,4,5], [2,4,3], [8,2,1], [8,6,7]]
puzzle[3] = [[6,4,45], [8,6,67], [2,8,81], [4,2,23]]
puzzle[4] = [[8,2,4], [2,4,6], [4,6,8], [6,8,2]]
puzzle[5] = [[6,3,34], [8,5,56], [8,3,32], [2,5,54]]
puzzle[6] = [[2,1,18], [4,3,32], [6,5,54], [8,7,76]]#有限制
puzzle[7] = [[8,4,44], [2,6,66]]
puzzle[8] = [[2,1,18], [4,3,32], [6,5,54], [8,7,76]]
puzzle[9] = [[4,3,34], [6,5,56], [8,7,78], [2,1,12]]

way = [[0, 0], [0, -2], [1, -1], [2, 0], [1, 1],
     #   無       上      右上      右     右下
        [0, 2], [-1, 1], [-2, 0], [-1, -1]]
     #    下      左下      左        左上
#//////////////////////////////////////////////////////////////////////////////////
count = 0
def dfs(layer):
    global count
    
    # if (layer >= 5):
    print('layer : ' ,layer)
    for i in range(9):
        for j in range(9):
            if (vis[i][j] == False):
                print('0', end = '')
            else:
                print(vis[i][j], end='')
        print('')
    count += 1
    return
    for j in range(9):
        for i in range(9):
            if(vis[j][i] != False):
                continue
            # print(i, j)
            for p in range(len(puzzle[layer])):
                is_possible = True
                for q in range(3):
                    direct = puzzle[layer][p][q]
                    # print(direct)
                    temp = 99
                    bufferX = 0
                    bufferY = 0
                    if (temp != 0):
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
                                # print(direct)
                                temp = direct%10#有的話temp不為0,99
                                direct = math.floor(direct/10)
                            prebufferX = i
                            prebufferY = j
                            bufferX = i + way[direct][0]
                            bufferY = j + way[direct][1]  
                        # print(j, i, bufferX, bufferY,'direct : ' ,direct, ' temp : ', temp)
                        if (bufferX > 8 or bufferX <0 or bufferY > 8 or bufferY < 0):
                            # print('HI1')
                            is_possible = False
                            break
                        if (vis[bufferY][bufferX] != False):
                            is_possible = False
                            break
                        if (direct == 1 or direct == 5):
                            bufferX = prebufferX + way[direct][0]
                            bufferY = prebufferY + int(way[direct][1]/2)
                            # print(bufferX, bufferY)
                            if (layer == 6):
                                if (board[bufferY][bufferX] == 1):#6的中間必須是牆
                                    is_possible = False
                                    # print('HI')
                                    break
                            else:
                                if (board[bufferY][bufferX] == 0):#上下遇到牆
                                    is_possible = False
                                    # print('HI2')
                                    break
                        if (direct == 3 or direct == 7):
                            bufferX = prebufferX + int(way[direct][0]/2)
                            bufferY = prebufferY + way[direct][1]
                            if (layer == 6):
                                if (board[bufferY][bufferX] == 1):#6的中間必須是牆
                                    # print('HI')
                                    is_possible = False
                                    break
                            else:
                                if (board[bufferY][bufferX] == 0):#左右遇到牆
                                    # print('HI3')
                                    is_possible = False
                                    break
                        bufferX = i + way[direct][0]
                        bufferY = j + way[direct][1] 
                        
                    if (is_possible == False):
                        break

                if (is_possible == True):
                    # print('HI')
                    vis[j][i] = layer#將四個點設為vis = layer 分辨數字
                    vis[j + way[puzzle[layer][p][0]][0]][i + way[puzzle[layer][p][0]][1]] = layer
                    vis[j + way[puzzle[layer][p][1]][0]][i + way[puzzle[layer][p][1]][1]] = layer
                    direct = puzzle[layer][p][2]
                    if (direct > 10):
                        temp = direct%10#有的話temp不為0,99
                        direct = math.floor(direct/10)
                        vis[j + way[direct][0] + way[temp][0]][i + way[direct][1] + way[temp][1]] = layer
                    dfs(layer+1)
                    #將四個點vis = False
                    vis[j][i] = False
                    vis[j + way[puzzle[layer][p][0]][0]][i + way[puzzle[layer][p][0]][1]] = False
                    vis[j + way[puzzle[layer][p][1]][0]][i + way[puzzle[layer][p][1]][1]] = False
                    direct = puzzle[layer][p][2]
                    if (direct > 10):
                        temp = direct%10#有的話temp不為0,99
                        direct = math.floor(direct/10)
                        vis[j + way[direct][0] + way[temp][0]][i + way[direct][1] + way[temp][1]] = False



dfs(1)
print(count)


