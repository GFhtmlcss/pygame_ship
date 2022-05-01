# import pygame
# from random import randint
#
#
# # ship - корабль и огонь
# class Ship(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load('image/ship.png'), (250, 250))
#         self.image.set_colorkey('WHITE')
#         self.rect = self.image.get_rect()
#         self.rect.x = window_width / 2 - 180
#         self.rect.y = window_height - window_height / 2
#         self.speed = 5
#
#         self.last = pygame.time.get_ticks()
#         self.last_green = pygame.time.get_ticks()
#         self.cooldown = 500
#         self.green_cooldown = self.cooldown / 4
#
#     def check(self):
#         if ship_check:
#             self.change_view('image/ship.png', 'WHITE', 250, 250)
#         else:
#             self.change_view('image/boom.png','WHITE', 250, 250)
#
#     def fire(self):
#         if now - self.last >= self.cooldown:
#             self.last = now
#             bullet = Gun()
#             bullets.add(bullet)
#
#         if now_green - self.last_green >= self.green_cooldown:
#             bullet_green = GreenGun()
#             bullets_green.add(bullet_green)
#             self.last_green = now_green
#
#             bullet_green_2 = GreenGun()
#             bullet_green_2.rect.x += 195
#             bullets_green.add(bullet_green_2)
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if ship_check:
#             if keys[pygame.K_a]:
#                 if self.rect.x > 0 and ship_check:
#                     self.rect.x -= self.speed
#             elif keys[pygame.K_d]:
#                 if self.rect.x < window_width - 250 and ship_check:
#                     self.rect.x += self.speed
#             if keys[pygame.K_w]:
#                 if self.rect.y > -10 and ship_check:
#                     self.rect.y -= self.speed
#             elif keys[pygame.K_s]:
#                 if self.rect.y < window_height - 250 and ship_check:
#                     self.rect.y += self.speed
#
#     def change_view(self, image, color, xscale=10, yscale=10):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load(image), (xscale, yscale))
#         self.image.set_colorkey(color)
#
#
# # оружие
# class Gun(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load('image/snaryad.png'), (30, 50))
#         self.image.set_colorkey('WHITE')
#         self.rect = self.image.get_rect()
#         self.rect.x = ship.rect.x + 112
#         self.rect.y = ship.rect.y
#         self.speed = 15
#
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < -50:
#             self.kill()
#
#
# # вторичное оружие
# class GreenGun(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load('image/greengun.png'), (15, 30))
#         self.image.set_colorkey('WHITE')
#         self.rect = self.image.get_rect()
#         self.rect.x =ship.rect.x + 20
#         self.rect.y = ship.rect.y
#         self.speed = 25
#
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < -50:
#             self.kill()
#
#
# #астероиды small
# class Asteroid(pygame.sprite.Sprite):
#     def __init__(self, y=0):
#         pygame.sprite.Sprite.__init__(self)
#         self.change_view('image/asteroid_small.png', 'WHITE', 64, 64)
#         self.rotate_image = self.image
#         self.rect = self.image.get_rect()
#         self.rect.x = randint(0 + 150, window_width - 150)
#         self.rect.y = y
#         self.speed = 1
#         self.angle = 0
#
#     def spawn_asteroid(self):
#         self.asteroid = Asteroid()
#         asteroids.add(asteroid)
#         # self.asteroid = Asteroid(-150)
#
#     def killing(self):
#         # self.check()
#         self.asteroid.kill()
#         asteroid.spawn_asteroid()
#
#     def change_view(self, image, color, xscale=10, yscale=10):
#         self.image = pygame.transform.scale(pygame.image.load(image), (xscale, yscale))
#         self.image.set_colorkey(color)
#
#     def check(self):
#         if asteroid_check:
#             self.change_view('image/asteroid_small.png', 'WHITE', 64, 64)
#         else:
#             self.change_view('image/boom.png','WHITE', 250, 250)
#
#     def update(self):
#         self.rect.y += self.speed
#         self.image = pygame.transform.rotate(self.rotate_image, self.angle)
#         self.image.set_colorkey('WHITE')
#         self.angle += 1
#         if self.rect.y > window_height:
#             self.killing()
#
#
# pygame.init()
#
# # для проверок
# ship_check = True
# asteroid_check = True
#
# # подсчет
# asteroid_check_balls = 0
#
# # Background
# window_width = 1100
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
#
# background = pygame.transform.scale(pygame.image.load('image/bg.jpg'), (window_width, window_height))
#
# # обьединения в группы
# ship = Ship()
# asteroid = Asteroid()
# bullets = pygame.sprite.Group()
# bullets_green = pygame.sprite.Group()
# asteroids = pygame.sprite.Group()
# asteroids.add(asteroid)
#
# # fps
# clock = pygame.time.Clock()
# FPS = 60
#
# # первый спавн, начальный
# asteroid.spawn_asteroid()
#
# # текст
# font = pygame.font.Font(None, 40)
# text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check_balls)
# text = font.render(text_text, True, [240, 160, 75])
# text_position = 15, 10
#
#
# # цикл
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 now = pygame.time.get_ticks()
#                 now_green = pygame.time.get_ticks()
#                 ship.fire()
#
#     # корабль и астероиды
#     asteroid_collide = pygame.sprite.spritecollide(ship, asteroids, False)
#     for i in asteroid_collide:
#         text_text = 'О нет! Ты врезался! Корабль сломан! Твой счет до смерти: {}'.format(asteroid_check_balls)
#         text = font.render(text_text, True, [240, 160, 75])
#         ship_check = False
#         ship.check()
#         asteroid.kill()
#         # asteroid.spawn_asteroid()
#
#     # пули и астероиды
#     bullets_asteroids = pygame.sprite.groupcollide(bullets, asteroids, True, False)
#     for i in bullets_asteroids:
#         i.kill()
#         asteroid.kill()
#         asteroid.asteroid = Asteroid()
#         asteroids.add(asteroid)
#
#
#         asteroid_check_balls += 1
#         text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check_balls)
#         text = font.render(text_text, True, [240, 160, 75])
#     bullets_asteroids = pygame.sprite.groupcollide(bullets_green, asteroids, True, False)
#     for i in bullets_asteroids:
#         i.kill()
#         asteroid.killing()
#
#         asteroid_check_balls += 1
#         text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check_balls)
#         text = font.render(text_text, True, [240, 160, 75])
#
#     # обновление
#     ship.update()
#     bullets.update()
#     bullets_green.update()
#     asteroids.update()
#
#     # рисование всего
#     window.blit(background, (0, 0))
#
#     bullets.draw(window)
#     bullets_green.draw(window)
#
#     window.blit(ship.image, (ship.rect.x, ship.rect.y))
#     window.blit(text, text_position)
#
#     asteroids.draw(window)
#
#     pygame.display.update()
#     clock.tick(FPS)
import pygame
from random import randint


