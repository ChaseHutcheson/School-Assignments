from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import datetime
import time

class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation = 'vertical')
        self.image = Image()
        layout.add_widget(self.image)
        self.save_image_button = MDRaisedButton(
            text='Translate',
            pos_hint={'center_x': .55, 'center_y': .5},
            size_hint = (None, None))
        self.save_image_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_image_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame 
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        image_name = datetime.datetime.now().strftime('%m-%d-%y, %H;%M;%S') + ".jpg"
        save_path = f"Images\\{image_name}"
        cv2.imwrite(save_path, self.image_frame)
        self.image = Image(source=f"Images\\{image_name}")

if __name__ == '__main__':
    MainApp().run()