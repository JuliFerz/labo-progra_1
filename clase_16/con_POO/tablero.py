import pygame as py
from tarjeta import Tarjeta
from boton import Boton
from musica import Music
from score import Score
import time
import re
import random

class Tablero:
    def __init__(self, l_tarjetas, l_botones, score, background, win, start):
        self.l_tarjetas = l_tarjetas
        self.l_botones = l_botones
        self.score = score
        self.background = background
        self.win = win
        self.running = start
        self.tiempo_tarjeta = 0

    
    def colicion(self, pos_xy: tuple) -> None:
        lista_tarjetas = self.l_tarjetas
        fn = Tarjeta(l_tarjetas=lista_tarjetas)
 
        flip = Music('/voltear.wav')
        if fn.get_visibles_no_descubiertas() < 2 and self.running:
            for i in range(len(lista_tarjetas)):
                if lista_tarjetas[i]['rect'].collidepoint(pos_xy) and not lista_tarjetas[i]['descubierto']:
                    self.tiempo_tarjeta = py.time.get_ticks()
                    if not lista_tarjetas[i]['visible']:
                        flip.Play # MUSIC
                        lista_tarjetas[i]['visible'] = True
                    break

        click = Music('/clic.wav') # MUSIC
        for btn in self.l_botones:
            if btn['rect'].collidepoint(pos_xy):
                if (re.search('/start.png', btn['path_imagen']) and not self.running):
                    click.Play # MUSIC
                    self.restart_game()
                    self.background.PlayInLoop
                    self.win.Stop
                    self.running = True
                elif (re.search('/restart.png', btn['path_imagen']) and self.running):
                    click.Play # MUSIC
                    self.restart_game()

    
    def update(self):
        tiempo_actual = py.time.get_ticks()

        lista_tarjetas = self.l_tarjetas
        fn = Tarjeta(l_tarjetas=lista_tarjetas)

        if self.running:
            time_lapse = Score(score=self.score, txt='Tiempo', value=int(tiempo_actual / 1000)) 
            time_lapse.update() 
            fn.match()
            if((tiempo_actual >= self.tiempo_tarjeta + 600)):
                for el in lista_tarjetas:
                    if not el['descubierto']:
                        el['visible'] = False
            if(fn.get_descubiertas() == len(lista_tarjetas)):
                self.background.Stop
                self.win.Play
                self.running = False


    def render(self, superficie) -> None:
        # render cards
        fn_card = Tarjeta(l_tarjetas=self.l_tarjetas, superficie=superficie)
        fn_card.draw()

        # render buttons
        fn_btn = Boton(l_botones=self.l_botones, superficie=superficie)
        fn_btn.draw()

        # render time_lapse
        time_lapse = Score(score=self.score, superficie=superficie)
        time_lapse.draw()


    def shuffle(self) -> None:
        lista_tarjetas = self.l_tarjetas
        
        temp_list = []
        for card in lista_tarjetas:
            for key, value in card.items():
                temp_list.append(value) if key == 'rect' else ''
        random.shuffle(temp_list)
        for i in range(len(lista_tarjetas)):
            lista_tarjetas[i].update({'rect': temp_list[i]})


    
    def restart_game(self) -> dict:
        lista_tarjetas = self.l_tarjetas
        for el in lista_tarjetas:
            el['visible'] = False
            el['descubierto'] = False
        self.shuffle()
   