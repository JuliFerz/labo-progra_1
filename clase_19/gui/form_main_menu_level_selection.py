import pygame, sys
from constantes import *
from gui_button import Button
from gui_label import Label
from form_gui import Form
from sub_form_level_selector import SubFormLevelSelector

class FormMainMenuLevelSelection(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active)

        # Widgets & labels
        self.label_title = Label(
            # inherit_rect=self,
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6,
            w=500,
            h=50,
            color_background=VIOLET, # change to background img
            text='Select level',
            font=PATH_FONT,
            font_size=25,
            font_color='black')
        self.button_back = Button(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=ANCHO_VENTANA-200,
            y=ALTO_VENTANA-150,
            w=150,
            h=50,
            color_background=VIOLET,
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Back',
            font=PATH_FONT,
            font_size=25,
            font_color='black')

        # Sub-form
        self.sub_form_level_selector = SubFormLevelSelector(
            name='sub_form_level_selector',
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/2 + self.slave_rect.h/10,
            w=500,
            h=500,
            color_background=BROWN,
            color_border='',
            levels=['asdf',12,3,5] # NUEVO - pasar array de niveles
            )

        # print('B', self.sub_form_level_selector.slave_surface)


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
                    self.on_click('form_main_menu')

    def update(self, event_list):
        super().draw()
        self.draw()
        self.get_key_event(event_list)
        self.sub_form_level_selector.update(event_list)

        # draw method (button) in slave_form
        self.label_title.draw()
        self.button_back.update(event_list)
        self.button_back.draw()

        pass

    def draw(self):
        self.slave_surface.blit(
            self.sub_form_level_selector.slave_surface,
            self.sub_form_level_selector.slave_rect)
        pass
