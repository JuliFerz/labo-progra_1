import pygame, sys
from gui.constantes import * # REVISAR
from gui.gui_button import Button
from gui.gui_label import Label
from gui.form_gui import Form

class FormMainMenu(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, music):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        self.first_menu = True
        self.id_music = 'menu'

        # print(self.main_surface_rect)
        self.label_title = Label(
            # inherit_rect=self,
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/6,
            w=500,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='PYGAME | GAME',
            text_pos='center', # REVISAR
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_start = Button(
            # inherit_rect=self,
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/4,
            w=300,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='form_main_menu_selection',
            text='Play levels',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        """ self.button_level_editor = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/4+70,
            w=300,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_level_editor_gui',
            text='Level editor',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black') """
        self.button_settings = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/4+70,
            w=300,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_settings',
            text='Settings',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_game_score = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/4+70+70,
            w=300,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_scores',
            text='Scores',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_exit = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/4+70+70+70,
            w=300,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='exit',
            text='Quit game',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        
        self.label_list=[self.label_title]
        # self.widget_list=[self.button_start]
        # self.widget_list=[self.button_start, self.button_level_editor, self.button_settings, self.button_game_score, self.button_exit]
        self.widget_list=[self.button_start, self.button_settings, self.button_game_score, self.button_exit]

    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_w:
                    self.on_click('form_main_menu_selection')
                if event.key == pygame.K_e:
                    self.on_click('form_settings')
    
    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            if not self.first_menu: self.music_manager.update('select')
            self.playing_music = True
            self.first_menu = False
        
        # draw slave_form
        self.get_key_event(event_list)

        # draw method (button) in slave_form
        self.label_title.draw()

        for button in self.widget_list:
            button.update(event_list)
            button.draw()
        super().draw()

    def draw(self):
        pass
