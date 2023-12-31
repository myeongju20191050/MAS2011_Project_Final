import pygame
import random
from os import path

sound_dir = path.join(path.dirname(__file__), 'snd')
img_dir = path.join(path.dirname(__file__), 'img')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Projuct Final_20191050_Duck's way to home")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, "grass.png"))

player = pygame.image.load(path.join(img_dir, 'duck.png'))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = (WIDTH - player_width) / 2
player_y_pos = HEIGHT - player_height

to_x = 0
to_y = 0

speed = 0.1

home = pygame.image.load(path.join(img_dir, 'home.png'))
home_size = home.get_rect().size
home_width = home_size[0]
home_height = home_size[1]
home_x_pos = (WIDTH - home_width) / 2
home_y_pos = home_height

enemy1 = pygame.image.load(path.join(img_dir, 'animal1.png'))
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_x_pos = 0
enemy1_y_pos = 400
enemy1_speed = 3

enemy2 = pygame.image.load(path.join(img_dir, 'animal2.png'))
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = 300
enemy2_y_pos = 250
enemy2_speed = 3.5

enemy3 = pygame.image.load(path.join(img_dir, 'animal3.png'))
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_x_pos = WIDTH - enemy3_width
enemy3_y_pos = 350
enemy3_speed = 4

enemy4 = pygame.image.load(path.join(img_dir, 'animal4.png'))
enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_x_pos = 500
enemy4_y_pos = 150
enemy4_speed = 3.5

game_font = pygame.font.Font(None, 40)

total_time = 50000

start_ticks = pygame.time.get_ticks()

pygame.mixer.music.load(path.join(sound_dir, 'bgm.wav'))
pygame.mixer.music.play()
step_sound = pygame.mixer.Sound(path.join(sound_dir, 'step.wav'))
gameover_sound = pygame.mixer.Sound(path.join(sound_dir, 'gameover.wav'))
win_sound = pygame.mixer.Sound(path.join(sound_dir, 'win.wav'))

gameover_font = pygame.font.Font(None, 80)
gameover_text = gameover_font.render('GAME OVER', True, (255, 0, 0))
size_text_width = gameover_text.get_rect().size[0]
size_text_height = gameover_text.get_rect().size[1]
x_pos_gameover = WIDTH/2 - size_text_width/2
y_pos_gameover = HEIGHT/2 - size_text_height/2

win_font = pygame.font.Font(None, 80)
win_text = win_font.render('WIN!', True, (0, 0, 255))
size_text_width = win_text.get_rect().size[0]
size_text_height = win_text.get_rect().size[1]
x_pos_win = WIDTH/2 - size_text_width/2
y_pos_win = HEIGHT/2 - size_text_height/2

timeover_font = pygame.font.Font(None, 80)
timeover_text = timeover_font.render('TIME OVER', True, (255, 255, 0))
size_text_width = timeover_text.get_rect().size[0]
size_text_height = timeover_text.get_rect().size[1]
x_pos_timeover = WIDTH/2 - size_text_width/2
y_pos_timeover = HEIGHT/2 - size_text_height/2

title_font = pygame.font.Font(None, 40)
start_font = pygame.font.Font(None, 20)

def show_text(text, font, screen, x, y):
    textobj = font.render(text, True, WHITE, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def press_space_to_start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            
show_text("Duck's way to home", title_font, screen, WIDTH/2-140, HEIGHT/2-50)
show_text('Press SPACE KEY to start', start_font, screen, WIDTH/2-90, HEIGHT/2+100)

pygame.display.update()
press_space_to_start()


running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                step_sound.play()
                to_x -= speed
            if event.key == pygame.K_RIGHT:
                step_sound.play()
                to_x += speed
            if event.key == pygame.K_UP:
                step_sound.play()
                to_y -= speed
            elif event.key == pygame.K_DOWN:
                step_sound.play()
                to_y += speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    player_x_pos += to_x * dt
    player_y_pos += to_y * dt
    enemy1_x_pos += enemy1_speed
    enemy2_x_pos += enemy2_speed
    enemy3_x_pos -= enemy3_speed
    enemy4_x_pos -= enemy4_speed

    if enemy1_x_pos > WIDTH:
        enemy1_x_pos = 0
        enema1_y_pos = 400

    if enemy2_x_pos > WIDTH:
        enemy2_x_pos = 0
        enema2_y_pos = 250

    if enemy3_x_pos + enemy3_width < 0:
        enemy3_x_pos = WIDTH - enemy3_width
        enema2_y_pos = 350

    if enemy4_x_pos + enemy4_width < 0:
        enemy4_x_pos = WIDTH - enemy4_width
        enema4_y_pos = 150

    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > WIDTH - player_width:
        player_x_pos = WIDTH - player_width
    
    if player_y_pos > 500:
        player_y_pos = 500
    elif player_y_pos < player_height:
        player_y_pos = player_height

    player_rect = player.get_rect()
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos

    home_rect = player.get_rect()
    home_rect.left = home_x_pos
    home_rect.top = home_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_x_pos
    enemy4_rect.top = enemy4_y_pos

    if player_rect.colliderect(enemy1_rect):
        gameover_sound.play()
        background.blit(gameover_text, (x_pos_gameover, y_pos_gameover))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    if player_rect.colliderect(enemy2_rect):
        gameover_sound.play()
        background.blit(gameover_text, (x_pos_gameover, y_pos_gameover))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    if player_rect.colliderect(enemy3_rect):
        gameover_sound.play()
        background.blit(gameover_text, (x_pos_gameover, y_pos_gameover))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    if player_rect.colliderect(enemy4_rect):
        gameover_sound.play()
        background.blit(gameover_text, (x_pos_gameover, y_pos_gameover))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    if player_rect.colliderect(home_rect):
        win_sound.play()
        background.blit(win_text, (x_pos_win, y_pos_win))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(home, (home_x_pos, home_y_pos))
    screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos))
    screen.blit(enemy4, (enemy4_x_pos, enemy4_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks / 1000)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 0, 0))

    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0 :
        gameover_sound.play()
        background.blit(timeover_text, (x_pos_timeover, y_pos_timeover))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    pygame.display.update()

pygame.quit()