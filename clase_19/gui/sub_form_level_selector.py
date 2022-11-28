import pygame, sys
from constantes import *
from gui_widget import Widget
from gui_button import Button
from gui_label import Label
from form_gui import Form

class SubFormLevelSelector(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, color_background, color_border, levels=0, active=True):
        # super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active)
        # self.slave_surface = main_surface
        self.x, self.y, self.w, self.h = x, y, w, h

        self._main_surface = main_surface
        self._main_rect = main_rect
        
        self.color_background = color_background
        self.color_border = color_border


        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(center=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            center=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))

        self.list_levels = levels
        if self.list_levels:
            self.list_levels = self.show_levels(self.list_levels)
        

    def show_levels(self, list_levels):
        temp_list = []
        y = 0
        for i, level in enumerate(list_levels):
            temp_list.append(
                Button(
                    # inherit_rect=self,
                    main_surface=self.slave_surface,
                    main_rect=self.slave_rect_collide,
                    x=self.slave_rect.w/2,
                    y=50 + y,
                    w=500,
                    h=70,
                    color_background=BLUE, # change to background img
                    color_border='', # think in how button image works while pressing click on it
                    on_click=self.on_click,
                    on_click_param='form_main_menu',
                    text='Level {}'.format(i+1),
                    font=PATH_FONT,
                    font_size=25,
                    font_color='black'
                )
            )
            y += 90
        return temp_list

    def on_click(self, form): 
        if form == 'exit':
            sys.exit()
        else:
            self.update_view_form(form)

    def click_collition(self, mouse_xy):
        # colisionar SOLO con botones que estén dentro del segundo form
        if self.slave_rect_collide.collidepoint(mouse_xy):
            print('l0l')

    def get_mouse_click(self, event_list):
        # print(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                self.click_collition(event.pos)

    def update(self, event_list):
        # No se debe dibujar con la herencia. Sobreescribe el slave_surface de form_main_menu_level_selection
        # super().draw()
        
        # self.get_mouse_click(event_list)

        if self.list_levels:
            for level in self.list_levels:
                level.update(event_list)
                level.draw()

    def draw(self):
        # pygame.draw.rect(self.slave_surface, BLUE, self.slave_rect_collide)
        pass
        # print(self.list_levels)
