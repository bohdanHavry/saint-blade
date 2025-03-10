import pygame

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лазание по стенам")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Гравитация и скорость
GRAVITY = 0.5
SPEED = 5
CLIMB_SPEED = 4

# Класс стены
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx, self.dy = 0, 0
        self.on_wall = False

    def update(self, walls):
        keys = pygame.key.get_pressed()
        self.dx = 0
        self.dy += GRAVITY  # Гравитация

        # Движение влево/вправо
        if keys[pygame.K_a]: 
            self.dx = -SPEED
        if keys[pygame.K_d]: 
            self.dx = SPEED

        # Проверка столкновений по горизонтали
        self.rect.x += self.dx
        self.on_wall = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.dx > 0:  # Движение вправо
                    self.rect.right = wall.rect.left
                elif self.dx < 0:  # Движение влево
                    self.rect.left = wall.rect.right
                self.on_wall = True  # Если касаемся стены, включаем возможность лазания

        # Лазание по стене
        if self.on_wall and keys[pygame.K_w]:  
            self.dy = -CLIMB_SPEED  # Движение вверх

        # Проверка столкновений по вертикали
        self.rect.y += self.dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.dy > 0:  # Если падаем вниз
                    self.rect.bottom = wall.rect.top
                    self.dy = 0
                elif self.dy < 0:  # Если двигаемся вверх
                    self.rect.top = wall.rect.bottom
                    self.dy = 0

# Создаем игрока и стены
player = Player(100, HEIGHT - 100)
walls = [Wall(300, 400, 50, 200), Wall(600, 200, 50, 300)]

# Группы спрайтов
all_sprites = pygame.sprite.Group(player, *walls)
wall_group = pygame.sprite.Group(*walls)

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    player.update(wall_group)

    # Отрисовка
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
