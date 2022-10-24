import pygame as py
import score
import math
import random
import re
from functools import reduce

from constantes import *


class Music:
    py.mixer.init()
    def __init__(self, path_music, volume = 1):
        self.path_music = py.mixer.Sound(PATH_RECURSOS+path_music)
        self.volume = volume

    @property
    def Play(self):
        self.path_music.set_volume(self.volume)
        return self.path_music.play()
    
    @property
    def PlayInLoop(self):
        self.path_music.set_volume(self.volume)
        return self.path_music.play(-1)

    @property
    def Stop(self):
        return self.path_music.stop()