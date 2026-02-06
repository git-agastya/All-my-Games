import pygame
import random
ball_x=random.randint(15,600-15)
ball_y=0
ball_speed=3
basket_x=250
clock=pygame.time.Clock()


pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("My First Game")
running =True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    ball_y+=ball_speed
    if ball_y>400:
        ball_x=random.randint(15,600-15)
        ball_y=0

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if basket_x>0:
            basket_x=basket_x-10
    
    if keys[pygame.K_RIGHT]:
        if basket_x<(600-100):
            basket_x=basket_x+10
    
    if basket_x<ball_x<basket_x+100:
        if 350<ball_y<350+20:
            print("Caught!")
            ball_x=random.randint(15,600-15)
            ball_y=0

    pygame.draw.rect(screen,(255,0,0),(basket_x,350,100,20))
    pygame.draw.circle(screen,(0,0,255),(ball_x,ball_y,),15)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

#0,0,0 is for black screen
#255,255,255 is for white screen
#600,400 is for an basic screen size for a game
#255,0,0 is for red
#0,255,0 is for green
#0,0,255 is for blue
#RGB