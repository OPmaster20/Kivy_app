import pyqrcode as pq
from kivy.core.audio import SoundLoader
from kivy.graphics import RoundedRectangle,Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import qrcode as qc
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import kivy.clock as c
import message,user
import qrcode
from kivy.lang import Builder
from kivy.event import EventDispatcher
import random
import time
from kivy.animation import Animation
import os,sound_process
from kivy.properties import StringProperty,NumericProperty
from plyer import gps
import pydiogment.auga

Builder.load_file('pagebox.kv')
class qr_log_in(Screen):
    gen_num = NumericProperty(0)
    def __init__(self,**kwargs):
        self.clean_img()
        self.generate()

        #self.qr.png('code.png', scale=8, module_color='#007bff', background='#fff', quiet_zone=3)

        super(qr_log_in, self).__init__(**kwargs)

        #self.qr_code()

    def generate(self):
        self.code_str = ''
        self.gen_num += 1
        for i in range(4):
            self.code_num = random.randint(0, 9)
            self.code_str = self.code_str + str(self.code_num)

        self.data = self.code_str
        self.qr = qrcode.make("verify password: " + self.data)
        self.qr.save(self.get_filename())



    def get_filename(self):
        print("qrcode" + str(self.gen_num) + ".png")
        return "qrcode" + str(self.gen_num) + ".png"
    def clean_img(self):
        filename = "qrcode" + str(self.gen_num) + ".png"
        if os.path.isfile(filename):
            os.remove(filename)
            print("removed over")

    def qr_code_vairty(self,code = ' '):
        code = self.ids.Verification_code.text
        if code == ' ':
            message.mess1(5)

        if code != self.code_str:
            self.ids.Verification_code.select_all()
            self.ids.Verification_code.text = ''
            self.clean_img()
            self.generate()
            self.canvas.after.clear()


            with self.canvas.after:
                RoundedRectangle(
                source= self.get_filename(),
                size= (430, 430),
                pos= (120, 150),
                radius= [(20, 20), (20, 20), (20, 20), (20, 20)])

            message.mess1(4)

        else:

            user.import_guest()
            self.manager.current = 'sub3'
            message.work1(2)

class mainpage(Screen,EventDispatcher):
    def __init__(self,**kwargs):
        self.create()
        self.count = 0
        self.v = False
        self.once = 0
        self.sound = ''

        super(mainpage, self).__init__(**kwargs)
        self.coco = Animation(color=[0, 255, 0, 1], duration=3, t='in_circ') + Animation(color=[0, 0, 255, 1],
                                                                                    duration=3, t='in_quad')
        self.coco.repeat = True
        self.coco.start(self.ids.apple)
        with self.canvas:
            self.mu1 = RoundedRectangle(
                source= "m1.png",
                size= (430, 430),
                pos= (380, 230),
                radius= [(20, 20), (20, 20), (20, 20), (20, 20)])

        self.anim_run = Animation(size=(350, 350), duration=2, t='in_circ') + Animation(
            size=(400, 400), duration=1, t='in_quad') + Animation(
            size=(410, 410), duration=2, t='in_quad')
        self.anim_run.repeat = True


    def create(self):
        self.song_pos = 0
        self.box = BoxLayout(orientation='vertical')
        self.labelre = Label(text="Result", size=(20, 30),font_size="35sp",bold=True)
        self.box.add_widget(self.labelre)
        self.textre = TextInput(size=(40, 50), disabled=True)
        self.textre.bind(on_touch_down=self.listen)
        self.box.add_widget(self.textre)


        self.auto()
        self.event_listen()

    def search_songs(self):
        if len(self.ids.song_name.text) != 0:
            self.result = user.search_for_songs(self.ids.song_name.text)
            self.ids.splitter.clear_widgets()
            self.ids.splitter.add_widget(self.box)
            if self.result != 'No any result':
                str = ''
                for i in self.result.keys():
                    str = str + i + '\n' + self.result[i] + '\n'
                self.textre.text = str
            else:
                self.textre.text = self.result


    def listen(self,instance, touch):
        if instance.collide_point(*touch.pos) and self.result != 'No any result' and user.check_status_true() is True:
            if self.once == 0:
                self.ids.L1.text = self.result['song']
                user.update_count_songs(str(self.ids.L1.text))
                #pydiogment.auga.add_noise('Alone.wav',10)
                self.anim_run.start(self.mu1)
                #sound_process.optimization(self.ids.L1.text)
                if os.path.isfile(self.ids.L1.text + "song_plus.wav"):
                    self.sound = SoundLoader.load("Alonesong_plus.wav")
                    self.sound.play()
                    self.ids.play.text = "Stop"
                    self.v = True
                    self.ids.bar.max = int(self.sound.length)
                    self.ids.L3.text = str(self.sound.length)
                    self.auto_bar()
                    print("Hello")
                    self.once = 1


    def event_listen(self):
        self.if_status = c.Clock.schedule_interval(self.check_user,1.0)

    def check_user(self,time):
        if self.v is True and user.check_status_true() is True:
            self.sound.stop()
            self.if_status.cancel()

    def auto_bar(self):
        self.go = c.Clock.schedule_interval(self.update_bar,1.0)
    def auto(self):
        self.run = c.Clock.schedule_interval(self.run_br,2.0)

    def run_br(self,time):
        self.ids.car.load_next(mode='next')
        self.run()

    def play_listen(self):
        if self.v and self.once == 1:
            if self.count % 2 == 0:
                self.song_pos = self.sound.get_pos()
                print(self.song_pos)
                self.ids.bar.value = int(self.song_pos)
                self.ids.L2.text = str(self.ids.bar.value)
                self.sound.stop()
                self.anim_run.stop(self.mu1)
                self.ids.play.text = "Play"
            else:
                print(self.song_pos)
                self.auto_bar()
                self.sound.play()
                self.sound.seek(self.song_pos)
                self.anim_run.start(self.mu1)
                self.ids.play.text = "Stop"
            self.count += 1
        else:
            message.mess2(6)



    def update_bar(self,time):
        text = self.ids.play.text
        if self.ids.bar.max == self.ids.bar.value:
            self.go.cancel()
            print("no")

        if text == 'Stop' and self.v is True:
            self.ids.bar.value += 1
            self.ids.L2.text = str(int(self.ids.bar.value) + 1)
        else:
            self.go.release()





















