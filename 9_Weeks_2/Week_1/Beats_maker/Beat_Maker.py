import pygame
from pygame import mixer
pygame.init()

# Define all needed colors and sizes
Width = 1400
Height = 800
black = (0, 0, 0)
light_grey = (170, 170, 170)
white = (255, 255, 255)
grey = (128, 128, 128)
dark_grey = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

# Creats Background and Defines Fonts
screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 24)

#Defines all active variables
index = 100
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 8
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_list =[1 for _ in range(instruments)]
bpm = 138
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
beat_name = ''
typing = False

#Defines soundes needed
Riff1 = mixer.Sound('9_Weeks_2\Week_1\sounds\\New Love Buzz Riff 1.WAV')
Riff2 = mixer.Sound('9_Weeks_2\Week_1\sounds\\New Love Buzz Riff 2.wav')
Drums1 = mixer.Sound('9_Weeks_2\Week_1\sounds\\New Love Buzz Drums.wav')
Drums2 = mixer.Sound('9_Weeks_2\Week_1\sounds\\New Love Buzz Drum 2.wav')
Vocal = mixer.Sound('9_Weeks_2\Week_1\sounds\Love Buzz Bass.wav')
Bass1 = mixer.Sound('9_Weeks_2\Week_1\sounds\\New Love Buzz Bass.wav')
Bass2 = mixer.Sound('9_Weeks_2\Week_1\sounds\Love Buzz Bass.wav')


pygame.mixer.set_num_channels(instruments * 3)

#Function That tells the Audio to play when a square is labeled active
def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                Riff1.play()
            if i == 1:
                Riff2.set_volume(.35)
                Riff2.play()
            if i == 2:
                Drums1.play()
            if i == 3:
                Drums2.play()
            if i == 4:
                Vocal.play()
            if i == 6:
                Bass1.play()
            if i == 7:
                Bass2.play()

