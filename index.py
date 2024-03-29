from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.uix.image import Image
import os
from datetime import datetime

class AttendanceApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(TakeAttendanceScreen(name='take_attendance'))
        self.sm.add_widget(AttendanceSheetScreen(name='attendance_sheet'))

        self.menu = MenuScreen(name='menu')
        self.sm.add_widget(self.menu)
        
        return self.sm

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(layout)
        
        label = Label(text="Menu", size_hint_y=None, height=50)
        layout.add_widget(label)
        
        home_button = Button(text="Home", size_hint=(None, None), size=(150, 50))
        home_button.bind(on_press=self.go_to_home)
        layout.add_widget(home_button)
        
        take_attendance_button = Button(text="Take Attendance", size_hint=(None, None), size=(150, 50))
        take_attendance_button.bind(on_press=self.go_to_take_attendance)
        layout.add_widget(take_attendance_button)

    def go_to_home(self, instance):
        self.manager.current = 'home'
    
    def go_to_take_attendance(self, instance):
        self.manager.current = 'take_attendance'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(layout)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        label = Label(text="Home Screen", size_hint_y=None, height=50)
        layout.add_widget(label)
        
        button = Button(text="Take Attendance", size_hint=(None, None), size=(150, 50))
        button.bind(on_press=self.go_to_take_attendance)
        layout.add_widget(button)

    def go_to_take_attendance(self, instance):
        self.manager.current = 'take_attendance'

class TakeAttendanceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(layout)
        
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=True)
        layout.add_widget(self.background)
        
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)
        
        self.capture_button = Button(text="Capture", size_hint=(None, None), size=(150, 50))
        self.capture_button.bind(on_press=self.capture)
        layout.add_widget(self.capture_button)

    def capture(self, instance):
       now = datetime.now()
       dt_string = now.strftime("%Y%m%d_%H%M%S")
       filename = f"captured_image_{dt_string}.png"
       folder_path='Dataset'
       filepath = os.path.join(folder_path, filename)
       self.camera.export_to_png(filepath)
       print(f"Image captured and saved as '{filename}'")

class AttendanceSheetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        self.add_widget(Label(text="Attendance Sheet Screen"))

if __name__ == '__main__':
    AttendanceApp().run()