# ship - корабль и огонь
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('image/ship.png'), (250, 250))
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = window_width / 2 - 180
        self.rect.y = window_height - window_height / 2
        self.speed = 5

        self.last = pygame.time.get_ticks()
        self.last_green = pygame.time.get_ticks()
        self.cooldown = 500
        self.green_cooldown = self.cooldown / 4

    def check(self):
        if ship_check:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('image/ship.png'), (250, 250))
            self.image.set_colorkey('WHITE')
        else:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('image/boom.png'), (250, 250))
            self.image.set_colorkey('WHITE')

    def fire(self):
        if now - self.last >= self.cooldown:
                self.last = now
                bullet = Gun()
                bullets.add(bullet)
        if now_green - self.last_green >= self.green_cooldown:
                bullet_green = GreenGun()
                bullets_green.add(bullet_green)
                self.last_green = now_green

                bullet_green_2 = GreenGun()
                bullet_green_2.rect.x += 195
                bullets_green.add(bullet_green_2)

    def update(self):
        keys = pygame.key.get_pressed()
        if ship_check:
            if keys[pygame.K_a]:
                if self.rect.x > 0 and ship_check == True:
                    self.rect.x -= self.speed
            elif keys[pygame.K_d]:
                if self.rect.x < window_width - 250 and ship_check == True:
                    self.rect.x += self.speed
            if keys[pygame.K_w]:
                if self.rect.y > -10 and ship_check == True:
                    self.rect.y -= self.speed
            elif keys[pygame.K_s]:
                if self.rect.y < window_height - 250 and ship_check == True:
                    self.rect.y += self.speed


