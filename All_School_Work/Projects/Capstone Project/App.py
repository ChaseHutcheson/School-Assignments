from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.config import Config
import cv2
import datetime
import pytesseract
from PIL import Image as imunge

#School Computer Path: "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
#Laptop Path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


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
        self.layout.add_widget(self.save_image_button)

        self.new_image_button = MDRaisedButton(
            text = 'Back',
            pos_hint={'center_x': .75, 'center_y': .05},
            size_hint=(None, None))
        self.new_image_button.bind(on_press=self.new_picture)
        self.layout.add_widget(self.new_image_button)

        self.new_image_button.disabled = True
        self.capture = cv2.VideoCapture(0)
        self.camera = Clock.schedule_interval(self.load_video, 1.0/30.0)
        self.camera

        self.text_label = Label(text = "")
        self.layout.add_widget(self.text_label)
        return self.layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame 
        buffer = cv2.flip(frame, -1).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        image_name = datetime.datetime.now().strftime('%m-%d-%y, %H;%M;%S') + ".jpg"
        save_path = f"Images\\{image_name}"
        cv2.imwrite(save_path, cv2.flip(self.image_frame, 2))
        self.display_images = Image(source=f"Images\\{image_name}")
        self.save_image_button.disabled = True
        self.new_image_button.disabled = False
        pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
        untranslated_image = imunge.open(str(save_path))
        translated_text = pytesseract.image_to_string(untranslated_image)
        self.text_label.text = translated_text

    def new_picture(self, *args):
        self.layout.remove_widget(self.display_images)
        self.save_image_button.disabled = False
        self.new_image_button.disabled = True
        self.text_label.text = ""

if __name__ == '__main__':
    MainApp().run()