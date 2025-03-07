import pygame
import sys
from pygame.locals import *
from Main_menu.button import Button
from PIL import Image

running = True
# pygame.init()
BG = pygame.image.load("Main_menu/resource/Background.png")


TITLE = pygame.image.load("Main_menu/resource/title.png")

Info = pygame.display.Info()
height = Info.current_h
width = Info.current_w
resolution = (width, height)
screen = pygame.display.set_mode(resolution)

BG = pygame.transform.scale(BG, resolution)


TITLE = pygame.transform.scale(TITLE, (width // 1.7, height // 1.7))


def gif_p(path):
    pil_image = Image.open(path)
    frames = []
    for frame in range(pil_image.n_frames):
        pil_image.seek(frame)
        pygame_image = pygame.image.fromstring(pil_image.convert("RGBA").tobytes(), pil_image.size, "RGBA")
        pygame_image = pygame.transform.scale(pygame_image, resolution)
        frames.append(pygame_image)
    return frames
    

def get_font(size):
    return pygame.font.Font("Main_menu/resource/PKMN RBYGSC.ttf", size)


# Resolution, mode
def options(button_bg,frames,frame_index):
    global height, width,running
    # frame_index = 0
    clock = pygame.time.Clock()

    while running:
        font_size = height // 20
        screen.blit(frames[frame_index], (0, 0))  # Display current frame
        frame_index = (frame_index + 1) % len(frames)  # Loop GIF frames

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        RESOLUTION_BUTTON = Button(button_bg, pos=(640, 250), 
                                text_input="RESOLUTION", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        MODE_BUTTON = Button(button_bg, pos=(640, 400), 
                                text_input="MODE", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(button_bg, pos=(640, 550), 
                                text_input="BACK", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        
        for button in [RESOLUTION_BUTTON, MODE_BUTTON, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESOLUTION_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pass
                if MODE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(button_bg,frame_index)
        
        pygame.display.flip()
        pygame.event.pump()
        clock.tick(24) 

play_sing_frames = gif_p("Main_menu/resource/play_sing2.gif")
# for i in range(len(play_sing_frames)):
#     play_sing_frames[i].fill((200, 200, 200), special_flags=pygame.BLEND_RGB_MULT)
play_multi_frames = gif_p("Main_menu/resource/Play_multi.gif")


play_idle_frames = gif_p("Main_menu/resource/idle.gif")

def play(button_bg):
    global height, width,play_sing_frames, play_multi_frames, running 

    clock = pygame.time.Clock()
    frame_index = [0,0,0]
    single_hover = False
    multi_hover = False
    
    while running:
        font_size = height // 20

        screen.blit(play_idle_frames[frame_index[2]], (0, 0))
        frame_index[2] = (frame_index[2] + 1) % len(play_idle_frames)

        if single_hover:
            screen.blit(play_sing_frames[frame_index[0]], (0,0))
            frame_index[0] = (frame_index[0] + 1) % len(play_sing_frames)
            single_hover = False

        elif multi_hover:
            screen.blit(play_multi_frames[frame_index[1]], (0,0))
            frame_index[1] = (frame_index[1] + 1) % len(play_multi_frames)
            multi_hover = False


        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SINGLE = Button(button_bg, pos=(width//2 - width//3, height//2 - height//3), 
                                text_input="SINGLE", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        MULTI = Button(button_bg, pos=(width//2 - width//3, height//2 - height//3+ 150 ), 
                                text_input="MULTI", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(button_bg, pos=(width//2 - width//3, height//2 - height//3 + 300), 
                                text_input="BACK", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        
        for button in [SINGLE, MULTI, BACK_BUTTON]:
            name,is_hover = button.changeColor(PLAY_MOUSE_POS)
            # if name == "SINGLE" and is_hover == True:
            #     screen.blit(play_sing_frames[frame_index[0]], (0,0))
            #     frame_index[0] = (frame_index[0] + 1) % len(play_sing_frames)
            # elif name == "MULTI" and is_hover == True:
            #     screen.blit(play_multi_frames[frame_index[1]], (0,0))
            #     frame_index[1] = (frame_index[1] + 1) % len(play_multi_frames)
            if name == "SINGLE" and is_hover:
                single_hover = True
            elif name == "MULTI" and is_hover:
                multi_hover = True

            button.update(screen)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SINGLE.checkForInput(PLAY_MOUSE_POS):
                    running = False
                if MULTI.checkForInput(PLAY_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu(button_bg,frame_index = 0)

        # frame_index = (frame_index + 1) % len(play_sing_frames)
        pygame.display.flip()
        pygame.event.pump()
        clock.tick(12) #sus
    

def quit():
    pygame.quit()
    sys.exit()
    pass

menu_frames = gif_p("Main_menu/resource/BG_2.gif") # load first

def main_menu(button_bg,frame_index):
    global height, width, menu_frames,running
    tw, th = TITLE.get_size()
    
    # frame_index = 0
    clock = pygame.time.Clock()
    # button_bg = pygame.image.load("Game/resource/button.png")

    while running:
        font_size = height // 20
        
        screen.blit(menu_frames[frame_index], (0, 0))  # GIF as background
        frame_index = (frame_index + 1) % len(menu_frames)  # Cycle GIF frames

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(TITLE, (width//2 - tw//2, height//2 - th//2 - (height // 2.7)))

        
        PLAY_BUTTON = Button(button_bg, pos=(width//2, height//2 - height//5.9), 
                                text_input="PLAY", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(button_bg, pos=(width//2, height//2 - height//5.9 + 150), 
                                text_input="OPTIONS", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(button_bg, pos=(width//2, height//2 - height//5.9 + 300), 
                                text_input="QUIT", font=get_font(font_size), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(button_bg)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(button_bg,menu_frames,frame_index) #menu fram = option fram
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit()

        pygame.display.flip()
        pygame.event.pump()  
        clock.tick(24)  


# Run the main menu
# main_menu(button_bg = pygame.image.load("Main_menu/resource/button.png"),frame_index = 0)
