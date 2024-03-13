from random import randint
from sys import exit
import pygame
from random import randint
from sys import exit

clock = pygame.time.Clock()

pygame.init()

game_active = False

start_time = 0

font = pygame.font.Font(None, 50)

replay_text = font.render("Replay", True, (255, 255, 255))
replay_rect = replay_text.get_rect(center=(700, 400))

def displayscore() :
    r_score = (pygame.time.get_ticks() - start_time)//1000
    score_surface = font.render(f"Score : {r_score}", False, 'white')
    score_rect = score_surface.get_rect(center = (700, 50))
    screen.blit(score_surface, score_rect)

def display_start_screen():
    screen.fill((0, 0, 0))
    start_text = font.render("Space Wars", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(700, 300))
    screen.blit(start_text, start_rect)

    play_text = font.render("Play", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(700, 400))
    screen.blit(play_text, play_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return

screen = pygame.display.set_mode((1400,700))

bg_surf = pygame.image.load("./graphics/night.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft = (0,0))


plane_surf = pygame.image.load("./graphics/plane-rbg.png").convert_alpha()
plane_rect = plane_surf.get_rect(midbottom = (700,700))

rock1_surf =  pygame.image.load("./graphics/rock_1.png").convert_alpha()
rock1_rect = rock1_surf.get_rect(midtop = (200,0))

rock2_surf = pygame.image.load("./graphics/rock_2.png").convert_alpha()
rock2_rect = rock2_surf.get_rect(midtop = (500,0))

rock3_surf = pygame.image.load("./graphics/rock_3.png").convert_alpha()
rock3_rect = rock3_surf.get_rect(midtop = (800,0))

rock4_surf = pygame.image.load("./graphics/rock_4.png").convert_alpha()
rock4_rect = rock4_surf.get_rect(midtop = (1100,0))

s1,s2,s3,s4 = 4,4,4,4

display_start_screen()

game_active = True
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if replay_rect.collidepoint(event.pos):
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        mos_pos = pygame.mouse.get_pos()

        screen.blit(bg_surf,bg_rect)
        screen.blit(plane_surf,plane_rect)
        screen.blit(rock1_surf,rock1_rect)
        screen.blit(rock2_surf,rock2_rect)
        screen.blit(rock3_surf,rock3_rect)
        screen.blit(rock4_surf,rock4_rect)

        clock.tick(60)

        rock1_rect.bottom += s1
        rock2_rect.bottom += s2
        rock3_rect.bottom += s3
        rock4_rect.bottom += s4

        if(rock1_rect.top > 700) :
            rock1_rect.center = (randint(100,1300), randint(-400,-100))
            s1 += randint(0,3)

        if(rock2_rect.top > 700) :
            rock2_rect.center = (randint(100,1300), randint(-400,-100))
            s2 += randint(0,3)

        if(rock3_rect.top > 700) :
            rock3_rect.center = (randint(100,1300), randint(-400,-100))
            s3 += randint(0,3)

        if(rock4_rect.top > 700) :
            rock4_rect.center = (randint(100,1300), randint(-400,-100))
            s4 += randint(0,3)

        if(rock1_rect.collidepoint(mos_pos) or rock2_rect.collidepoint(mos_pos) or rock3_rect.collidepoint(mos_pos) or rock4_rect.collidepoint(mos_pos)) :
            game_active = False

        displayscore()

        plane_rect.center = mos_pos
        pygame.display.update()

    else:

        screen.blit(replay_text, replay_rect)

    pygame.display.update()
    clock.tick(60)

    
        
