from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MainScreen>:
    FloatLayout:
        padding: 50
        spacing: 50
        Label:
            font_size:"25sp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            text: 'Вкусняхи для общаги'
    
    
        Button:
            size_hint: 0.5, 0.2
            pos_hint:{'center_x':0.5, 'center_y':0.5}
            text: 'К готовке!'
            on_press: root.manager.current = 'ingredients'
            
            
<Ingredients>:
    FloatLayout:
        padding: 50
        spacing: 50
        Label:
            font_size:"20sp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            text_size: root.width, None
            size: self.texture_size
            halign: 'center'
            text: 'Выберите ингредиенты для будущего блюда'
            
    
    
        Button:
            size_hint: 0.5, 0.2
            pos_hint:{'center_x':0.5, 'center_y':0.5}
            text: 'К готовке!'    
            on_press: root.manager.current = 'main'
""")


class MainScreen(Screen):
    pass


class Ingredients(Screen):
    pass


class MyApp(App):
    running = True

    def on_stop(self):
        self.running = False

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Ingredients(name='ingredients'))
        return sm


MyApp().run()
input()
