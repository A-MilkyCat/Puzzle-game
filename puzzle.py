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
            vis[i][j] = True

puzzle = ['' for i in range(10)] 
puzzle[1] = [[6,8,81], [8,2,23], [2,5,45], [4,6,67]]
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

def dfs(layer):
    if (layer == 10):
        print('success')
    for i in range(9):
        for j in range(9):
            if(vis[i][j] == True):
                continue
            is_possible = True
            for p in range(len(puzzle[layer])):
                for q in range(4):
                    bufferx = i + (way[puzzle[layer][p][q]])
                    buffery = j + (way[puzzle[layer][p][q]])
            vis[i][j] = True

            







print(puzzle[1][2][1])
print(way[5])
for i in range(9):
    for j in range(9):
        print(board[i][j],end = '')
    print('')

