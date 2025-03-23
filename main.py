from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
import webbrowser as wb
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
#kv = Builder.load_file("scale.kv")

class MyMainWindow(Screen):
    def __init__(self, **kwargs):
        super(MyMainWindow, self).__init__(**kwargs)
        layout = GridLayout(cols=1, padding=10, spacing=5)
        label = Label(text='Select Difficulty')
        label2 = Label(text='')
        label3 = Label(text='')
        self.button1 = Button(text='Beginner', size_hint=(1,1), background_color=(0,0.5,1,1))
        self.button1.bind(on_press=lambda instance: setattr(self.manager, 'current', 'beginner'))

        self.button2 = Button(text='Intermediate', size_hint=(1, 1), background_color=(0.5, 0, 0.5, 1))
        self.button2.bind(on_press=lambda instance: setattr(self.manager, 'current', 'intermediate'))

        self.button3 = Button(text='Advanced', size_hint=(1, 1), background_color=(1, 0, 0, 1))
        self.button3.bind(on_press=lambda instance: setattr(self.manager, 'current', 'advanced'))
        layout.add_widget(label2)
        layout.add_widget(label)
        layout.add_widget(label3)
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)

        self.add_widget(layout)


class MyBeginner(Screen):
    def __init__(self, **kwargs):
        super(MyBeginner, self).__init__(**kwargs)
        float_layout = FloatLayout()

        layout = GridLayout(cols=2, rows=4, padding=20, spacing=10)

        self.button1 = Button(text='Block Chain', size_hint=(1,1), background_normal='im1.jpg', font_size='11sp')
        self.button2 = Button(text='Neural Networks', size_hint=(1, 1), background_color=(0, 0.5, 1, 1), font_size='11sp')
        self.button3 = Button(text='Augmented Reality', size_hint=(1, 1), background_color=(0, 0.5, 1, 1), font_size='11sp')
        self.button4 = Button(text='Bold Bots', size_hint=(1, 1), background_normal='im1.jpg', font_size='11sp')
        self.button5 = Button(text='Dodging Dockers', size_hint=(1, 1), background_normal='im1.jpg', font_size='11sp')
        self.button6 = Button(text='Physics Engines', size_hint=(1, 1), background_color=(0, 0.5, 1, 1), font_size='11sp')

        self.button1.bind(on_press=lambda instance: self.callback('https://youtu.be/gyMwXuJrbJQ'))
        self.button2.bind(on_press=lambda instance: self.callback('https://youtu.be/w8yWXqWQYmU'))
        self.button3.bind(on_press=lambda instance: self.callback('https://www.youtube.com/watch?v=02YRwQsaFeg&list=PLPJUho5jpFX-QomGPtAqpEKacSOjUQ5UH'))
        self.button4.bind(on_press=lambda instance: self.callback('https://youtu.be/0r1Bhf7ALJU'))
        self.button5.bind(on_press=lambda instance: self.callback('https://youtu.be/ne6R0Zluqj4'))
        self.button6.bind(on_press=lambda instance: self.callback('https://youtu.be/lzI7QUyl66g?list=PLSlpr6o9vURwq3oxVZSimY8iC-cdd3kIs'))

        self.back_button = Button(text='Back',background_normal='', size_hint=(None, None), size=(100, 50),
                                  background_color=(0.2, 0.2, 0.2, 1), font_size='11sp')
        self.back_button.pos_hint = {'x': 0, 'top': 1}
        self.back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))

        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)
        layout.add_widget(self.button4)
        layout.add_widget(self.button5)
        layout.add_widget(self.button6)

        float_layout.add_widget(layout)
        float_layout.add_widget(self.back_button)

        self.add_widget(float_layout)

    def callback(self, url):
        wb.open(url)