# оружие
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('image/snaryad.png'), (30, 50))
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x + 112
        self.rect.y = ship.rect.y
        self.speed = 15

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()


# вторичное оружие
class GreenGun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('image/greengun.png'), (15, 30))
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x + 20
        self.rect.y = ship.rect.y
        self.speed = 25

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()


# астероиды small
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/asteroid_small.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image.set_colorkey('WHITE')
        self.rotate_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 150
        self.speed = 5
        self.angle = 0

    def spawn_asteroid(self):
        self.asteroid = Asteroid()
        self.rect.x = randint(0 + 150, window_width - 150)
        self.rect.y = randint(50, 100)
        self.rect_x = self.rect.x
        self.rect_y = self.rect.y

    def killing(self):
        self.last = pygame.time.get_ticks()
        self.asteroid.kill()
        if self.last > 1000:
            asteroid.spawn_asteroid()
            asteroids.add(asteroid)

    def update(self):
        self.rect.y += self.speed
        self.image = pygame.transform.rotate(self.rotate_image, self.angle)
        self.image.set_colorkey('WHITE')
        self.angle += 1
        if self.rect.y > window_height:
            self.killing()


pygame.init()

# для проверок
ship_check = True

# подсчет
asteroid_check = 0

# Background
window_width = 1100
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

background = pygame.transform.scale(pygame.image.load('image/bg.jpg'), (window_width, window_height))

# обьединения в группы
ship = Ship()
asteroid = Asteroid()
bullets = pygame.sprite.Group()
bullets_green = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroids.add(asteroid)

# fps
clock = pygame.time.Clock()
FPS = 60

# первый спавн, начальный
asteroid.spawn_asteroid()

# текст
font = pygame.font.Font(None, 40)
text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check)
text = font.render(text_text, True, [240, 160, 75])
text_position = 15, 10

# цикл
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                now_green = pygame.time.get_ticks()
                ship.fire()

    # корабль и астероиды
    asteroid_collide = pygame.sprite.spritecollide(ship, asteroids, False)
    for i in asteroid_collide:
        text_text = 'О нет! Ты врезался! Корабль сломан! Твой счет до смерти: {}'.format(asteroid_check)
        text = font.render(text_text, True, [240, 160, 75])
        ship_check = False
        ship.check()

    # пули и астероиды
    bullets_asteroids = pygame.sprite.groupcollide(bullets, asteroids, True, False)
    for i in bullets_asteroids:
        i.kill()
        asteroid.killing()

        asteroid_check += 1
        text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check)
        text = font.render(text_text, True, [240, 160, 75])
    bullets_asteroids = pygame.sprite.groupcollide(bullets_green, asteroids, True, False)
    for i in bullets_asteroids:
        i.kill()
        asteroid.killing()

        asteroid_check += 1
        text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check)
        text = font.render(text_text, True, [240, 160, 75])

    # обновление
    ship.update()
    bullets.update()
    bullets_green.update()
    asteroids.update()

    # рисование всего
    window.blit(background, (0, 0))

    bullets.draw(window)
    bullets_green.draw(window)

    window.blit(ship.image, (ship.rect.x, ship.rect.y))
    window.blit(text, text_position)

    asteroids.draw(window)

    pygame.display.update()
    clock.tick(FPS)