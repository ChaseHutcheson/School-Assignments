import pygame
from pygame import mixer
pygame.init()

Width = 1400
Height = 800
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
dark_grey = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)


screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 24)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_list =[1 for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True
save_menu = False
load_menu = False
saved_beats = []
file = open('9_Weeks_2\Week_1\Beats_maker\saved_beats.txt', 'r')
for line in file:
    saved_beats.append(line)


hi_hat = mixer.Sound('9_Weeks_2\Week_1\sounds\hi hat.WAV')
snare = mixer.Sound('9_Weeks_2\Week_1\sounds\snare.WAV')
kick = mixer.Sound('9_Weeks_2\Week_1\sounds\kick.WAV')
crash = mixer.Sound('9_Weeks_2\Week_1\sounds\crash.wav')
clap = mixer.Sound('9_Weeks_2\Week_1\sounds\clap.wav')
tom = mixer.Sound('9_Weeks_2\Week_1\sounds\\tom.WAV')
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()



def draw_grid(clicks, beat, actives):
    left_box = pygame.draw.rect(screen, grey, [0, 0, 200, Height - 200], 5)
    bottom_box = pygame.draw.rect(screen, grey, [0, Height - 200, Width, 200], 5)
    boxes = []
    colors = [grey, white, grey]
    hi_hat_text = label_font.render('Hi Hat', True, colors[actives[0]])
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, colors[actives[1]])
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Bass Drum', True, colors[actives[2]])
    screen.blit(kick_text, (17, 230))
    Crash_text = label_font.render('Crash', True, colors[actives[3]])
    screen.blit(Crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, colors[actives[4]])
    screen.blit(clap_text, (30, 430))
    floor_text = label_font.render('Floor Tom', True, colors[actives[5]])
    screen.blit(floor_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, grey, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
    
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = grey
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = dark_grey
            rect = pygame.draw.rect(screen, color, [i * ((Width - 200) // beats) + 205, (j * 100) + 5, ((Width - 200) // beats) - 10, ((Height - 200) // instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold, [i * ((Width - 200) // beats) + 200, (j * 100), ((Width - 200) // beats), ((Height - 200) // instruments)], 5, 5)

            pygame.draw.rect(screen, black, [i * ((Width - 200) // beats) + 200, (j * 100), ((Width - 200) // beats), ((Height - 200) // instruments)], 2, 5)
            
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((Width - 200)//beats) + 200, 0, ((Width - 200)//beats), instruments * 100], 5, 3)
    return boxes


def draw_save_menu():
    pygame.draw.rect(screen, black, [0, 0, Width, Height])
    exit_btn = pygame.draw.rect(screen, grey, [Width - 200, Height - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (Width - 160, Height - 70))
    return exit_btn


def draw_load_menu():

    exit_btn = pygame.draw.rect(screen, grey, [Width - 200, Height - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (Width - 160, Height - 70))
    return exit_btn



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_list)

    play_pause = pygame.draw.rect(screen, grey, [50, Height - 150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, Height - 130))

    if playing:
        play_text2 = medium_font.render('Playing', True, dark_grey)
    else:
        play_text2 = medium_font.render('Paused', True, dark_grey)
    screen.blit(play_text2, (70, Height - 100))

    bpm_rect = pygame.draw.rect(screen, grey, [300, Height - 150, 220, 100], 5, 5)
    bpm_text = medium_font.render("Beats Per Minute", True, white)
    screen.blit(bpm_text, (308, Height - 130))
    bpm_text2 = label_font.render(f"{bpm}", True, white)
    screen.blit(bpm_text2, (370, Height - 100))
    bpm_add_rect = pygame.draw.rect(screen, grey, [525, Height - 150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, grey, [525, Height - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+5', True, white)
    sub_text = medium_font.render('-5', True, white)
    screen.blit(add_text, [535, Height - 140])
    screen.blit(sub_text, [535, Height - 90])

    beats_rect = pygame.draw.rect(screen, grey, [600, Height - 150, 220, 100], 5, 5)
    beats_text = medium_font.render("Beats in Loop", True, white)
    screen.blit(beats_text, (618, Height - 130))
    beats_text2 = label_font.render(f"{beats}", True, white)
    screen.blit(beats_text2, (680, Height - 100))
    beats_add_rect = pygame.draw.rect(screen, grey, [825, Height - 150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, grey, [825, Height - 100, 48, 48], 0, 5)
    add_text2 = medium_font.render('+1', True, white)
    sub_text2 = medium_font.render('-1', True, white)
    screen.blit(add_text2, [835, Height - 140])
    screen.blit(sub_text2, [835, Height - 90])

    instrument_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instrument_rects.append(rect)

    save_button = pygame.draw.rect(screen, grey, (900, Height - 150, 200, 48), 0, 5)
    save_text = label_font.render('Save Beat', True, white)
    screen.blit(save_text, (920, Height - 140))
    load_button = pygame.draw.rect(screen, grey, (900, Height - 100, 200, 48), 0, 5)
    load_text = label_font.render('Load Beat', True, white)
    screen.blit(load_text, (920, Height - 90))

    clear_button = pygame.draw.rect(screen, grey, (1150, Height - 150, 200, 100), 0, 5)
    clear_text = label_font.render('Clear Board', True, white)
    screen.blit(clear_text, (1155,  Height - 120))

    if save_menu:
        exit_button = draw_save_menu()
    if load_menu:
        exit_button = draw_load_menu()

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clear_button.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
            elif save_button.collidepoint(event.pos):
                save_menu = True
            elif load_button.collidepoint(event.pos):
                load_menu = True
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1
        elif event.type == pygame.MOUSEBUTTONUP:
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True

    beat_length = 3600 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()