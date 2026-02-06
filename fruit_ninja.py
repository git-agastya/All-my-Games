import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Fruit Ninja')


WHITE=(255,255,255)

font=pygame.font.SysFont("Arial",30)

fruit_images=[
    pygame.image.load(r'apple.png'),
    pygame.image.load(r'banana.png'),
    pygame.image.load(r'watermelon.png')
]

fruit_images=[pygame.transform.scale(fruit,(60,60)) for fruit in fruit_images]

background=pygame.image.load('background.jpg')
background=pygame.transform.scale(background,(800,600))

clock=pygame.time.Clock()

score=0
running=True
fruits=[]

class Fruit:
    def __init__(self,x,y,fruit_image):
        self.x=x
        self.y=y
        self.image=fruit_image
        self.rect=self.image.get_rect(center=(self.x, self.y))
        self.velocity=random.randint(5, 10)

    def update(self):
        self.y-=self.velocity
        self.rect.center=self.x,self.y
        if self.y<0:
            fruits.remove(fruit)
        
    def draw(self):
        screen.blit(self.image, self.rect)


while running:
    screen.fill(WHITE)

    screen.blit(background, (0,0))

    if random.randint(1,100)<2:
        fruit=Fruit(
            random.randint(50, 750),
            600,
            random.choice(fruit_images)
        )
        fruits.append(fruit)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()

            for fruit in fruits:
                if fruit.rect.collidepoint(mouse_x,mouse_y):
                    fruits.remove(fruit)
                    score+=10

        for fruit in fruits:
            fruit.update()
            fruit.draw()

    score_text=font.render(f"Score: {score}", True, WHITE)

    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()            