from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y< win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<win_height-80:
            self.rect.y += self.speed
class Middle_racket(GameSprite):
    direction = "Up"
    def auto_move(self):
       
        if self.rect.y < 10 and self.direction=="Up":
            self.direction = "Down"
        elif self.rect.y > win_height-50 and self.direction=="Down" :
            self.direction = "Up"

        if self.direction == "Down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
#Game scence
back = (200,255,255) #background color
win_width = 1000
win_height = 600
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png',30,200,50,150,5)
racket_m = Middle_racket('racket.png', win_width/2 ,200,50,150,5)
racket_r = Player('racket.png',win_width-60 ,200,50,150,5)
ball = GameSprite('download.jpg',200,200,70,70,5)
font.init()
font_label = font.Font(None,40)
lose_1 = font_label.render('PLAYER ONE LOSE!',True,(255,50,50))
lose_2 = font_label.render('PLAYER ONE LOSE!',True,(50,50,255))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_1.update_1()
        racket_r.update_r()
        racket_m.auto_move()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_r,ball)or sprite.collide_rect(racket_m,ball):
            speed_x*=-1
            speed_y*=-1
        if ball.rect.y > win_height-50 or ball.rect.y<0:
            speed_y *=-1
        if ball.rect.x<0:
            finish = True
            window.blit(lose_1,(200,200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_2,(200,200))
        racket_1.reset()
        racket_r.reset()
        racket_m.reset()
        ball.reset()
        display.update()
        clock.tick(FPS)
