import pygame 
pygame.init()
win = pygame.display.set_mode((1000,  500))
bg_img = pygame.image .load('desert_BG.png')
bg = pygame.transform.scale(bg_img,(1000, 500))
width = 1000
i = 0
pygame.display.set_caption("First Game")

x= 250
y=250
radius = 15
vel_x= 10
vel_y= 10

jump = False

run = True


run = True
while run:
    win.fill((0, 0, 0))
    win.blit(bg, (i,0)) 
    win.blit(bg, (width+i, 0)) 
    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0

    pygame.draw.circle(win, (255,255,255), (int(x), int(y)), radius)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
         x -= vel_x

    if userInput[pygame.K_RIGHT] and x < 500: 
         x += vel_x  
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True

    if jump is True:
        y -= vel_y
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10  
    
    win.blit(bg, (i,0)) 

    i -= 1 

    
    pygame.time.delay(30)
    pygame.display.update()

