import pygame, sys
from gui.constantes import * # REVISAR
from gui.gui_button import Button
from gui.gui_label import Label
from gui.form_gui import Form
from gui.sub_form_level_selector import SubFormLevelSelector
# from settings import level_map

class FormSettings(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, music, outside=False):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.main_surface = main_surface
        self.outside = outside

        self.music_manager = music
        self.playing_music = False
        self.id_music = 'menu'

        self.table_img = pygame.image.load(f'{PATH_IMAGE}/gui/jungle/settings/table.png')
        self.table_img = pygame.transform.scale(self.table_img,(self.w - self.w/4, self.h - self.h/5))
        self.rect_table_img = self.table_img.get_rect(center=(self.slave_rect.centerx-50, self.slave_rect.centery-50))
        self.rect_table_img.w, self.rect_table_img.h = self.slave_rect.w, self.slave_rect.h

        self.icon_img = pygame.image.load(f'{PATH_IMAGE}/gui/jungle/settings/92.png')
        self.icon_img = pygame.transform.scale(self.icon_img,(self.w/2 - self.w/5, self.h/2 - self.h/4))
        self.rect_icon_img = self.icon_img.get_rect(center=(self.slave_rect.centerx-50, self.slave_rect.top + (self.h/8)-50))
        self.rect_icon_img.w, self.rect_icon_img.h = self.slave_rect.w, self.slave_rect.h


        # buttons
        """ if self.outside:
            self.button_back = Button(
                main_surface=self.slave_background,
                main_rect=self.slave_background_rect,
                x=ANCHO_VENTANA-450, #mejor: x=self.slave_rect.w-200,
                # x=self.slave_background_rect.w/1, #mejor: x=self.slave_rect.w-200,
                y=ALTO_VENTANA-250, #mejor: y=self.slave_rect.h-150,
                w=150,
                h=50,
                color_background=VIOLET,
                slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
                color_border='',
                on_click=self.on_click,
                on_click_param='form_play_level',
                text='Back',
                text_pos='center',
                font=PATH_FONT,
                font_size=25,
                font_color='white'
            )
        else:
            self.button_back = Button(
                main_surface=self.slave_background,
                main_rect=self.slave_background_rect,
                x=ANCHO_VENTANA-450, #mejor: x=self.slave_rect.w-200,
                # x=self.slave_background_rect.w/1, #mejor: x=self.slave_rect.w-200,
                y=ALTO_VENTANA-250, #mejor: y=self.slave_rect.h-150,
                w=150,
                h=50,
                color_background=VIOLET,
                slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
                color_border='',
                on_click=self.on_click,
                on_click_param='form_main_menu',
                text='Back',
                text_pos='center',
                font=PATH_FONT,
                font_size=25,
                font_color='white'
            ) """
        
        self.label_volume = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - self.slave_background_rect.w/4,
            y=self.slave_background_rect.h/4,
            w=150,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Volume',
            text_pos='left',
            font=PATH_FONT,
            font_size=18,
            font_color='white'
            )
        self.label_music = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - self.slave_background_rect.w/4,
            y=self.slave_background_rect.h/3 + 15,
            w=200,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='On/Off music',
            text_pos='left',
            font=PATH_FONT,
            font_size=18,
            font_color='white'
            )
        self.label_effects = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + self.slave_background_rect.w/3 - 30,
            y=self.slave_background_rect.h/3 + 15,
            w=230,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='On/Off effects',
            text_pos='left',
            font=PATH_FONT,
            font_size=18,
            font_color='white'
            )

        self.button_back = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=ANCHO_VENTANA-450, #mejor: x=self.slave_rect.w-200,
            y=ALTO_VENTANA-250, #mejor: y=self.slave_rect.h-150,
            w=150,
            h=50,
            color_background=VIOLET,
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Back',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='white'
        )
        self.volume_down_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/4,
            w=50,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/98.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_down_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black'
        )
        self.volume_up_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/4,
            w=50,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/97.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_up_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black'
        )
        
        self.volume_quit_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/96.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_quit_music_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            active=True
        )
        self.volume_add_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/95.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_add_music_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            active=False
        )
        
        
        
        # cambiar imagen con una función ReGex
        self.volume_quit_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/96.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_quit_effects_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            active=True
        )
        self.volume_add_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/settings/95.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='volume_add_effects_button',
            text='',
            text_pos='center',
            font=PATH_FONT,
            font_size=25,
            font_color='black',
            active=False
        )

        self.change_controls_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + 30,
            y=self.slave_background_rect.h/3 + 15 + 90,
            w=350,
            h=50,
            color_background=VIOLET, # change to background img
            slave_background=f'{PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Change controls',
            text_pos='left',
            font=PATH_FONT,
            font_size=25,
            font_color='white'
        )

    def on_click(self, id):
        if id == 'form_main_menu':
            super().on_click(id)
        else:
            if id == 'volume_down_button':
                print('➖', id)
                self.music_manager.change_volume(-1)
            elif id == 'volume_up_button':
                print('➕', id)
                self.music_manager.change_volume(1)
            
            
            
            elif id == 'volume_quit_music_button':
                print('❌', id)
                self.music_manager.change_play_music()
                self.volume_quit_music_button.active = False
                self.volume_add_music_button.active = True
            elif id == 'volume_add_music_button':
                print('✅', id)
                self.music_manager.change_play_music()
                self.volume_quit_music_button.active = True
                self.volume_add_music_button.active = False


            elif id == 'volume_quit_effects_button':
                print('❌', id)
                self.music_manager.change_play_effects()
                self.volume_quit_effects_button.active = False
                self.volume_add_effects_button.active = True
            elif id == 'volume_add_effects_button':
                print('✅', id)
                self.music_manager.change_play_effects()
                self.volume_quit_effects_button.active = True
                self.volume_add_effects_button.active = False

            self.music_manager.update('select')
        

        # values
    # REVISAR - sacar
    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_click('form_main_menu')

    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
        
        self.get_key_event(event_list)

        self.button_back.draw()
        self.button_back.update(event_list)

        self.label_volume.draw()
        self.label_music.draw() # REVISAR
        self.label_effects.draw() # REVISAR
        self.volume_down_button.draw()
        self.volume_down_button.update(event_list)
        self.volume_up_button.draw()
        self.volume_up_button.update(event_list)


        if self.volume_quit_music_button.active:
            self.volume_quit_music_button.draw()
            self.volume_quit_music_button.update(event_list)
        elif self.volume_add_music_button.active:
            self.volume_add_music_button.draw()
            self.volume_add_music_button.update(event_list)



        if self.volume_quit_effects_button.active:
            self.volume_quit_effects_button.draw()
            self.volume_quit_effects_button.update(event_list)
        elif self.volume_add_effects_button.active:
            self.volume_add_effects_button.draw()
            self.volume_add_effects_button.update(event_list)
        


        self.change_controls_button.draw()
        
        super().draw()
        self.draw()


    def draw(self):
        self.slave_background.blit(self.table_img, self.rect_table_img)
        self.slave_background.blit(self.icon_img, self.rect_icon_img)
