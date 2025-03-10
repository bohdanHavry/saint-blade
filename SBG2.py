# підключаємо бібліотеку, імпортуємо модулі
import sys
import pygame
import pygame.key
import random
import time
pygame.init()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, height, groups = []):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))


    def draw(self, surface, camera_offset=pygame.Vector2(0, 0)):
        surface.blit(self.image, self.rect.topleft + camera_offset)
        pygame.draw.rect(surface, (255, 0, 0), self.rect.move(camera_offset), 2)

    # для класу gamesprite треба зробити перевірку натискання по нашому об'єкту
    def is_clicked(self, mouse_pos): # до нашого методу передаємо координати події клік
        return self.rect.collidepoint(mouse_pos) # перевіряємо чи натискаємо по об'єкту 
                                                 # функцією collidepoint і передаємо коор як аргумент

def update_camera(hero, screen_width):
    return pygame.Vector2(screen_width // 2 - 100 - hero.rect.centerx, 0)

def scrolling(startwindow, background_image, camera_offset, speed_factor=1.0):
    
    bg_x = camera_offset.x * speed_factor
    bg_x %= background_image.get_width()  #циклюємо фон

    startwindow.blit(background_image, (bg_x, 0))
    if bg_x > 0:
        startwindow.blit(background_image, (bg_x - background_image.get_width(), 0))


# логіка роботи кнопок
def start_new_game():
    startwindow = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Saint Blade')

    barrier = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    objects = pygame.sprite.Group()
    subject = pygame.sprite.Group()


    fon3 = GameSprite(0, 0, "vizyal/texture/legasy/Background/fon3.png", window.get_width(), window.get_height())
    fon4 = GameSprite(0, 0, "vizyal/texture/oak_woods_v1.0/background/fon1.png", window.get_width(), window.get_height())
    fon5 = GameSprite(0, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon6 = GameSprite(300, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon7 = GameSprite(600, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon8 = GameSprite(900, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon13s = GameSprite(1200, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon14s = GameSprite(1500, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon15s = GameSprite(1800, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon16s = GameSprite(2100, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon17s = GameSprite(2400, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon18s = GameSprite(2700, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon19s = GameSprite(3000, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon20s = GameSprite(3300, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon21s = GameSprite(3600, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon22s = GameSprite(3900, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon23s = GameSprite(4200, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon24s = GameSprite(4500, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon25s = GameSprite(4800, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon26s = GameSprite(5100, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon27s = GameSprite(5400, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon28s = GameSprite(5700, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon29s = GameSprite(6000, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon30s = GameSprite(6300, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon31s = GameSprite(6600, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon32s = GameSprite(6900, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon33s = GameSprite(7200, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon34s = GameSprite(7500, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon35s = GameSprite(7800, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon36s = GameSprite(8100, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon37s = GameSprite(8400, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon38s = GameSprite(8700, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon39s = GameSprite(9000, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon40s = GameSprite(9300, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon41s = GameSprite(9600, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon42s = GameSprite(9900, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon43s = GameSprite(10200, 500, "vizyal/texture/Background/map.png", 300, 150)
    fon44s = GameSprite(10500, 500, "vizyal/texture/Background/map.png", 300, 150)

   

    fon9 = GameSprite(-125, 207, "vizyal/texture/Background/wall.png", 150, 300)
    fon10 = GameSprite(-125, 0, "vizyal/texture/Background/wall.png", 150, 300)
    fon11 = GameSprite(-500, 0, "vizyal/texture/Background/wall2.png", 500, 500)
    fon12 = GameSprite(-500, 500, "vizyal/texture/Background/wall2.png", 500, 500)
    fon13 = GameSprite(9990, 215, "vizyal/texture/Background/wall3.png", 150, 300)
    fon14 = GameSprite(9990, 0, "vizyal/texture/Background/wall3.png", 150, 300)
    fon15 = GameSprite(10125, 0, "vizyal/texture/Background/wall2.png", 500, 500)
    fon16 = GameSprite(10125, 500, "vizyal/texture/Background/wall2.png", 500, 500)

    fon1dop = GameSprite(0, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon2dop = GameSprite(300, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon3dop = GameSprite(500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon4dop = GameSprite(600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon5dop = GameSprite(900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon6dop = GameSprite(1100, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon7dop = GameSprite(1200, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon8dop = GameSprite(1500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon9dop = GameSprite(1800, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon10dop = GameSprite(1900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon11dop = GameSprite(2000, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon12dop = GameSprite(2300, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon13dop = GameSprite(2500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon14dop = GameSprite(2600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon15dop = GameSprite(2900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon16dop = GameSprite(3100, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon17dop = GameSprite(3200, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon18dop = GameSprite(3500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon19dop = GameSprite(3600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon20dop = GameSprite(3900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon21dop = GameSprite(4000, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon22dop = GameSprite(4300, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon23dop = GameSprite(4500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon24dop = GameSprite(4600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon25dop = GameSprite(4900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon26dop = GameSprite(5100, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon27dop = GameSprite(5200, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon28dop = GameSprite(5500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon29dop = GameSprite(5700, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon30dop = GameSprite(5800, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon31dop = GameSprite(6100, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon32dop = GameSprite(6200, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon33dop = GameSprite(6500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon34dop = GameSprite(6600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon35dop = GameSprite(6700, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon36dop = GameSprite(7000, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon37dop = GameSprite(7100, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon38dop = GameSprite(7200, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon39dop = GameSprite(7500, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon40dop = GameSprite(7600, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon41dop = GameSprite(7900, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon42dop = GameSprite(8000, 12, "vizyal/texture/Background/trees.png", 400, 500)
    fon43dop = GameSprite(8300, 110, "vizyal/texture/Background/house-a.png", 300, 400)
    fon44dop = GameSprite(8580, 110, "vizyal/texture/Background/house-b.png", 300, 400)
    fon45dop = GameSprite(8900, 110, "vizyal/texture/Background/house-c.png", 300, 400)
    fon46dop = GameSprite(9200, 110, "vizyal/texture/Background/house-b.png", 300, 400)
    fon47dop = GameSprite(8860, 410, "vizyal/texture/Background/wagon.png", 100, 100)
    fon48dop = GameSprite(8580, 460, "vizyal/texture/Background/crate.png", 50, 50)
    fon49dop = GameSprite(9170, 410, "vizyal/texture/Background/crate-stack.png", 100, 100)
    fon50dop = GameSprite(9500, 110, "vizyal/texture/Background/chuch.png", 500, 400)
    

    fon1sup = GameSprite(0, 460, "vizyal/texture/Background/zabor.png", 200, 50)
    fon2sup = GameSprite(200, 460, "vizyal/texture/Background/zabor2.png", 200, 50)
    fon3sup = GameSprite(400, 460, "vizyal/texture/Background/zabor.png", 200, 50)
    fon4sup = GameSprite(600, 460, "vizyal/texture/Background/zabor.png", 200, 50)
    fon5sup = GameSprite(100, 310, "vizyal/texture/Background/street-lamp.png", 100, 200)
    fon6sup = GameSprite(650, 310, "vizyal/texture/Background/street-lamp.png", 100, 200)
    fon7sup = GameSprite(1100, 310, "vizyal/texture/Background/street-lamp.png", 100, 200)
    fon8sup = GameSprite(1600, 310, "vizyal/texture/Background/street-lamp.png", 100, 200)
    fon9sup = GameSprite(2000, 465, "vizyal/texture/Background/peni.png", 50, 50)
    fon10sup = GameSprite(7900, 410, "vizyal/texture/Background/well.png", 100, 100)
    fon11sup = GameSprite(4000, 265, "vizyal/texture/Background/war.png", 100, 250)
    fon12sup = GameSprite(4150, 310, "vizyal/texture/Background/stone.png", 400, 200)
    fon13sup = GameSprite(4600, 265, "vizyal/texture/Background/war2.png", 100, 250)
    fon14sup = GameSprite(2100, 460, "vizyal/texture/Background/koster.png", 100, 50)
    


    hero = Player(350, fon5.rect.top - 130, "vizyal/pers/right/idle1.png", "vizyal/pers/right/idle1.png", 65, 125, 0, 0)
    enemy1 = Enemy1(window.get_width(), 100, 'vizyal/monstersles/Monster_2/left/idle0.png', 'vizyal/monstersles/Monster_2/left/idle0.png', 100, 100, 0, 0, 600, 1200, 'Monster_2')    
    enemy2 = Enemy1(4500, 350, 'vizyal/monstersles/Monster_5/right/fly0.png', 'vizyal/monstersles/Monster_5/right/fly0.png', 100, 100, 0, 0, 4500,5500 , 'Monster_5')
    enemy3 = Enemy1(2800, 460, 'vizyal/monstersles/Monster_7/right/fly0.png', 'vizyal/monstersles/Monster_7/right/fly0.png', 100, 100, 0, 0, 2000,2900 , 'Monster_7')
    enemy4 =  Enemy1(4300, 460, 'vizyal/monstersles/Monster_9/right/fly0.png', 'vizyal/monstersles/Monster_9/right/fly0.png', 100, 100, 0, 0, 4300,4600 , 'Monster_9')
    enemy5 = Enemy1(9000, 350, 'vizyal/monstersles/Monster_1/right/fly0.png', 'vizyal/monstersles/Monster_1/right/fly0.png', 200, 200, 0, 0, 9000,9100 , 'Monster_1')
    enemy6 = Enemy1(2300, 100, 'vizyal/monstersles/Monster_2/left/idle0.png', 'vizyal/monstersles/Monster_2/left/idle0.png', 100, 100, 0, 0, 2300, 3000, 'Monster_2')    
    enemy7 = Enemy1(3600, 350, 'vizyal/monstersles/Monster_5/right/fly0.png', 'vizyal/monstersles/Monster_5/right/fly0.png', 100, 100, 0, 0, 3000,3600 , 'Monster_5')
    enemy8 = Enemy1(3100, 460, 'vizyal/monstersles/Monster_7/right/fly0.png', 'vizyal/monstersles/Monster_7/right/fly0.png', 100, 100, 0, 0, 2600,3100 , 'Monster_7')
    enemy9 =  Enemy1(3900, 460, 'vizyal/monstersles/Monster_9/right/fly0.png', 'vizyal/monstersles/Monster_9/right/fly0.png', 100, 100, 0, 0, 3900,4300 , 'Monster_9')
    enemy10 = Enemy1(9400, 350, 'vizyal/monstersles/Monster_1/right/fly0.png', 'vizyal/monstersles/Monster_1/right/fly0.png', 200, 200, 0, 0, 9400,9500 , 'Monster_1')
    healthbar = Player(20, fon5.rect.top - 365,'vizyal/buttons/bars/bar1.png','vizyal/buttons/bars/bar1.png', 35, 265, 0, 0)
    

    camera_offset = pygame.Vector2(0, 0)
    barrier.add(fon5, fon6, fon7, fon8, fon13s, fon14s, fon15s, fon16s, fon17s, fon18s, fon19s, fon20s, fon21s, fon22s, fon23s, fon24s, fon25s, fon26s, fon27s, fon28s, fon29s, fon30s, fon31s, fon32s, fon33s, fon34s, fon35s, fon36s, fon37s, fon38s, fon39s, fon40s, fon41s, fon42s, fon43s, fon44s)
    walls.add(fon9, fon10, fon11, fon12,fon13,fon14,fon15,fon16)
    enemys.add(enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10)
    objects.add(fon1dop,fon2dop,fon3dop,fon4dop,fon5dop,fon6dop,fon7dop,fon8dop,fon9dop,fon10dop,fon11dop,fon12dop,fon13dop,fon14dop,fon15dop,fon16dop,fon17dop,fon18dop,fon19dop,fon20dop,fon21dop,fon22dop,fon23dop,fon24dop,fon25dop,fon26dop,fon27dop,fon28dop,fon29dop,fon30dop,fon31dop,fon32dop,fon33dop,fon34dop,fon35dop,fon36dop,fon37dop,fon38dop,fon39dop,fon40dop,fon41dop,fon42dop,fon43dop,fon44dop,fon45dop,fon46dop,fon47dop,fon48dop,fon49dop,fon50dop)
    subject.add(fon1sup,fon2sup,fon3sup,fon4sup,fon5sup,fon6sup,fon7sup,fon8sup,fon9sup,fon10sup,fon11sup,fon12sup,fon13sup,fon14sup)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                hero.go = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not hero.Attack:
                    hero.Attack = True
                    hero.attack_timer = 15
                    hero.Frame = 0    

        key_press = pygame.key.get_pressed()
        
        if key_press[pygame.K_d]:
            hero.dx = 10
            hero.go = True
            hero.Left = False
            hero.Right = True

        if key_press[pygame.K_a]:
            hero.dx = -10
            hero.go = True
            hero.Left = True
            hero.Right = False

        if key_press[pygame.K_w]:
            if hero.OnGround:
                hero.dy = -8
                hero.OnGround = False
                hero.Jump = True

        if hero.climbing:  # Якщо персонаж лізе по стіні
            hero.dy = 1  # Медленне сповзання вниз
            if key_press[pygame.K_w]:  # Рух вгору
                hero.dy = -4
                hero.OnGround = False
                hero.Jump = False
            if key_press[pygame.K_s]:  # Рух вниз
                hero.dy = 4
                hero.OnGround = True
                hero.Jump = False
        else:
            hero.dy += 1  # Гравітація, якщо персонаж не лізе по стіні
        #чтобы враг не летал
        if enemy1.OnGround:
            hero.OnGround = False
            enemy1.OnGround = True

        # Обробка атаки ворога
        if enemy1.Attack:
            if enemy1 and not enemy1.Dead and hero.rect.colliderect(enemy1.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        # Оновлення атаки ворога
        if enemy1.rect.colliderect(hero.rect):
            if not enemy1.Attack:
                enemy1.Attack = True
                enemy1.attack_timer = 10
                enemy1.Frame = 0

            if enemy1.Attack:
                enemy1.attack_timer -= 1
                if enemy1.attack_timer <= 0:
                    enemy1.Attack = False 
   
        if enemy2.Attack:
            if enemy2 and not enemy2.Dead and hero.rect.colliderect(enemy2.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy2.rect.colliderect(hero.rect):
            if not enemy2.Attack:
                enemy2.Attack = True
                enemy2.attack_timer = 10
                enemy2.Frame = 0

            if enemy2.Attack:
                enemy2.attack_timer -= 1
                if enemy2.attack_timer <= 0:
                    enemy2.Attack = False 


        if enemy3.Attack:
            if enemy3 and not enemy3.Dead and hero.rect.colliderect(enemy3.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy3.rect.colliderect(hero.rect):
            if not enemy3.Attack:
                enemy3.Attack = True
                enemy3.attack_timer = 10
                enemy3.Frame = 0

            if enemy3.Attack:
                enemy3.attack_timer -= 1
                if enemy3.attack_timer <= 0:
                    enemy3.Attack = False 

        if enemy4.Attack:
            if enemy4 and not enemy4.Dead and hero.rect.colliderect(enemy4.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy4.rect.colliderect(hero.rect):
            if not enemy4.Attack:
                enemy4.Attack = True
                enemy4.attack_timer = 10
                enemy4.Frame = 0

            if enemy4.Attack:
                enemy4.attack_timer -= 1
                if enemy4.attack_timer <= 0:
                    enemy4.Attack = False
        
        if enemy5.Attack:
            if enemy5 and not enemy5.Dead and hero.rect.colliderect(enemy5.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy5.rect.colliderect(hero.rect):
            if not enemy5.Attack:
                enemy5.Attack = True
                enemy5.attack_timer = 10
                enemy5.Frame = 0

            if enemy5.Attack:
                enemy5.attack_timer -= 1
                if enemy5.attack_timer <= 0:
                    enemy5.Attack = False


        if enemy6.Attack:
            if enemy6 and not enemy6.Dead and hero.rect.colliderect(enemy6.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy6.rect.colliderect(hero.rect):
            if not enemy6.Attack:
                enemy6.Attack = True
                enemy6.attack_timer = 10
                enemy6.Frame = 0

            if enemy6.Attack:
                enemy6.attack_timer -= 1
                if enemy6.attack_timer <= 0:
                    enemy6.Attack = False

        if enemy7.Attack:
            if enemy7 and not enemy7.Dead and hero.rect.colliderect(enemy7.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy7.rect.colliderect(hero.rect):
            if not enemy7.Attack:
                enemy7.Attack = True
                enemy7.attack_timer = 10
                enemy7.Frame = 0

            if enemy7.Attack:
                enemy7.attack_timer -= 1
                if enemy7.attack_timer <= 0:
                    enemy7.Attack = False


        if enemy8.Attack:
            if enemy8 and not enemy8.Dead and hero.rect.colliderect(enemy8.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy8.rect.colliderect(hero.rect):
            if not enemy8.Attack:
                enemy8.Attack = True
                enemy8.attack_timer = 10
                enemy8.Frame = 0

            if enemy8.Attack:
                enemy8.attack_timer -= 1
                if enemy8.attack_timer <= 0:
                    enemy8.Attack = False
        
        if enemy9.Attack:
            if enemy9 and not enemy9.Dead and hero.rect.colliderect(enemy9.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy9.rect.colliderect(hero.rect):
            if not enemy9.Attack:
                enemy9.Attack = True
                enemy9.attack_timer = 10
                enemy9.Frame = 0

            if enemy9.Attack:
                enemy9.attack_timer -= 1
                if enemy9.attack_timer <= 0:
                    enemy9.Attack = False
        
        if enemy10.Attack:
            if enemy10 and not enemy10.Dead and hero.rect.colliderect(enemy10.attack_hitbox):
                hero.take_damage(10, healthbar)

                
                if hero.health <= 0:
                    hero.death() # cмерть нашего героя 
                    end_screen()

        if enemy10.rect.colliderect(hero.rect):
            if not enemy10.Attack:
                enemy10.Attack = True
                enemy10.attack_timer = 10
                enemy10.Frame = 0

            if enemy10.Attack:
                enemy10.attack_timer -= 1
                if enemy10.attack_timer <= 0:
                    enemy10.Attack = False




        # Перевірка зіткнень з бар'єрами
        collided_barriers = pygame.sprite.spritecollide(hero, barrier, False)
        for barrier_obj in collided_barriers:
            if -barrier_obj.rect.width < barrier_obj.rect.x + camera_offset.x < startwindow.get_width():
                if hero.dy > 0 and hero.rect.bottom > barrier_obj.rect.top - 5:
                    hero.rect.bottom = barrier_obj.rect.top + 20
                    hero.dy = 0
                    hero.OnGround = True
                    hero.Jump = False
    
        # Оновлення стану гравця
        hero.update(startwindow.get_rect().height - hero.rect.height, walls=walls, enemys = enemys)

        # Оновлення камери
        camera_offset = update_camera(hero, startwindow.get_width())

        # Відображення фону з ефектом прокрутки
        scrolling(startwindow, fon3.image, camera_offset, 0.25)
        scrolling(startwindow, fon4.image, camera_offset, 0.5)

        # Відображення бар'єрів
        for obj in barrier:
            if -obj.rect.width < obj.rect.x + camera_offset.x < startwindow.get_width():
                obj.draw(startwindow, camera_offset)

        # Відображення стін
        for obj in walls:
            if -obj.rect.width < obj.rect.x + camera_offset.x < startwindow.get_width():
                obj.draw(startwindow, camera_offset)


        for obj in objects:
            if -obj.rect.width < obj.rect.x + camera_offset.x < startwindow.get_width():
                obj.draw(startwindow, camera_offset)
        
        for obj in subject:
            if -obj.rect.width < obj.rect.x + camera_offset.x < startwindow.get_width():
                obj.draw(startwindow, camera_offset)

        for obj in enemys:
            if -obj.rect.width < obj.rect.x + camera_offset.x < startwindow.get_width():
                obj.draw(startwindow, camera_offset)

        # Відображення гравця
        hero.draw(startwindow, camera_offset)

        # Відображення хелсбара
        healthbar.draw(startwindow)
        
        # Оновлення ворогів
        enemys.update(hero, enemys)
        # Оновлення екрану
        pygame.display.update()
        clock.tick(fps)


def open_settings():
    setting = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Настройки')
    
    Options = pygame.sprite.Group()

    OPTION = GameSprite(0, 0, "vizyal/texture/oak_woods_v1.0/background/fon2.png", window.get_width(), window.get_height())
    OPTION2 = GameSprite(-6, 15, "vizyal/buttons/GameMenu/1x/fon1.png", window.get_width(), window.get_height())
    fonButton = GameSprite(445, 400,"vizyal/buttons/FREE icon collection/1024/fots.png",100,100)
    Back_button = GameSprite(458, 415,"vizyal/buttons/FREE icon collection/1024/back.png",70,70)
    
    Options.add(OPTION)
    Options.add(OPTION2)
    Options.add(fonButton)
    Options.add(Back_button)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Back_button.is_clicked(mouse_pos):
                    return

        Options.draw(setting)
        pygame.display.update()
        clock.tick(fps)


def quit_game():
    pygame.quit()
    exit()

def end_screen():
    end_screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Saint Blade')
    
    group = pygame.sprite.Group()

    dead = GameSprite(0, 0, "vizyal/texture/dead.jpg", window.get_width(), window.get_height())
    main = GameSprite(150, 500,"vizyal/buttons/GameMenu/1x/main.png",285,65)
    cont = GameSprite(550, 500,"vizyal/buttons/GameMenu/1x/cont.png",285,65)
    
    group.add(dead)
    group.add(main)
    group.add(cont)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if cont.is_clicked(mouse_pos):
                    return start_new_game()
                elif main.is_clicked(mouse_pos):
                    return menu()

        group.draw(end_screen)
        pygame.display.update()
        clock.tick(fps)





class Player(GameSprite):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, groups=[]):
        super().__init__(x, y, image, width, height, groups)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.OnGround = True
        self.go = False
        self.Frame = 0
        self.Left = False
        self.Right = True
        self.Jump = False
        self.Attack = False
        self.attack_timer = 0
        self.Cling = False
        self.climbing = False  # Додаємо окрему змінну для лазіння
        self.attack_hitbox = None  # Хітбокс для атаки
        self.Tichka = False
        self.max_health = 100  # Максимальне здоров'я
        self.health = self.max_health 
        self.Dead = False
        self.last_damage_time = 0
        self.bars = [f'vizyal/buttons/bars/bar{i+1}.png' for i in range(9,0,-1)]
        self.attack_damage = 10
        
    def update(self, ground_level, walls, enemys):
        Perssonel = ['run1.png', 'run2.png', 'run3.png', 'run4.png', 'run5.png', 'run6.png', 'run7.png', 'run8.png', 'run9.png', 'run10.png']
        Stand = ['idle1.png', 'idle2.png', 'idle3.png', 'idle4.png', 'idle5.png', 'idle6.png', 'idle7.png', 'idle8.png', 'idle9.png', 'idle10.png']
        jump = ['jump1.png', 'jump2.png', 'jump3.png']
        attack = ['attack1.png', 'attack2.png', 'attack3.png', 'attack4.png']
        cling = ['climb.png']
        tichka = ['hit1.png','hit1.png','hit1.png']
        dead = ['dead1.png','dead2.png','dead3.png','dead4.png','dead5.png','dead6.png','dead7.png','dead8.png','dead9.png','dead10.png']
        bars = ['bar1.png','bar2.png','bar3.png','bar4.png','bar5.png','bar6.png','bar7.png','bar8.png','bar9.png']

        file = 'right' if self.Right else 'left'

        if self.Dead:
            if self.Frame < len(dead) - 1:  
                self.Frame += 0.2
            else:
                self.Frame = len(dead) - 1

            self.image = pygame.image.load(f'vizyal/pers/{file}/{dead[int(self.Frame)]}')
            self.rect = self.image.get_rect(center=self.rect.center)
            self.dx = 0

            self.dy = 9 
            self.rect.y += self.dy

            if self.rect.bottom >= ground_level:
                self.rect.bottom = ground_level
                self.dy = 0
                self.OnGround = True

            return



        if not self.Attack:
            self.rect.x += self.dx

        self.rect.y += self.dy

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > 10000:
            self.rect.right = 10000

        self.climbing = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if (self.dx > 0 and self.Right) or (self.dx < 0 and self.Left):
                    self.climbing = True
                    self.dx = 0

        if not self.OnGround:
            self.rect.y += self.dy
            self.OnGround = False

            if self.rect.y >= ground_level:
                self.rect.y = ground_level
                self.dy = 0
                self.OnGround = True
                self.Jump = False


        if self.Tichka: 
            self.Frame += 0.2
            if self.Frame >= len(tichka):
                self.Frame = 0

            self.tichka_timer -= 1

            if self.tichka_timer <= 0:
                self.Tichka = False
                self.tichka_timer = 0
                self.Frame = 0

            self.image = pygame.image.load(f'vizyal/pers/{file}/{tichka[int(self.Frame)]}')

            hp_index = max(0, min(self.health // 10, len(bars) - 1))  
            self.hp_image = pygame.image.load(f'vizyal/buttons/bars/{bars[int(hp_index)]}')

        elif self.climbing:
            self.Frame += 0.2
            if self.Frame >= len(cling):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/pers/{file}/{cling[int(self.Frame)]}')




        elif self.Attack:
            if self.attack_timer == 0:
                self.attack_timer = 15

            self.Frame += 0.2
            if self.Frame >= len(attack):
                self.Frame = 0
                self.Attack = False

            self.image = pygame.image.load(f'vizyal/pers/{file}/{attack[int(self.Frame)]}')

            if self.Right:
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)
            else:
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)

            # Перевіряємо колізію хітбоксу атаки з ворогами
            for enemy in enemys:
                if self.attack_hitbox.colliderect(enemy.rect):
                    enemy.take_damage(self.attack_damage, enemys)  # Наносимо урон ворогу

            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.Attack = False
                self.attack_hitbox = None

        elif self.Jump:
            self.Frame += 0.2
            if self.Frame >= len(jump):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/pers/{file}/{jump[int(self.Frame)]}')
        
        elif self.Dead:
            if self.Frame < len(dead) - 1:  # Прокручуємо анімацію до останнього кадру
                self.Frame += 0.2
            else:
                self.Frame = len(dead) - 1  # Залишаємо на останньому кадрі і не обнуляємо його більше
            self.image = pygame.image.load(f'vizyal/pers/{file}/{dead[int(self.Frame)]}')
            self.dx = 0  # Персонаж не рухається
            self.dy = 0



        elif self.go:
            self.Frame += 0.2
            if self.Frame >= len(Perssonel):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/pers/{file}/{Perssonel[int(self.Frame)]}')

        else:
            self.Frame += 0.2
            if self.Frame >= len(Stand):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/pers/{file}/{Stand[int(self.Frame)]}')

        self.dx = 0

    

    def take_damage(self, damage, healthbar):
        current_time = time.time()
        if current_time - self.last_damage_time >= 2:
            self.health -= damage
            if self.health < 0:
                self.health = 0
            self.Tichka = True
            self.tichka_timer = 15
            self.last_damage_time = current_time 
        
            hearts_count = len(self.bars)
            hp_index = max(0, min(self.health // 10, hearts_count - 1))
            healthbar.image = pygame.image.load(self.bars[hp_index])


    def death(self):
        self.health -= 10
        if self.health <= 0:
            self.health = 0
            self.Attack = False
            self.climbing = False
            self.go = False
            self.Jump = False
            self.Tichka = False
            self.Dead = True
            self.dx = 0  # Зупиняємо рух тільки після смерті
            self.dy = 0



    def draw(self, surface, camera_offset=pygame.Vector2(0, 0)):
        # Відображаємо персонажа
        if self.Left and self.Attack:
            # Якщо персонаж атакує ліворуч, зміщуємо зображення вліво на ширину хітбоксу (130 пікселів)
            surface.blit(self.image, (self.rect.x + camera_offset.x - 130, self.rect.y + camera_offset.y))
        else:
            # В інших випадках відображаємо звичайно
            surface.blit(self.image, (self.rect.x + camera_offset.x, self.rect.y + camera_offset.y))

        # Відображаємо хітбокс персонажа
        adjusted_player_hitbox = self.rect.move(camera_offset)
        pygame.draw.rect(surface, (255, 0, 0), adjusted_player_hitbox, 2)  # Червоний колір для хітбоксу персонажа

        # Відображаємо хітбокс атаки
        if self.attack_hitbox:
            adjusted_hitbox = self.attack_hitbox.move(camera_offset)
            pygame.draw.rect(surface, (0, 255, 0), adjusted_hitbox, 2)  # Зелений колір для хітбоксу атаки
        

class Enemy(GameSprite):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, monster, groups=[]):
        super().__init__(x, y, image, width, height, groups)
        self.max_health = 100  # Максимальне здоров'я
        self.health = self.max_health  # Поточне здоров'я
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.go = True
        self.Frame = 0
        self.Left = True
        self.Right = False
        self.Attack = False
        self.attack_timer = 0
        self.unit_speed = 2
        self.side = 'left'
        self.patrol_left = patrol_left  
        self.patrol_right = patrol_right
        self.detection_hitbox = pygame.Rect(0, 0, 500, 400)  
        self.detection_hitbox.center = self.rect.center  
        self.detection_hitbox.y += 20  
        self.initial_y = y   #
        self.target_y = y   
        self.damage = 10
        self.Dead = False
        self.speed_y = 1
        self.attack_hitbox = None
        self.monster = monster
        self.max_health = 350  
        self.health = self.max_health
        self.death_timer = 0
        self.OnGround = True
        self.fly = False

    def update(self, hero, ground_level, enemys):
        self.detection_hitbox.centerx = self.rect.centerx
        self.detection_hitbox.y = self.rect.centery  - 100

        if self.detection_hitbox.colliderect(hero.rect):
            if hero.rect.centerx < self.rect.centerx:
                self.side = 'left'
            else:
                self.side = 'right'

            self.target_y = hero.rect.centery
        else:
            self.target_y = self.initial_y

            if self.rect.x <= self.patrol_left:
                self.side = 'right'
            elif self.rect.x >= self.patrol_right:
                self.side = 'left'
        
        if self.side == 'left':
            self.rect.x -= self.unit_speed
            self.Left = True
            self.Right = False
        else: 
            self.rect.x += self.unit_speed
            self.Right = True
            self.Left = False

        if self.rect.centery < self.target_y:
            self.rect.y += self.speed_y
        elif self.rect.centery > self.target_y:
            self.rect.y -= self.speed_y

        if self.rect.colliderect(hero.rect):
            self.Attack = True

            if self.side == 'right':
                self.rect.x -= self.unit_speed  # Відсуваємо ворога праворуч
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)

            else:
                self.rect.x += self.unit_speed  # Відсуваємо ворога ліворуч
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)
                
        if self.rect.bottom >= ground_level:
                self.rect.bottom = ground_level
                self.dy = 0
                self.OnGround = True

                return
            
       

        if self.Attack:
            if self.attack_timer == 0:
                self.attack_timer = 5
            
        if self.Dead:
            self.death_timer -= 1
            if self.death_timer <= 0:  
                if self in enemys:
                    enemys.remove(self)  
            return

    def take_damage(self, damage, enemys):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            self.death(enemys)

    def draw_health_bar(self, surface, camera_offset):
        # Розміри хелсбара
        health_bar_width = 50
        health_bar_height = 5
        health_bar_x = self.rect.x + camera_offset.x + (self.rect.width - health_bar_width) // 2
        health_bar_y = self.rect.y + camera_offset.y - 10  # Хелсбар трохи вище ворога

        # Фон хелсбара (червоний)
        pygame.draw.rect(surface, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        current_health_width = max(0, (self.health / self.max_health) * health_bar_width)
        pygame.draw.rect(surface, (0, 255, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))
    

    def death(self, enemys):
        self.health = 0
        self.Attack = False
        self.Dead = True
        self.attack_hitbox = None  # Додаємо цю строку
        self.dx = 0
        self.dy = 0
        self.death_timer = 25

    

    def draw(self, surface, camera_offset=pygame.Vector2(0, 0)):
        super().draw(surface, camera_offset)
        adjusted_detection_hitbox = self.detection_hitbox.move(camera_offset)
        pygame.draw.rect(surface, (0, 255, 0), adjusted_detection_hitbox, 2)
        
        self.draw_health_bar(surface, camera_offset)
            

class Enemy1(Enemy):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, monster, groups=[]):
        super().__init__(x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, monster, groups)

    def update(self, hero, enemys):
        monster1 = ['idle0.png', 'idle1.png', 'idle2.png', 'idle3.png', 'idle4.png', 'idle5.png', 'idle6.png', 'idle7.png', 'idle8.png', 'idle9.png', 'idle10.png', 'idle11.png', 'idle12.png', 'idle13.png', 'idle14.png', 'idle15.png', 'idle16.png', 'idle17.png']
        flying = ['fly0.png', 'fly1.png', 'fly2.png', 'fly3.png', 'fly4.png', 'fly5.png', 'fly6.png', 'fly7.png', 'fly8.png', 'fly9.png', 'fly10.png', 'fly11.png', 'fly12.png', 'fly13.png', 'fly14.png', 'fly15.png', 'fly16.png', 'fly17.png']
        attack = ['attack0.png', 'attack1.png', 'attack2.png', 'attack3.png', 'attack4.png', 'attack5.png', 'attack6.png', 'attack7.png', 'attack8.png', 'attack9.png', 'attack10.png', 'attack11.png', 'attack12.png', 'attack13.png', 'attack14.png', 'attack15.png', 'attack16.png', 'attack17.png']
        dead = ['dying0.png', 'dying1.png', 'dying2.png', 'dying3.png', 'dying4.png', 'dying5.png', 'dying6.png', 'dying7.png', 'dying8.png', 'dying9.png', 'dying10.png', 'dying11.png', 'dying12.png', 'dying13.png', 'dying14.png', 'dying15.png', 'dying16.png', 'dying17.png']

        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        
        if self.Dead:
            self.Frame += 0.5
            if self.Frame >= len(dead):
                self.Frame = 0
                self.Dead = True 
            self.image = pygame.image.load(f'vizyal/monstersles/{self.monster}/{file}/{dead[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        elif self.Attack:
            self.Frame += 0.5
            if self.Frame >= len(attack):
                self.Frame = 0
                self.Attack = False 
            self.image = pygame.image.load(f'vizyal/monstersles/{self.monster}/{file}/{attack[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

            if self.Right:
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)
            else:
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)

        elif self.go:
            self.Frame += 1
            if self.Frame >= len(flying):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/monstersles/{self.monster}/{file}/{flying[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        else:
            self.Frame += 0.5
            if self.Frame >= len(monster1):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/monstersles/{self.monster}/{file}/{monster1[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        super().update(hero, enemys)


class Enemy2(Enemy):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups=[]):
        super().__init__(x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups)

    def update(self, hero):
        flying = ['fly0.png', 'fly1.png', 'fly2.png', 'fly3.png', 'fly4.png', 'fly5.png', 'fly6.png', 'fly7.png', 'fly8.png', 'fly9.png', 'fly10.png', 'fly11.png', 'fly12.png', 'fly13.png', 'fly14.png', 'fly15.png', 'fly16.png', 'fly17.png']
        attack = ['attack0.png', 'attack1.png', 'attack2.png', 'attack3.png', 'attack4.png', 'attack5.png', 'attack6.png', 'attack7.png', 'attack8.png', 'attack9.png', 'attack10.png', 'attack11.png', 'attack12.png', 'attack13.png', 'attack14.png', 'attack15.png', 'attack16.png', 'attack17.png']
        dead = ['dying0.png', 'dying1.png', 'dying2.png', 'dying3.png', 'dying4.png', 'dying5.png', 'dying6.png', 'dying7.png', 'dying8.png', 'dying9.png', 'dying10.png', 'dying11.png', 'dying12.png', 'dying13.png', 'dying14.png', 'dying15.png', 'dying16.png', 'dying17.png']

        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        
        if self.Dead:
            self.Frame += 0.5
            if self.Frame >= len(dead):
                self.Frame = 0
                self.Dead = True 
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{dead[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        elif self.Attack:
            self.Frame += 0.5
            if self.Frame >= len(attack):
                self.Frame = 0
                self.Attack = False 
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{attack[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

            if self.Right:
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)
            else:
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)

        elif self.go:
            self.Frame += 1
            if self.Frame >= len(flying):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{flying[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        super().update(hero)

class Enemy3(Enemy):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups=[]):
        super().__init__(x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups)

    def update(self, hero):
        attack = ['attack1.png', 'attack2.png', 'attack3.png', 'attack4.png', 'attack5.png', 'attack6.png', 'attack7.png', 'attack8.png', 'attack9.png', 'attack10.png', 'attack11.png', 'attack12.png', 'attack13.png']
        dead = ['dead1.png','dead2.png','dead3.png','dead4.png','dead5.png','dead6.png','dead7.png','dead8.png','dead9.png','dead10.png','dead11.png','dead12.png','dead13.png','dead14.png','dead15.png','dead16.png']
        flying = ['walk1.png','walk2.png','walk3.png','walk4.png','walk5.png','walk6.png','walk7.png','walk8.png']
        
        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        
        if self.Dead:
            self.Frame += 0.5
            if self.Frame >= len(dead):
                self.Frame = 0
                self.Dead = True 
            self.image = pygame.image.load(f'vizyal/monstersles/miniboss/{file}/{dead[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        elif self.Attack:
            self.Frame += 0.5
            if self.Frame >= len(attack):
                self.Frame = 0
                self.Attack = False 
            self.image = pygame.image.load(f'vizyal/monstersles/miniboss/{file}/{attack[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

            if self.Right:
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)
            else:
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)

        elif self.go:
            self.Frame += 1
            if self.Frame >= len(flying):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/monstersles/miniboss/{file}/{flying[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        super().update(hero)

class Enemy4(Enemy):
    def __init__(self, x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups=[]):
        super().__init__(x, y, image, file, width, height, speed_x, speed_y, patrol_left, patrol_right, groups)

    def update(self, hero):
        flying = ['walking0.png', 'wallking1.png', 'wallking2.png', 'wallking3.png', 'wallking4.png', 'wallking5.png', 'wallking6.png', 'wallking.png', 'wallking8.png', 'wallking9.png', 'wallking10.png', 'wallking11.png', 'wallking12.png', 'wallking13.png', 'wallking14.png', 'wallking15.png', 'wallking16.png', 'wallking17.png']
        attack = ['attack0.png', 'attack1.png', 'attack2.png', 'attack3.png', 'attack4.png', 'attack5.png', 'attack6.png', 'attack7.png', 'attack8.png', 'attack9.png', 'attack10.png', 'attack11.png', 'attack12.png', 'attack13.png', 'attack14.png', 'attack15.png', 'attack16.png', 'attack17.png']
        dead = ['dying0.png', 'dying1.png', 'dying2.png', 'dying3.png', 'dying4.png', 'dying5.png', 'dying6.png', 'dying7.png', 'dying8.png', 'dying9.png', 'dying10.png', 'dying11.png', 'dying12.png', 'dying13.png', 'dying14.png', 'dying15.png', 'dying16.png', 'dying17.png']

        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        
        if self.Dead:
            self.Frame += 0.5
            if self.Frame >= len(dead):
                self.Frame = 0
                self.Dead = True 
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{dead[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        elif self.Attack:
            self.Frame += 0.5
            if self.Frame >= len(attack):
                self.Frame = 0
                self.Attack = False 
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{attack[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

            if self.Right:
                self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y, 130, self.rect.height)
            else:
                self.attack_hitbox = pygame.Rect(self.rect.left - 130, self.rect.y, 130, self.rect.height)

        elif self.go:
            self.Frame += 1
            if self.Frame >= len(flying):
                self.Frame = 0
            self.image = pygame.image.load(f'vizyal/monstersles/Monster_5/{file}/{flying[int(self.Frame)]}')
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        super().update(hero)


    
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Saint Blade")
clock = pygame.time.Clock()
fps = 60

def menu():
    end = False
    game_over = False

    #фон логично
    backfon = GameSprite(0, 0, "vizyal/texture/oak_woods_v1.0/background/fon2.png", window.get_width(), window.get_height())
    backfon2 = GameSprite(-6, 15, "vizyal/buttons/GameMenu/1x/fon1.png", window.get_width(), window.get_height())

    #newgame = pygame.image.load("vizyal/buttons/GameMenu/1x/newgame.png")

    # тут краще вказати що це у нас кнопки, тому добавимо приставку _button
    newgame_button = GameSprite(375, 110,"vizyal/buttons/GameMenu/1x/newgame.png",250,50)
    settings_button = GameSprite(388, 300,"vizyal/buttons/GameMenu/1x/setting.png",200,65)
    quit_button = GameSprite(350, 400,"vizyal/buttons/GameMenu/1x/quit.png",285,65)

    finish = False
    while not end:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if newgame_button.is_clicked(mouse_pos):
                    start_new_game()
                elif settings_button.is_clicked(mouse_pos):
                    open_settings()
                elif quit_button.is_clicked(mouse_pos):
                    quit_game()

                
            if not finish:
                backfon.draw(window)
                backfon2.draw(window)
                newgame_button.draw(window)
                settings_button.draw(window)
                quit_button.draw(window)
    
        pygame.display.update()
        
        clock.tick(fps)

menu()
