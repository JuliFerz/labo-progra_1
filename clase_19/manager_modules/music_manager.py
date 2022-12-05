class MusicManager():
    def __init__(self, music):
        self.music = music
        self.id = ''
        self.update
        self.play_music = True
        self.play_effects = True

        print('⭕ Instance')

    def change_play_effects(self):
        self.play_effects = not self.play_effects

    def change_play_music(self):
        self.play_music = not self.play_music

        if not self.play_music:
            self.update_song()
        elif self.play_music:
            self.update_song(self.id)

    def change_volume(self, id):
        for music in self.music.obj_music:
            if id > 0:
                self.music.change_volume(self.music.obj_music[music], 0.01)
            else:
                self.music.change_volume(self.music.obj_music[music], -0.01)

    def play_sound(self, id):
        self.music.Play(self.music.obj_music[id])

    def change_song(self, id):
        self.music.PlayInLoop(self.music.obj_music[id])

    def update_song(self, id=''):
        for music in self.music.obj_music:
            self.music.Stop(self.music.obj_music[music])
        if id:
            self.change_song(id)

    def update(self, id):
        if id in ['menu', 'background'] and self.play_music:
            if self.id != id:
                print('🎹🎵🎶id:', id)
                print('>>>', id, self.play_music)
                self.id = id
                self.update_song(self.id)
        elif id not in ['menu', 'background'] and self.play_effects:
            print('🔈Sound!', id)
            self.play_sound(id)