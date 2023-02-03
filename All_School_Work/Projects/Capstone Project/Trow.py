from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config
import cv2
import datetime
import pytesseract
from PIL import Image as imunge

#School Computer Path: "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
#Laptop Path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Builder.load_file('BasicallyCSS.kv')

class TheFloatLayout(Widget):
    pass


class MainApp(MDApp):
    def build(self):
        return TheFloatLayout()

if __name__ == '__main__':
    MainApp().run()