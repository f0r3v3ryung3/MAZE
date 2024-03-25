import pygame, time, random
pygame.init()
size = (1018, 640)
screen = pygame.display.set_mode(size)

color = (0, 255, 0)

pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1019, 640), 0)

Text = False
font = pygame.font.SysFont('serif', 20)
text = font.render('В этой игре вы проходите лабиринт. На W,A,S,D вы управляете своим песонажем(зеленным квадратиком).', True, (0, 0, 0))
screen.blit(text, (50, 200))

text = font.render('Вы проходите левый лабиринт, правый проходит ИИ(искуственный интелект). Оба лабиринта одиннаковые.', True, (0, 0, 0))
screen.blit(text, (50, 225))

text = font.render('Смысл игры дойти до красной точки быстрее ИИ. Если очень сложно, можете посматривать на ИИ', True, (0, 0, 0))
screen.blit(text, (75, 250))

font = pygame.font.SysFont('serif', 40)

text = font.render('Если поняли нажмите кнопку W', True, (0, 0, 0))
screen.blit(text, (200, 275))

pygame.display.update()

while Text == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Text = True
                
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1019, 641), 0)

k = 30

Win = False
Lab = [[32, 3], [293, 3], [32, 32], [61, 32], [90, 32], [119, 32], [148, 32], [206, 32], [235, 32], [293, 32], [322, 32], [351, 32], [380, 32], [409, 32], [438, 32], [148, 61], [235, 61], [380, 61], [438,61], [32, 90], [61, 90], [90, 90], [148,90], [177, 90], [206, 90], [235, 90], [293, 90], [351, 90], [380, 90], [438, 90], [90, 119], [293, 119], [351, 119], [32, 148], [61, 148], [90, 148], [148, 148], [177, 148], [206, 148], [235, 148], [264, 148], [293, 148], [322, 148], [351, 148], [380, 148], [409, 148], [438, 148], [32, 177], [177, 177], [438, 177], [3, 206], [32, 206], [90, 206], [119, 206], [148, 206], [177, 206], [235, 206], [264, 206], [293, 206], [322, 206], [351, 206], [380, 206], [438, 206], [90, 235], [293, 235], [380, 235], [438, 235], [32, 264], [90, 264], [119, 264], [148, 264], [177, 264], [206, 264], [235, 264], [293, 264], [351, 264], [380, 264], [409, 264], [438, 264], [32, 293], [235, 293], [293, 293], [351, 293], [32, 322], [61, 322], [90, 322], [119, 322], [177, 322], [235, 322], [409, 322], [438, 322], [90, 351], [177, 351], [235, 351], [264, 351], [293, 351], [351, 351], [438, 351], [32, 380], [61, 380], [90, 380], [119, 380], [177, 380], [351, 380], [380, 380], [409, 380], [438, 380], [467, 380], [32, 409], [119, 409], [177, 409], [235, 409], [264, 409], [293, 409], [351, 409], [32, 438], [90, 438], [119, 438], [148, 438], [177, 438], [293, 438], [409, 438], [438, 438], [32, 467], [177, 467], [206, 467], [235, 467], [293, 467], [322, 467], [351, 467], [380, 467], [409, 467], [32, 496], [61, 496], [90, 496], [119, 496], [177, 496], [235, 496], [293, 496], [119, 525], [177, 525], [235, 525], [264, 525], [293, 525], [351, 525], [380, 525], [409, 525], [438, 525], [3, 554], [32, 554], [61, 554], [119, 554], [177, 554], [351, 554], [438, 554], [3, 583], [61, 583], [90, 583], [119, 583], [177, 583], [206, 583], [235, 583], [322, 583], [293, 583], [351, 583], [409, 583], [438, 583], [3, 612], [293, 612]]

GameOver = False

x = 32
y = 3
xDot = 32
yDot = 3

while [x, y] in Lab:
    x = random.randint(0, 16) * (k - 1) + 3
    y = random.randint(0, 21) * (k - 1) + 3
    
while [xDot, yDot] in Lab and [xDot, yDot] != [x, y]:
    xDot = random.randint(0, 16) * (k - 1) + 3
    yDot = random.randint(0, 21) * (k - 1) + 3

pygame.draw.rect(screen, (255, 0, 0), (xDot, yDot, k - 4, k - 4), 0)
pygame.draw.rect(screen, (255, 0, 0), (xDot + 522, yDot, k - 4, k - 4), 0)

pygame.display.update()

for i in range(1, 1019, k - 1):
    pygame.draw.line(screen, (169, 169, 169), (i , 0), (i, 640), 1)
    
for j in range(1, 641, k - 1):
    pygame.draw.line(screen, (169, 169, 169), (0 , j), (1026, j), 1)

for i in range(1, 641, 29):
    pygame.draw.rect(screen, (128, 128, 128), (496, i + 2, k - 4, k - 4))
    
for j in range(0, len(Lab)):
    pygame.draw.rect(screen, (0, 0, 0), (Lab[j][0], Lab[j][1], k - 4, k - 4))
    
for j in range(0, len(Lab)):
    pygame.draw.rect(screen, (0, 0, 0), (Lab[j][0] + 522, Lab[j][1], k - 4, k - 4))
    
