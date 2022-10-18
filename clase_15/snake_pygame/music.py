import pygame as py
import src

# set music
py.mixer.init()
# background music
background_m = py.mixer.Sound(src.M_FONDO)
background_m.set_volume(0.7)
# eat apple
crunchy = py.mixer.Sound(src.S_CRUNCH)
# lose game
punch = py.mixer.Sound(src.S_PUNCH)
punch.set_volume(0.5)
