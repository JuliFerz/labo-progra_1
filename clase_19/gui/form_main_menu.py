import pygame, sys
from constantes import *
from gui_widget import Widget
from gui_button import Button
from gui_label import Label
from form_gui import Form

class FormMainMenu(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active)

        # print(self.main_surface_rect)
        self.label_title = Label(
            # inherit_rect=self,
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6,
            w=500,
            h=50,
            color_background=VIOLET, # change to background img
            text='PYGAME | GAME',
            font=PATH_FONT,
            font_size=25,
            font_color='black')

        self.button_start = Button(
            # inherit_rect=self,
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/3,
            w=300,
            h=50,
            color_background=VIOLET, # change to background img
            color_border='', # think in how button image works while pressing click on it
            on_click=self.on_click,
            on_click_param='form_main_menu_selection',
            text='Play levels',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_level_editor = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/3+70,
            w=300,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_level_editor_gui',
            text='Level editor',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_configuration = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/3+70+70,
            w=300,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_configuration_gui',
            text='Configuration',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_credits = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/3+70+70+70,
            w=300,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_credits_gui',
            text='Credits',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_exit = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/3+70+70+70+70,
            w=300,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='exit',
            text='Exit',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.label_list=[self.label_title]
        self.widget_list=[self.button_start, self.button_level_editor, self.button_configuration, self.button_credits, self.button_exit]


    def on_click(self, form):
        # print('Pressed:', form)
        if form == 'exit':
            sys.exit()
        else:
            self.update_view_form(form)

    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def update(self, event_list):
        # draw slave_form
        super().draw()
        self.get_key_event(event_list)

        # draw method (button) in slave_form
        self.label_title.draw()
        for widget in self.widget_list:
            widget.update(event_list)
            widget.draw()

    def draw(self):
        pass
