import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Hitler vs. Stalin")
clock = pygame.time.Clock()

# Replace paths with your actual file locations
background_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\ww2.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
bird_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\adolf hitler.png").convert_alpha(), (50, 50))
pipe_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\joseph stalin.png").convert_alpha(), (70, 80))
funny_meme = pygame.image.load("C:\\Users\\hp\\Downloads\\funny hitler.jpg").convert_alpha()
funny_meme = pygame.transform.scale(funny_meme, (WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.mixer.music.load("C:\\Users\\hp\\Downloads\\dark is the night.mp3")
game_over_sound = pygame.mixer.Sound("C:\\Users\\hp\\Downloads\\Voicy_hitler.mp3")

score = 0
scored_pipes = set()
font = pygame.font.SysFont(None, 40)

bird_x = 170
bird_y = WINDOW_HEIGHT // 2
bird_movement = 0
gravity = 0.4
flap_power = -10

pipe_speed = 2.5
pipe_gap = 240
pipe_frequency = 1800
pipes = []
last_pipe_time = pygame.time.get_ticks() - pipe_frequency
music_started = False
game_active = False

def create_pipe_pair():
    lower_bound = 100
    upper_bound = WINDOW_HEIGHT - 100 - pipe_gap
    if upper_bound < lower_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
    y_pos = random.randint(lower_bound, upper_bound)
    top_rect = pipe_img.get_rect(midbottom=(WINDOW_WIDTH + 40, y_pos))
    bot_rect = pipe_img.get_rect(midtop=(WINDOW_WIDTH + 40, y_pos + pipe_gap))
    return top_rect, bot_rect

def move_pipes(pipes):
    updated = []
    for top_rect, bot_rect in pipes:
        top_rect.x -= pipe_speed
        bot_rect.x -= pipe_speed
        if top_rect.right > 0:
            updated.append((top_rect, bot_rect))
    return updated

def draw_pipes(pipes):
    for top_rect, bot_rect in pipes:
        window.blit(pygame.transform.flip(pipe_img, False, True), top_rect)
        window.blit(pipe_img, bot_rect)

def check_collision(bird_rect, pipes):
    if bird_rect.top <= 0 or bird_rect.bottom >= WINDOW_HEIGHT:
        return True
    for top_rect, bot_rect in pipes:
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):
            return True
    return False

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not game_active:
                game_active = True
            if event.key == pygame.K_SPACE:
                bird_movement = flap_power
                if not music_started:
                    pygame.mixer.music.play(-1)
                    music_started = True

    if game_active:
        bird_movement += gravity
        bird_y += bird_movement
        bird_rect = pygame.Rect(bird_x, bird_y, 50, 50)

        now = pygame.time.get_ticks()
        if now - last_pipe_time > pipe_frequency:
            pipes.append(create_pipe_pair())
            last_pipe_time = now

        pipes = move_pipes(pipes)

        for top_rect, bot_rect in pipes:
            pipe_id = id(top_rect)
            if pipe_id not in scored_pipes and top_rect.right < bird_x:
                score += 1
                scored_pipes.add(pipe_id)

        if check_collision(bird_rect, pipes):
            pygame.mixer.music.stop()
            game_over_sound.play()
            window.blit(funny_meme, (0, 0))
            pygame.display.update()
            pygame.time.wait(3000)
            game_active = False
            music_started = False
            pipes.clear()
            scored_pipes.clear()
            score = 0
            bird_y = WINDOW_HEIGHT // 2
            bird_movement = 0

        window.blit(background_img, (0, 0))
        draw_pipes(pipes)
        window.blit(pygame.transform.scale(bird_img, (50, 50)), (bird_x, bird_y))
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        window.blit(score_surface, (20, 20))
    else:
        window.fill((0, 0, 0))
        window.blit(background_img, (0, 0))
        title_text = font.render("Press any key to start", True, (255, 255, 255))
        instr_text = font.render("Spacebar to flap", True, (255, 255, 255))
        window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, WINDOW_HEIGHT // 2 - 50))
        window.blit(instr_text, (WINDOW_WIDTH // 2 - instr_text.get_width() // 2, WINDOW_HEIGHT // 2 + 10))

    pygame.display.update()
