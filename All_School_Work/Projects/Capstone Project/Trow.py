from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import datetime
import pytesseract
from PIL import Image as imunge

#School Computer Path: "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
#Laptop Path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Builder.load_file('BadCSS.kv')

class MyFloat(FloatLayout):
        def builf(self):

            #Defines Layout

            #Camera Image Widget

            #Button That takes a picture
            # self.save_image_button = ma.ids['image_save_button']

            #Button that lets you return from taking a picture

            #Back button starts disables

            #OpenCV Camera capture
            # self.capture = cv2.VideoCapture(0)

            #Camera updating
            # self.camera = Clock.schedule_interval(self.load_video, 1.0/30.0)
            # self.camera
            pass


        def load_video(self, *args):
            # ret, frame = self.capture.read()
            # self.image_frame = frame 
            # buffer = cv2.flip(frame, 0).tobytes()
            # texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            # texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            # self.image.texture = texture
            pass

        def take_picture(self, *args):
            # #Makes an image name
            # image_name = datetime.datetime.now().strftime('%m-%d-%y, %H;%M;%S') + ".jpg"
            
            # #Saves it to image folder
            # save_path = f"Images\\{image_name}"
            # cv2.imwrite(save_path, cv2.flip(self.image_frame, 2))
            

            # pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
            # untranslated_image = imunge.open(str(save_path))
            # translated_text = pytesseract.image_to_string(untranslated_image)
            pass

        def new_picture(self, *args):
            pass

class MainApp(App):
    def build(self):
        return MyFloat()

if __name__ == '__main__':
    MainApp().run()