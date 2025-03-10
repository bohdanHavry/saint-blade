import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Преследование")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Параметры игрока и врага
player_size = 30
enemy_size = 30
detection_radius = 200

player_x, player_y = 100, 100
enemy_x, enemy_y = 300, 300

speed = 3
enemy_speed = 2

running = True
while running:
    pygame.time.delay(30)  # Задержка для FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение игрока (стрелки)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= speed
    if keys[pygame.K_RIGHT]: player_x += speed
    if keys[pygame.K_UP]: player_y -= speed
    if keys[pygame.K_DOWN]: player_y += speed

    # Проверка расстояния для преследования
    dx, dy = player_x - enemy_x, player_y - enemy_y
    distance = (dx**2 + dy**2) ** 0.5

    if distance < detection_radius:  # Если игрок в зоне
        enemy_x += enemy_speed * (dx / distance)
        enemy_y += enemy_speed * (dy / distance)

    # Отрисовка
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(win, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

    pygame.display.update()

pygame.quit()
