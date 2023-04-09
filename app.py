from pygame import *

speed_x=3
speed_y=3







class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(
            player_image), (wight, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# test commentt
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


ball=GameSprite('ball.png',200,200,4,50,50)

rocket1=Player('1.png',30,200,4,50,150)

rocket2=Player('2.png',520,200,4,50,150)

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.rect.x += speed_x
    ball.rect.y += speed_y


    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x > win_width-50 or ball.rect.x < 0:
        speed_x *= -1

    if sprite.collide_rect(rocket1,ball)or sprite.collide_rect(rocket2,ball):
        speed_x *= -1
    rocket1.update_r()
    rocket2.update_l()
    ball.reset()
    rocket1.reset()
    rocket2.reset()
    display.update()
    clock.tick(FPS) 

