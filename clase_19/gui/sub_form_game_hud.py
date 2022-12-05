import pygame, sys
from gui.constantes import * # REVISAR
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label
from gui.gui_responsive_label import ResponsiveLabel
from gui.hud_life import HudLife
from gui.hud_bullets import HudBullets
from gui.hud_time import HudTime
from gui.hud_static_bar import HudBar
from gui.hud_score import HudScore
import time
import datetime

from settings import get_levels


class SubFormGameHud(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, image_background, color_border, levels=0, qty_levels=0, active=True, score=0, max_life=10, life=10, bullets=0, time=0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.name = name
        self.image_background = image_background
        self.color_border = color_border
        self.active = active

        # main
        self._main_surface = main_surface
        self._main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(topleft=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            topleft=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))
        
        # PJ
        # self.score = score
        self.score = -1
        self.max_life = max_life
        # self.life = -1
        self.life = life
        self.bullets = bullets
        self.current_time = time
        # self.bullets = -1

        # levels
        self.qty_levels = qty_levels
        self.game_levels = levels
        self.list_levels = ''
        if self.qty_levels:
            self.list_levels = self.show_levels(self.qty_levels)
       
        self.gui_bar = HudBar(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=ANCHO_VENTANA/2,
            y=ALTO_VENTANA-5,
            w=ANCHO_VENTANA + ANCHO_VENTANA/5,
            h=150,
        )
        self.gui_life = HudLife(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=ALTO_VENTANA-25,
            w=500,
            h=30,
            color_background=VIOLET, # change to background img
            color_border='white', 
            max_life=self.max_life,
            value=self.life,
            )
        self.gui_bullets = HudBullets(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=ANCHO_VENTANA-200,
            y=ALTO_VENTANA-25,
            w=300,
            h=30,
            color_background=VIOLET, # change to background img
            color_border='white', 
            max_bullets=self.bullets,
            value=self.bullets,
            )
        self.gui_score = HudScore(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=200,
            y=ALTO_VENTANA-25,
            w=200,
            h=40,
            color_background=VIOLET, # change to background img
            color_border='white', 
            value=self.score,
            font=PATH_FONT,
            font_size=25,
            font_color='white')
        self.gui_time = HudTime(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=ANCHO_VENTANA-120,
            y=35,
            w=200,
            h=40,
            color_background=VIOLET, # change to background img
            color_border='white', 
            value=self.current_time,
            font=PATH_FONT,
            font_size=25,
            font_color='white')

    """ def on_click(self, value):
        if self.running:
            self.running = False
            self.level.running = False
            self.sub_form_pause_game.active=True
        
    def update_view_form(self, id_form):
        print(self.dict_forms)
        super().update_view_form(id_form) # apaga los forms y activa el actual
        self.dict_forms[id_form].running = True
        self.dict_forms[id_form].change_level(self.level, id) """


    """ def get_damage(self, amount):
        if self.life > 0: # Si recibe daño y aún tiene vida, restarle 
            self.life -= amount
        if self.life <= 0:
            self.life = 0

    def get_health(self, amount):
        if self.life < self.max_life:
            self.life += amount
        if self.life >= self.max_life:
            self.life = self.max_life """

    def update(self, score, life, bullets, time):
        if score != self.score:
            self.score = score
            self.gui_score.update(self.score)

        if life != self.life:
            # comparar las vidas, si la vida que viene es mas chica que la que tiene, entonces se restó vida. Si la vida que viene es mas grande que la que tiene, entonces sumó vida (g0d)
        

            self.amount_life = life - self.life

            if life > self.life:
                print('➕ Sumó vida')
                self.gui_life.get_health(self.amount_life) # resta vida
            if life < self.life:
                print('➖ Restó vida')
                self.gui_life.get_damage() # resta vida


            # print('>>>>>',self.amount_life)
            # if self.amount_life > 0:
            # self.gui_life.update(self.amount_life) # resta vida







            # self.amount_life = self.life - life
            # print('>>>>>',self.amount_life)
            # if self.amount_life > 0:
            #     self.gui_life.get_damage() # resta vida


            # if self.life < self.max_life:
            #     self.life += amount
            # if self.life >= self.max_life:
            #     self.life = self.max_life

            # if self.amount_life < 0:
            #     print('Te sumaste vida') # suma vida
            #     self.gui_life.get_health()
            self.life = life
        
        if bullets != self.bullets:
            if bullets > self.bullets:
                self.bullets = bullets
                self.gui_bullets.update_bullets(self.bullets)
            else:
                self.bullets = bullets

            self.gui_bullets.update()

        self.gui_time.update(time)

        self.draw()

    def draw(self):
        self.slave_surface.blit(self.image_background, self.slave_rect)
        self.gui_bar.draw()
        # for label in self.label_list: # dibujamos los botones
        #     label.draw()
        
        self.gui_score.draw()
        self.gui_life.draw()
        self.gui_bullets.draw()
        self.gui_time.draw()
        # self.r_label_score.draw()
