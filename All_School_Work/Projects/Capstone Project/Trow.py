from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import kivy.core.text
import cv2
from kivy.app import App
from kivy.base import EventLoop
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
import datetime
import pytesseract
from PIL import Image as imunge

#School Computer Path: "C:\\Users\\hutcheson_chase\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe"
#Laptop Path: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Builder.load_file('BadCSS.kv')

class Kamera(Image):
    def __init__(self, **kwargs):
        super(Kamera, self).__init__(**kwargs)
        self.capture = capture

    def update(self, dt):
        return_value, frame = self.capture.read()
        if return_value:
            texture = self.texture
            w, h = frame.shape[1], frame.shape[0]
            if not texture or texture.width != w or texture.height != h:
                self.texture = texture = Texture.create(size=(w, h))
                texture.flip_vertical()
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.canvas.ask_update()


capture = cv2.VideoCapture(0)

class MyFloat(FloatLayout):
    def __init__(self):
        #Camera Image Widget
        global capture
        self.image = self.ids.camera_display

        #Button That takes a picture
        self.save_image_button = self.ids.image_save_button

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
        Window.clearcolor = (0, 0, 0, 1)
        MyFloat.__init__()
        return MyFloat()

if __name__ == '__main__':
    MainApp().run()