#Draws the UI
def draw_grid(clicks, beat, actives):
    left_box = pygame.draw.rect(screen, grey, [0, 0, 200, Height - 200], 5)
    bottom_box = pygame.draw.rect(screen, grey, [0, Height - 200, Width, 200], 5)
    boxes = []
    colors = [grey, white, grey]
    Riff_1_text = label_font.render('Riff', True, colors[actives[0]])
    screen.blit(Riff_1_text, (30, 25))
    Riff_2_text = label_font.render('Riff 2', True, colors[actives[1]])
    screen.blit(Riff_2_text, (30, 100))
    Drum_1_text = label_font.render('Drums', True, colors[actives[2]])
    screen.blit(Drum_1_text, (30, 175))
    Drum_2_text = label_font.render('Drums 2', True, colors[actives[3]])
    screen.blit(Drum_2_text, (30, 250))
    Vocal_1_text = label_font.render('Vocal 1', True, colors[actives[4]])
    screen.blit(Vocal_1_text, (30, 325))
    Vocal_2_text = label_font.render('Vocal 2', True, colors[actives[5]])
    screen.blit(Vocal_2_text, (30, 400))
    Bass_1_text = label_font.render('Bass', True, colors[actives[6]])
    screen.blit(Bass_1_text, (30, 475))
    Bass_2_text = label_font.render('Bass 2', True, colors[actives[7]])
    screen.blit(Bass_2_text, (30, 550))
    for i in range(instruments):
        pygame.draw.line(screen, grey, (0, (i * 75) + 75), (200, (i * 75) + 75), 3)
    
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = grey
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = dark_grey
            rect = pygame.draw.rect(screen, color, [i * ((Width - 200) // beats) + 205, (j * 75) + 5, ((Width - 200) // beats) - 10, ((Height - 200) // instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold, [i * ((Width - 200) // beats) + 200, (j * 75), ((Width - 200) // beats), ((Height - 200) // instruments)], 5, 5)

            pygame.draw.rect(screen, black, [i * ((Width - 200) // beats) + 200, (j * 75), ((Width - 200) // beats), ((Height - 200) // instruments)], 2, 5)
            
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((Width - 200)//beats) + 200, 0, ((Width - 200)//beats), instruments * 75], 5, 3)
    return boxes

#Draws the UI screen
def draw_save_menu(beat_name, typing):
    pygame.draw.rect(screen, black, [0, 0, Width, Height])
    menu_text = label_font.render('SAVE MENU: Enter a Name for Current Beat!', True, white)
    saving_btn = pygame.draw.rect(screen, grey, [Width // 2 - 200, Height * 0.75, 400, 100], 0, 5)
    saving_txt = label_font.render("Save Beat", True, white)
    screen.blit(saving_txt, (Width // 2 - 70, Height * 0.75 + 30))
    screen.blit(menu_text, (400, 40))
    exit_btn = pygame.draw.rect(screen, grey, [Width - 200, Height - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (Width - 160, Height - 70))
    if typing:
        pygame.draw.rect(screen, dark_grey, [400, 200, 600, 200], 0, 5)
    entry_rect = pygame.draw.rect(screen, grey, [400, 200, 600, 200], 5, 5)
    entry_text = label_font.render(f"{beat_name}", True, white)
    screen.blit(entry_text, (430, 250))
    return exit_btn, saving_btn, entry_rect

#Draws Loading Screen and Loads in by slicing up Strings from saved_beats.txt to find bpm, clicked blocks, beats, etc.
def draw_load_menu(index):
    loaded_clicked = []
    loaded_beats = 0
    loaded_bpm = 0
    pygame.draw.rect(screen, black, [0, 0, Width, Height])
    menu_text = label_font.render('LOAD MENU: Select a beat to Load in!', True, white)
    loading_btn = pygame.draw.rect(screen, grey, [Width // 2 - 200, Height * 0.87, 400, 100], 0, 5)
    loading_txt = label_font.render("Load Beat", True, white)
    screen.blit(loading_txt, (Width // 2 - 70, Height * 0.87 + 30))
    delete_btn = pygame.draw.rect(screen, grey, [(Width // 2) - 500, Height * 0.87, 200, 100], 0, 5)
    delete_text = label_font.render("Delete Beat", True, white)
    screen.blit(delete_text, ((Width // 2) - 495, Height * 0.87 + 30))
    screen.blit(menu_text, (400, 40))
    exit_btn = pygame.draw.rect(screen, grey, [Width - 200, Height - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (Width - 160, Height - 70))
    loaded_rectangle = pygame.draw.rect(screen, grey, [190, 90, 1000, 600], 5, 5)
    if 0 <= index < len(saved_beats):
        pygame.draw.rect(screen, light_grey, [190, 100 + index * 50, 1000, 50])
    for beat in range(len(saved_beats)):
        if beat < 10:
            beat_clicked = []
            row_text = medium_font.render(f"{beat + 1}", True, white)
            screen.blit(row_text, (200, 100 + beat * 50))
            name_index_start = saved_beats[beat].index("name: ") + 6
            name_index_end = saved_beats[beat].index(', beats:')
            name_text = medium_font.render(saved_beats[beat][name_index_start:name_index_end], True, white)
            screen.blit(name_text, (240, 100 + beat * 50))
        if 0 <= index < len(saved_beats) and beat == index:
            beat_index_end = saved_beats[beat].index(", bpm")
            loaded_beats = int(saved_beats[beat][name_index_end + 8: beat_index_end])
            bpm_index_end = saved_beats[beat].index(', selected')
            loaded_bpm = int(saved_beats[beat][beat_index_end + 6: bpm_index_end])
            loaded_clicks_string = saved_beats[beat][bpm_index_end + 14: -3]
            loaded_clicks_rows = list(loaded_clicks_string.split('], ['))
            for row in range(len(loaded_clicks_rows)):
                loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == "1" or loaded_clicks_row[item] == "-1":
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
                beat_clicked.append(loaded_clicks_row)
                loaded_clicked = beat_clicked
    loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]
    return exit_btn, loading_btn, delete_btn, loaded_rectangle, loaded_info



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_list)

    play_pause = pygame.draw.rect(screen, grey, [50, Height - 150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, Height - 130))

# Draws Play/Pause Button
    if playing:
        play_text2 = medium_font.render('Playing', True, dark_grey)
    else:
        play_text2 = medium_font.render('Paused', True, dark_grey)
    screen.blit(play_text2, (70, Height - 100))

# Draws Bpm info and draws +5 and -5 Bpm buttons
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

# Draws Beat info and draws +1 and -1 Beat buttons
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
        rect = pygame.rect.Rect((0, i * 75), (170, 50))
        instrument_rects.append(rect)
# Draws Save buttons and Load Button
    save_button = pygame.draw.rect(screen, grey, (900, Height - 150, 200, 48), 0, 5)
    save_text = label_font.render('Save Beat', True, white)
    screen.blit(save_text, (920, Height - 140))
    load_button = pygame.draw.rect(screen, grey, (900, Height - 100, 200, 48), 0, 5)
    load_text = label_font.render('Load Beat', True, white)
    screen.blit(load_text, (920, Height - 90))

    clear_button = pygame.draw.rect(screen, grey, (1150, Height - 150, 200, 100), 0, 5)
    clear_text = label_font.render('Clear Board', True, white)
    screen.blit(clear_text, (1155,  Height - 120))

# If save or load screens are active, pull values from their respective functions
    if save_menu:
        exit_button, saving_button, entry_rectangle = draw_save_menu(beat_name, typing)
    if load_menu:
        exit_button, loading_button, delete_button, loaded_rectangle, loaded_info = draw_load_menu(index)

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
# If the mouse clicks the play pause button without the save or laod menu being up, # it'll pause, if its not playing, it'll un pause
        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
# If you hit the +5 or -5 buttons, the bpm will increase or decrease by 5
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
# If you hit the +1 or -1 buttons, the beats will increase or decrease by 1
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
# if you hit the clear button, all active buttons will unactivate
            elif clear_button.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
# if you hit the "Save Beat" button, the program determines that its open
            elif save_button.collidepoint(event.pos):
                save_menu = True
# if you hit the "Load Beat" button, the program determines that its open
            elif load_button.collidepoint(event.pos):
                load_menu = True
# if you click on an instruments rectangle it wil deactivate all of its active notes
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1
# if you hit the exit button, the current menu will close
        elif event.type == pygame.MOUSEBUTTONUP:
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True
                beat_name = ''
                typing - False
# if hit a in the load menu song, the loaded rectangle highlights it 
# if you hit the delete button while the beats highlighted, the string is poped frome saved_beats.
#  If you hit the load button while the beats highlighted, the current values are overwritten
            if load_menu:
                if loaded_rectangle.collidepoint(event.pos):
                    index = (event.pos[1] - 100) // 50
                if delete_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        saved_beats.pop(index)
                if loading_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        beats = loaded_info[0]
                        bpm = loaded_info[1]
                        clicked = loaded_info[2]
                        index = 100
                        load_menu = False
# If you click on the entry prompt in the save menu, the box highlights to show its selected 
# If the box is highlighted, the program sets typing to true
# If you click save after typing, the program opens the saved beats file ans writes down all the data into a string
            if save_menu:
                if entry_rectangle.collidepoint(event.pos):
                    if typing:
                        typing = False
                    elif not typing:
                        typing = True
                if saving_button.collidepoint(event.pos):
                    file = open('9_Weeks_2\Week_1\Beats_maker\saved_beats.txt', 'w')
                    saved_beats.append(f'\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for i in range(len(saved_beats)):
                        file.write(str(saved_beats[i]))
                        file.close
                        save_menu = False
                        typing = False
                        beat_name = ''
# If you input text into the box, the beat name is what you put down
# If you hit backspace, The beatname will only save/ display everything after the backspace
        if event.type == pygame.TEXTINPUT and typing:
            beat_name += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0 and typing:
                beat_name = beat_name[:-1]

    beat_length = 3600 // bpm

# If the active length is less than beat length while its playing, active length increases by 1
# If active is is equal to or greater than beat length, active length is set to 0
# if active length is then less than beats - 1, 1 is added active length and beat_changed is equal to true
# if active length is less than beat length and beats, its set to 0 and beat changed is equal to true
# This moves the blue player rectangle across the notes
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