i = 0
    
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
            
            if [x + k - 1, y] == [xDot, yDot]:
                Dot = i + 1
            elif [x + k - 1, y] not in AllSteps and x + k - 1 < 1019 and [x + k - 1 - 522, y] not in Lab:
                Steps1 += [[x + k - 1, y, i + 1]]
                AllSteps += [[x + k - 1, y]]
                AllSteps2 += [[x + k - 1, y, i + 1]]
                
            if [x - k + 1, y] == [xDot, yDot]:
                Dot = i + 1
            elif [x - k + 1, y] not in AllSteps and x - k + 1 > 496 and [x - k + 1 - 522, y] not in Lab:
                Steps1 += [[x - k + 1, y, i + 1]]       
                AllSteps += [[x - k + 1, y]]
                AllSteps2 += [[x - k + 1, y, i + 1]]
                    
            if [x, y + k - 1] == [xDot, yDot]:
                Dot = i + 1 
            elif [x, y + k - 1] not in AllSteps and y + k - 1 < 640 and [x - 522, y + k - 1] not in Lab:
                Steps1 += [[x, y + k - 1, i + 1]]
                AllSteps += [[x, y + k - 1]]
                AllSteps2 += [[x, y + k - 1, i + 1]]   
                
            if [x, y - k + 1] == [xDot, yDot]:
                Dot = i + 1
            elif [x, y - k + 1] not in AllSteps and y - k + 1 > 0 and [x - 522, y - k + 1] not in Lab:
                Steps1 += [[x, y - k + 1, i + 1]]
                AllSteps += [[x, y - k + 1]]
                AllSteps2 += [[x, y - k + 1, i + 1]]
                
        Steps[:] = Steps1[:]
        
        Steps1 = []
    
    Steps = [[xDot, yDot, Dot]]
    j = 0
        
    while j < len(Steps):
        x = Steps[j][0]
        y = Steps[j][1]
        i = Steps[j][2]    
        
        if [x + k - 1 - 522, y] not in Lab and [x + k - 1, y, i - 1] in AllSteps2:
            Steps += [[x + k - 1, y, i - 1]]
                
        elif [x - k + 1 - 522, y] not in Lab and [x - k + 1, y, i - 1] in AllSteps2:
            Steps += [[x - k + 1, y, i - 1]]
                
        elif [x - 522, y + k - 1] not in Lab and [x, y + k - 1, i - 1] in AllSteps2:
            Steps += [[x, y + k - 1, i - 1]]
            
        elif [x - 522, y - k + 1] not in Lab and [x, y - k + 1, i - 1] in AllSteps2:
            Steps += [[x, y - k + 1, i - 1]]
            
        j += 1
    return Steps

pygame.draw.rect(screen, (0, 255, 0), (x, y, k - 4, k - 4))
pygame.display.update()

Steps = XY(k, x + 522, y, xDot + 522, yDot, Lab)

i = len(Steps) - 1

StartTime = time.time()
t = time.time() - StartTime

while GameOver == False:
    if x == xDot and y == yDot:
        GameOver = True
        Win = True
    if time.time() - StartTime >= t:
        t += 0.3
        pygame.draw.rect(screen, (0, 255, 0), (Steps[i][0], Steps[i][1], k - 4, k - 4))
        pygame.display.update()   
        
        if i != len(Steps) - 1:
            pygame.draw.rect(screen, (255, 255, 255), (Steps[i + 1][0], Steps[i + 1][1], k - 4, k - 4))
            pygame.display.update()               
        
        if i > 0:
            i -= 1
        else:
            GameOver = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and [x + k - 1, y] not in Lab and x + k - 1 < 496:
                    pygame.draw.rect(screen, (0, 255, 0), (x + k - 1, y, k - 4, k - 4))
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, k - 4, k - 4))
                    pygame.display.update()
                    x += k - 1
                    
                elif event.key == pygame.K_a and [x - k + 1, y] not in Lab and x - k + 1 > 0:
                    pygame.draw.rect(screen, (0, 255, 0), (x - k + 1, y, k - 4, k - 4))
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, k - 4, k - 4))
                    pygame.display.update()
                    x -= k - 1
                    
                elif event.key == pygame.K_s and [x, y + k - 1] not in Lab and y + k - 1 < 641:
                    pygame.draw.rect(screen, (0, 255, 0), (x, y + k - 1, k - 4, k - 4))
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, k - 4, k - 4))
                    pygame.display.update()
                    y += k - 1
                    
                elif event.key == pygame.K_w and [x, y - k + 1] not in Lab and y - k + 1 > 0:
                    pygame.draw.rect(screen, (0, 255, 0), (x, y - k + 1, k - 4, k - 4))
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, k - 4, k - 4))
                    pygame.display.update()
                    y -= k - 1

if Win == False:
    font2 = pygame.font.SysFont('serif', 100)
    text2 = font2.render("Game Over", True, (255, 0, 0))
     
    screen.blit(text2, (300, 250))
     
    pygame.display.update()
    
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
else:
    font2 = pygame.font.SysFont('serif', 100)
    text2 = font2.render(" You Win ", True, (0, 255, 0))
     
    screen.blit(text2, (300, 250))
     
    pygame.display.update()
    
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()    