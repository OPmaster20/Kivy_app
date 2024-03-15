import re

import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.label import Label
import kivy.clock as c
from kivy.lang import Builder
from kivy.uix.settings import Settings
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
from kivy.config import ConfigParser

from kivy.config import Config
Config.set('kivy', 'window_icon', 'icons.ico')


pd_etime = 0
Builder.load_file('box.kv')

class init_box(Screen):
    def __init__(self, **kwargs):
        self.count = 0
        self.end_time = 0

        super(init_box, self).__init__(**kwargs)

    def init(self):

        self.mains = self.ids.box_id
        self.mains.add_widget(self.ids.pd_id, index=0)
        self.mains.add_widget(self.ids.label_id, index=1)
        #self.mains.add_widget(self.ids.but1)
        # self.mains.add_widget(self.ids.count_id,index=2)
        self.ids.count_id.pos = (100, 100)
        self.register_event_type('run_pd')

    def up(self):
        self.end_time = time.time()
        self.up_pd = c.Clock.schedule_interval(self.update_pd, (pd_stime - self.end_time))

    def update_pd(self, time):
        if self.ids.pd_id.value == self.ids.pd_id.max:
            self.ids.label_id.opacity = 0
            self.ids.label_id.text = "This is Apple Home"
            anim2 = Animation(opacity=1, duration=10)
            anim2.start(self.ids.label_id)
            self.up_pd.cancel()
            self.ids.pd_id.opacity = 0
            self.ids.count_id.opacity = 0
            self.change()
        else:
            self.ids.count_id.text = "Loading :" + str(self.count)
            self.ids.pd_id.value = self.ids.pd_id.value + 10
            self.count = self.count + 10
            self.up_pd()

    def change(self):
        self.ids.but1.opacity = 1

        with self.canvas:
            self.RR1 = RoundedRectangle(source='a2.png', size=(430, 430),
                                        pos=(self.center_x - 230, self.center_y - 300),
                                        radius=[(5, 5), (5, 5), (5, 5), (5, 5)])
            self.RR2 = RoundedRectangle(source='a3.png', size=(230, 230),
                                        pos=(700, 400),
                                        radius=[(200, 200), (200, 200), (200, 200), (200, 200)])
            self.RR3 = RoundedRectangle( size=(130, 130), source='a1.gif',
                                        pos=(400, 350),
                                        radius=[(200, 200), (200, 200), (200, 200), (200, 200)])
            self.RR4 = RoundedRectangle(size=(400, 400), source='a4.png',
                                        pos=(20, 20),
                                        radius=[(200, 200), (200, 200), (200, 200), (200, 200)])

            self.RR5 = RoundedRectangle(size=(400, 400), source='a5.png',
                                        pos=(630, 20),
                                        radius=[(200, 200), (200, 200), (200, 200), (200, 200)])






        self.canvas.remove(self.RR1)
        self.canvas.remove(self.RR2)
        path = "entry.wav"
        b = SoundLoader.load(path)
        b.play()
        anim1 = Animation(radius=[(200, 200), (200, 200), (200, 200), (200, 200)], duration=2, t='in_quad') + Animation(
            size=(150, 150), pos=(150, 500), duration=2, t='in_circ')
        time.sleep(1)
        anim1.start(self.RR1)

        anim_est = Animation(size=(227, 227), duration=2, t='in_quad') + Animation(
            size=(245, 245), duration=1, t='in_quad') + Animation(
            size=(230, 230), duration=2, t='in_quad')
        anim_est.repeat = True

        anim_run = Animation(size=(350,350),duration=2,t='in_circ') + Animation(
            size=(400, 400), duration=1, t='in_quad') + Animation(
            size=(410, 410), duration=2, t='in_quad')
        anim_run.repeat = True
        anim_est.start(self.RR2)
        anim_est.start(self.RR3)
        anim_run.start(self.RR4)


        anim_text = Animation(color=[0, 255, 0, 1],duration=3,t='in_quad') + Animation(color=[0, 0, 255, 1],duration=3,t='in_quad')

        anim_text.repeat = True
        anim_text.start(self.ids.label_id)




        self.canvas.add(self.RR1)
        self.ids.but1.disabled = False

        self.canvas.add(self.RR2)


