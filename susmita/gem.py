import pygame
pygame.init()
x=0
y=0
flag=2
player_width=94
lane_width=900/3
screen_width=900
screen_height=600
player_y=400
screen=pygame.display.set_mode((screen_width,screen_height))
background_image=pygame.image.load('road.png').convert()
car_image=pygame.image.load('car.png').convert_alpha()
running=True
while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             running=False
        if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT or event.key == ord('a'):
                 if flag<=1: continue
                 flag-=1
             if event.key==pygame.K_RIGHT or event.key == ord('d'):
                 if flag>=3: continue
                 flag+=1
        if event.type==pygame.KEYUP:
            pass
    rel_y=y% screen_height
    print("rel_y-screen_height{}".format(rel_y-screen_height))
    screen.blit(background_image,(x,(rel_y-screen_height)))
    if(rel_y<screen_height):
        screen.blit(background_image,(x,rel_y))
    y=y%screen_height
    y=y+1
    player_x=flag*lane_width-(lane_width+player_width)/2
    
    screen.blit(car_image,(player_x,player_y,))
    pygame.display.update()
