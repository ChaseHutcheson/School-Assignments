from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import datetime
import pytesseract as pyt


class MainApp(MDApp):

    def build(self):
        self.layout = MDFloatLayout()
        self.image = Image()
        self.layout.add_widget(self.image)
        self.save_image_button = MDRaisedButton(
            text='Translate',
            pos_hint={'center_x': .25, 'center_y': .05},
            size_hint = (None, None))
        self.save_image_button.bind(on_press=self.take_picture)
        self.new_image_button = MDRaisedButton(
            text = 'Back',
            pos_hint={'center_x': .75, 'center_y': .05},
            size_hint=(None, None))
        self.new_image_button.bind(on_press=self.new_picture)
        self.layout.add_widget(self.save_image_button)
        self.layout.add_widget(self.new_image_button)
        self.new_image_button.disabled = True
        self.capture = cv2.VideoCapture(0)
        self.camera = Clock.schedule_interval(self.load_video, 1.0/30.0)
        self.camera
        return self.layout

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
        self.display_images = Image(source=f"Images\\{image_name}")
        self.layout.add_widget(self.display_images)
        self.save_image_button.disabled = True
        self.new_image_button.disabled = False
        translate_img = cv2.imread(self.display_images)
        pyt.pytesseract.tesseract_cmd = "C:\\Users\\hutcheson_chase\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        translated_text = pyt.image_to_string(translate_img)
        text_label = Label(text = translated_text)
        self.layout.add_widget(text_label)

    def new_picture(self, *args):
        self.layout.remove_widget(self.display_images)
        self.save_image_button.disabled = False
        self.new_image_button.disabled = True

if __name__ == '__main__':
    MainApp().run()