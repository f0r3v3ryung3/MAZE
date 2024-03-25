import pygame, time, random, sys
pygame.init()
sys.setrecursionlimit(100000000)
k = 10
n = 135
m = 61
size = (n * k + 1, m * k + 1)
screen = pygame.display.set_mode(size)

color = (0, 255, 0)

pygame.draw.rect(screen, (0, 0, 0), (0, 0, n * k + 1, m * k + 1), 0)

x = 2 + k
y = 2 + k
i = 0
Lab = [[2 + k, 2 + k]]
xDot = (n - 2) * k + 2
yDot = (m - 2) * k + 2

pygame.display.update()

for i in range(0, n * k, k):
    pygame.draw.line(screen, (169, 169, 169), (i , 0), (i, m * k), 1)
    
for j in range(0, m * k, k):
    pygame.draw.line(screen, (169, 169, 169), (0 , j), (n * k, j), 1)
    
pygame.display.update()

def XY(k, x, y, xDot, yDot, Lab):
    Steps1 = []
    Dot = 0
    i = 0
    Steps = [[x, y, i]]
    AllSteps = [[x, y]]
    AllSteps2 = [[x, y, 0]]
    while len(Steps) > 0 and Dot == 0:
        for j in range(0, len(Steps)):
            x = Steps[j][0]
            y = Steps[j][1]
            i = Steps[j][2]

            if [x + k, y] == [xDot, yDot]:
                Dot = i + 1            
            elif [x + k, y] not in AllSteps and [x + k, y] in Lab and x + k < n * k + 1:
                Steps1 += [[x + k, y, i + 1]]
                AllSteps += [[x + k, y]]
                AllSteps2 += [[x + k, y, i + 1]]
                    
            if [x - k, y] == [xDot, yDot]:
                Dot = i + 1
            elif [x - k, y] not in AllSteps and [x - k, y] in Lab and x - k > 0:
                Steps1 += [[x - k, y, i + 1]]
                AllSteps += [[x - k, y]]
                AllSteps2 += [[x - k, y, i + 1]]
            
            if [x, y + k] == [xDot, yDot]:
                Dot = i + 1          
            elif [x, y + k] not in AllSteps and [x, y + k] in Lab and y + k < m * k + 1:
                Steps1 += [[x, y + k, i + 1]]
                AllSteps += [[x, y + k]]
                AllSteps2 += [[x, y + k , i + 1]]          
            
            if [x, y - k] == [xDot, yDot]:
                Dot = i + 1    
            elif [x, y - k] not in AllSteps and [x, y - k] in Lab and y - k > 0:
                Steps1 += [[x, y - k , i + 1]]
                AllSteps += [[x, y - k]]
                AllSteps2 += [[x, y - k, i + 1]]
                
        Steps[:] = Steps1[:]
        
        Steps1 = []
    
    Steps = [[xDot, yDot, Dot]]
    j = 0
        
    while j < len(Steps):
        x = Steps[j][0]
        y = Steps[j][1]
        i = Steps[j][2]    
        
        if [x + k, y, i - 1] in AllSteps2:
            Steps += [[x + k, y, i - 1]]
                
        elif [x - k, y, i - 1] in AllSteps2:
            Steps += [[x - k, y, i - 1]]
                
        elif [x, y + k, i - 1] in AllSteps2:
            Steps += [[x, y + k, i - 1]]
            
        elif [x, y - k, i - 1] in AllSteps2:
            Steps += [[x, y - k, i - 1]]
            
        j += 1
    return Steps

Labi = []
for i in range(0, n):
    a = []
    for j in range(0, m):
        a += [0]
    Labi += [a]


def lab(x, y, m, n, k):
    global Labi, Lab
    Labi[x][y] = 1
    d = [(x - 2, y, x - 1, y), (x + 2, y, x + 1, y), (x, y - 2, x, y - 1), (x, y + 2, x, y + 1)]
    random.shuffle(d)
    for i in d:
        if i[0] > 0 and i[0] < n and i[1] > 0 and i[1] < m and Labi[i[0]][i[1]] == 0:
            Labi[i[2]][i[3]] = 1
            Lab += [[i[0] * k + 2, i[1] * k + 2], [i[2] * k + 2, i[3] * k + 2]]
            lab(i[0], i[1], m, n, k)

lab(1, 1, m, n, k)

for i in Lab:
    pygame.draw.rect(screen, (255, 255, 255), (i[0], i[1], k - 3, k - 3))
    pygame.display.update()

        
Steps = XY(k, x, y, xDot, yDot, Lab)
for i in range(0, len(Steps)):
    pygame.draw.rect(screen, (0, 255, 0), (Steps[i][0], Steps[i][1], k - 3, k - 3))
    pygame.display.update()

time.sleep(999999)