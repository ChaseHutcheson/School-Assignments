import pygame 
from pygame import mixer
pygame.init()

Width = 1400
Height = 800
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)


screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 8
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True

hi_hat = mixer.Sound('9_Weeks_2\Week_1\sounds\hi hat.WAV')
snare = mixer.Sound('9_Weeks_2\Week_1\sounds\snare.WAV')
kick = mixer.Sound('9_Weeks_2\Week_1\sounds\kick.WAV')
crash = mixer.Sound('9_Weeks_2\Week_1\sounds\crash.wav')
clap = mixer.Sound('9_Weeks_2\Week_1\sounds\clap.wav')
tom = mixer.Sound('9_Weeks_2\Week_1\sounds\\tom.WAV')
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
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



def draw_grid(clicks, beat):
    left_box = pygame.draw.rect(screen, grey, [0, 0, 200, Height - 200], 5)
    bottom_box = pygame.draw.rect(screen, grey, [0, Height - 200, Width, 200], 5)
    boxes = []
    colors = [grey, white, grey]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 230))
    Crash_text = label_font.render('Crash', True, white)
    screen.blit(Crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, grey, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
    
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = grey
            else:
                color = green
            rect = pygame.draw.rect(screen, color, [i * ((Width - 200) // beats) + 205, (j * 100) + 5, ((Width - 200) // beats) - 10, (Height // instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold, [i * ((Width - 200) // beats) + 200, (j * 100), ((Width - 200) // beats), (Height // instruments)], 5, 5)

            pygame.draw.rect(screen, black, [i * ((Width - 200) // beats) + 200, (j * 100), ((Width - 200) // beats), (Height // instruments)], 2, 5)
            
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((Width - 200)//beats) + 200, 0, ((Width - 200)//beats), instruments * 100], 5, 3)
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)

    play_pause = pygame.draw.rect(screen, grey, [50, Height - 150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text(70, Height-130))

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

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