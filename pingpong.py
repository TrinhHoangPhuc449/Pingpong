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
        if keys[K_s] and self.rect.y<win_heaight - 80:
            self.rect.y + = self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y>5:
            self.rect.y -= self.speed