class init_user(Screen):
    def __init__(self, **kwargs):
        super(init_user, self).__init__(**kwargs)
        self.move(self.ids.text20)

    def move(self,n):
        coco = Animation(color=[0, 255, 0, 1], duration=3, t='in_circ') + Animation(color=[0, 0, 255, 1],
                                                                                    duration=3, t='in_quad')
        coco.repeat = True
        coco.start(n)

    def init_interface(self):


        self.grid = self.ids.box2_id
        self.grid.add_widget(self.ids.text1)
        self.grid.add_widget(self.ids.username)
        self.grid.add_widget(self.ids.text2)
        self.grid.add_widget(self.ids.password)
        self.grid.add_widget()


        print("ok")



    def output(self):
        '''

        code = user.search(self.ids.username.text, self.ids.password.text)
        if code == 1:
            self.ids.username.select_all()
            self.ids.username.text = ''
            self.ids.password.select_all()
            self.ids.password.text = ''
        else:
            message.work1(2)
            self.manager.current = 'sub3'

        '''

        self.manager.current = 'sub3'


class register_user(Screen):
    def __init__(self, **kwargs):
        self.text_code = ''
        self.count = 0
        self.code_file_name = ''
        self.auto_del()
        self.operate_code()

        super(register_user, self).__init__(**kwargs)
        with self.canvas:
            self.s1 = Rectangle(
                source='star.png',
                size=(200,200),
                pos=(250,350))
            self.s2 = Rectangle(
                source='star.png',
                size=(100,100),
                pos=(500,400))
            self.s3 = Rectangle(
                source='star.png',
                size=(50,50),
                pos=(650,500))

        self.movie()



    def operate_code(self):
        filename = self.code_file_name
        if os.path.isfile(filename):
            os.remove(filename)
            print("removed over")
        self.generate()


    def auto_del(self):
        file_path = os.listdir()
        for i in file_path:
            if re.search("^[v_code]+.\\.png$",i):
                os.remove(i)
                print(f"removed over {i}")

    def movie(self):
        anim_s1 = Animation(pos=(490,560),duration=20)
        anim_s1.start(self.s1)
        anim_s2 = Animation(pos=(590, 500), duration=20)
        anim_s2.start(self.s2)
        anim_s3 = Animation(pos=(600, 300), duration=20)
        anim_s3.start(self.s3)

    def generate(self):
        self.count += 1
        code_img = Image.new('RGB', (120, 40), 'white')
        draw_img = ImageDraw.Draw(code_img)
        font = ImageFont.truetype('arial.ttf', size=30)
        code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
        draw_img.text((10, 5), code, font=font, fill='black')
        for _ in range(random.randint(50, 100)):
            draw_img.point((random.randint(0, 120), random.randint(0, 40)), fill='black')
        image = code_img.filter(ImageFilter.BLUR)
        image.save("v_code" + str(self.count) + ".png")
        self.code_file_name = "v_code" + str(self.count) + ".png"
        self.text_code = code









    def proof(self):

        user.register_search(self.ids.register_username.text,self.ids.register_password.text,self.ids.confirm_password.text,self.ids.register_email.text)
        if self.ids.vcode.text != self.text_code:
            message.mess2(1)
            self.ids.re_box.canvas.after.clear()
            self.operate_code()
            print(self.text_code,self.ids.vcode.text)
            self.ids.vcode.select_all()
            self.ids.vcode.text = ''
            with self.canvas.after:
                RoundedRectangle(
                source = self.code_file_name,
                size = (250,100),
                pos = (250,80))





class Apple(App):
    def build(self):
        self.icon = 'icons.ico'

        myapp = ScreenManager()
        myapp.add_widget(init_box(name='main'))
        myapp.add_widget(init_user(name='sub1'))
        myapp.add_widget(page1.qr_log_in(name='sub2'))
        myapp.add_widget(register_user(name='register'))
        myapp.add_widget(page1.mainpage(name='sub3'))
        myapp.add_widget(page2.user_infor(name='sub4'))
        return myapp


if __name__ == "__main__":
    pd_stime = time.time()


    Apple().run()

