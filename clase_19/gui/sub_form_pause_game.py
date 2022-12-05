import pygame, sys, re
from gui.constantes import * # REVISAR
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label
from gui.gui_responsive_label import ResponsiveLabel
from gui.form_settings import FormSettings

class SubFormPauseGame(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, color_background, color_border, active, music):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'background'

        # self.id_music = 'menu'
        self.x, self.y, self.w, self.h = x, y, w, h
        self.name = name
        self.color_background = color_background
        self.color_border = color_border
        self.active = active

        # main
        self._main_surface = main_surface
        self._main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(center=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            center=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))

        # media
        self.slave_surface.fill(self.color_background)

        self.label_title = Label(
            # inherit_rect=self,
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6,
            w=500,
            h=50,
            color_background=VIOLET, # change to background img
            text='Pause...',
            text_pos='center_plus',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.continue_game = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70,
            w=400,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_play_level',
            text='Continue',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            on_click_param_aux=''
        )
        self.settings_menu = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70 + 70,
            w=400,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_settings',
            text='Settings',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            on_click_param_aux=''
        )
        self.main_menu = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70 + 70 + 70,
            w=400,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Main menu',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            on_click_param_aux=''
        )
        self.exit_game = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70 + 70 + 70 + 70,
            w=400,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='exit',
            text='Exit to desktop',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            on_click_param_aux=''
        )
        
        # self.label_title
        self.button_list = [self.continue_game,self.settings_menu,self.main_menu,self.exit_game]
    
    # def on_click(self, id):
    #     if id == 'form_settings':
    #         print('l0l')
    #         self.form_settings = FormSettings(
    #             name='form_settings_outside',
    #             main_surface=self._main_surface,
    #             x=50,
    #             y=50,
    #             w=ANCHO_VENTANA - 100,
    #             h=ALTO_VENTANA - 100,
    #             color_background=RED,
    #             slave_background=f'{PATH_IMAGE}/gui/jungle/settings/bg.png',
    #             color_border='',
    #             active=False,
    #             music=self.music_manager,
    #             outside=True)
    #         super().on_click('form_settings_outside')
    #     else: 
    #         super().on_click(id)
    #     pass


    def update_view_form(self, id_form):
        super().update_view_form(id_form) # apaga todos los form y activa el presente
        self.dict_forms[id_form].running = True
        self.active = False
        if id_form == 'form_play_level':
            self.dict_forms[id_form].level.running = True
        

    def update(self, event_list):
        if self.active and not self.playing_music:
            # self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
        # self.get_key_event(event_list)
        self.label_title.draw()

        for button in self.button_list:
            button.update(event_list)
            button.draw()

    def draw(self):
        pass
