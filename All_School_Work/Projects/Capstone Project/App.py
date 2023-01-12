from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix import image
import 

class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation = 'vertical')
        self.image = image()
        layout.add_widget(self.image)
        layout.add_widget(MDRaisedButton(
            text='Take A Picture',
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint = (None, None))
        )
        self.capture = cv2
        return layout

if __name__ == '__main__':
    MainApp().run()