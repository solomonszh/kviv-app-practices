from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Selfie(App):
    def make(self):
        self.ob_camera = Camera()
        self.obj_camera.resolution = (8110, 810)
        obj_button = Button(text="Click !!")
        obj_button.size_hint = (0.6, 0.3)
        obj_button.pos_hint = {"x":0.35, "y":35}
        obj_button.bind(on_press = self.selfie_take())
        obj_layout = BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
    
    def selfie_take(self):
        print("Selfies has been taken successfully")
        self.obj_camera.export_to_png("selfie.png")

if __name__ == "__main__":
    Selfie().run()