from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.config import Config
import cv2
import datetime
import pytesseract
from PIL import Image as imunge
from kivy.lang.builder import Builder

#School Computer Path: "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
#Laptop Path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Builder.load_file(r'BadCSS.kv')

class Float(Screen):
    def build(self):
        pass

class MainApp(App):
    def build(self):
        self.Webcam = Image(size_hint = (1, .8))
        

        self.capture = cv2.VideoCapture(0)
        self.camera = Clock.schedule_interval(self.load_video, 1.0/30.0)
        self.camera

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame 
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.Webcam.texture = texture

        return Float()

if __name__ == "__main__":
    MainApp().run()