class MyIntermediate(Screen):
    def __init__(self, **kwargs):
        super(MyIntermediate, self).__init__(**kwargs)
        float_layout = FloatLayout()
        layout = GridLayout(cols=2, rows=3, padding=20, spacing=10)

        self.button1 = Button(text='Optical Character Recognition', size_hint=(1,1), background_normal='pp.jpg', font_size='11sp')
        self.button2 = Button(text='NES Emulator', size_hint=(1, 1), background_color=(0.5, 0, 0.5, 1), font_size='11sp')
        self.button3 = Button(text='Command Line Commander', size_hint=(1, 1), background_color=(0.5, 0, 0.5, 1), font_size='11sp')
        self.button4 = Button(text='Ray Casting Engine', size_hint=(1, 1), background_normal='pp.jpg', font_size='11sp')
        self.button5 = Button(text='Network Stack', size_hint=(1, 1), background_normal='pp.jpg', font_size='11sp')
        self.button6 = Button(text='Haskel', size_hint=(1, 1), background_color=(0.5, 0, 0.5, 1), font_size='11sp')

        self.button1.bind(on_press=lambda instance: self.callback('https://youtu.be/tQGgGY8mTP0?list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i'))
        self.button2.bind(on_press=lambda instance: self.callback('https://youtu.be/F8kx56OZQhg?list=PLrOv9FMX8xJHqMvSGB_9G9nZZ_4IgteYf'))
        self.button3.bind(on_press=lambda instance: self.callback('https://youtu.be/zPYjfgxYO7k'))
        self.button4.bind(on_press=lambda instance: self.callback('https://youtu.be/gYRrGTC7GtA'))
        self.button5.bind(on_press=lambda instance: self.callback('https://youtu.be/_gWfFEuert8'))
        self.button6.bind(on_press=lambda instance: self.callback('https://youtu.be/Vgu82wiiZ90?list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV'))

        self.back_button = Button(text='Back', background_normal='', size_hint=(None, None), size=(100, 50),
                                  background_color=(0.2, 0.2, 0.2, 1), font_size='11sp')
        self.back_button.pos_hint = {'x': 0, 'top': 1}
        self.back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))


        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)
        layout.add_widget(self.button4)
        layout.add_widget(self.button5)
        layout.add_widget(self.button6)

        float_layout.add_widget(layout)
        float_layout.add_widget(self.back_button)

        self.add_widget(float_layout)


    def callback(self, url):
        wb.open(url)

class MyAdvanced(Screen):
    def __init__(self, **kwargs):
        super(MyAdvanced, self).__init__(**kwargs)
        float_layout = FloatLayout()
        layout = GridLayout(cols=2, rows=3, padding=20, spacing=10)

        self.button1 = Button(text='Virtual Machine', size_hint=(1,1), background_normal='rd.jpg', font_size='11sp')
        self.button2 = Button(text='Gamers Game', size_hint=(1, 1), background_color=(1, 0, 0, 1), font_size='11sp')
        self.button3 = Button(text='Operating System', size_hint=(1, 1), background_color=(1, 0, 0, 1), font_size='11sp')
        self.button4 = Button(text='Programming Language', size_hint=(1, 1), background_normal='rd.jpg', font_size='11sp')
        self.button5 = Button(text='Web Server', size_hint=(1, 1), background_normal='rd.jpg', font_size='11sp')
        self.button6 = Button(text='Voxel Engine', size_hint=(1, 1), background_color=(1, 0, 0, 1), font_size='11sp')

        self.button1.bind(on_press=lambda instance: self.callback('https://youtu.be/vymrj-2YD64'))
        self.button2.bind(on_press=lambda instance: self.callback('https://youtu.be/YXPyB4XeYLA'))
        self.button3.bind(on_press=lambda instance: self.callback('https://youtu.be/9t-SPC7Tczc?list=PLFjM7v6KGMpiH2G-kT781ByCNC_0pKpPN'))
        self.button4.bind(on_press=lambda instance: self.callback('https://youtu.be/Eythq9848Fg?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD'))
        self.button5.bind(on_press=lambda instance: self.callback('https://youtu.be/7GBlCinu9yg'))
        self.button6.bind(on_press=lambda instance: self.callback('https://youtu.be/Ab8TOSFfNp4'))


        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)
        layout.add_widget(self.button4)
        layout.add_widget(self.button5)
        layout.add_widget(self.button6)

        self.back_button = Button(text='Back', background_normal='', size_hint=(None, None), size=(100, 50),
                                  background_color=(0.2, 0.2, 0.2, 1), font_size='11sp')
        self.back_button.pos_hint = {'x': 0, 'top': 1}
        self.back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))

        float_layout.add_widget(layout)
        float_layout.add_widget(self.back_button)

        self.add_widget(float_layout)


    def callback(self, url):
        wb.open(url)

class MyApp(App):
    def build(self):
        screens_manager = ScreenManager()
        screens_manager.add_widget(MyMainWindow(name='main'))
        screens_manager.add_widget(MyBeginner(name='beginner'))
        screens_manager.add_widget(MyIntermediate(name='intermediate'))
        screens_manager.add_widget(MyAdvanced(name='advanced'))
        return screens_manager


MyApp().run()
   

