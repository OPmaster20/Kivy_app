import re
import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.label import Label
import kivy.clock as c
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.graphics import RoundedRectangle,Rectangle
import user, message
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import time
import page1,os,page2
Builder.load_file('user.kv')

class user_infor(Screen):
    def __init__(self,**kwargs):
        super(user_infor, self).__init__(**kwargs)
        self.get_user_infor()
        coco = Animation(color=[0, 255, 0, 1], duration=3, t='in_circ') + Animation(color=[0, 0, 255, 1],
                                                                                    duration=3, t='in_quad')
        coco.repeat = True
        coco.start(self.ids.loved_singer)
        coco.start(self.ids.loved_song)
        coco.start(self.ids.loved_song_times)
        coco.start(self.ids.title)
    def get_user_infor(self):
        self.ids.loved_singer.text = user.computer_user_loved()
        self.re1,self.re2 = user.computer_user_loved_song()
        self.ids.loved_song.text = self.re1
        self.ids.loved_song_times.text = str(self.re2)
        self.ids.user_name.text = user.get_username()



    def user_log_out(self):
        user.user_log_out_fun()
        self.ids.loved_singer.text = "None"
        self.ids.loved_song.text = "None"
        self.ids.loved_song_times.text = "None"
        self.ids.user_name.text = "None"
