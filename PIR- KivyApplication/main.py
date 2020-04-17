
"""This code will create UI and prompted with open camera option. After capturing produce item image, it will predict the  item. 
Af of now supported produce items are listed below wirth the labels being used 
{
  "Apple": 0,
  "Avocado": 1,
  "Banana": 2,
  "Blueberry": 3,
  "Brocolli": 4,
  "Cabbage": 5,
  "Canada Pear": 6,
  "Carrot": 7,
  "Garlic": 8,
  "Green Peas": 9,
  "Green Pepper": 10,
  "Lettuce": 11,
  "Mangoes": 12,
  "Okra": 13,
  "Orange": 14,
  "Pineapple": 15,
  "Red Chilli": 16,
  "Red Onions": 17,
  "Spinach": 18,
  "Spring Onion": 19,
  "Tomato": 20,
  "Yellow Onion": 21,
  "Yellow Potato": 22,
  "bell pepper": 23
}

We have a seperate labels.txt file for future maintainace where we need to be keep udating our produce items"""


"""Import all the required libraries"""
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import time
import numpy as np
from glob import glob
from keras.models import load_model
from keras.preprocessing import image
from keras.models import Model
from kivy.utils import platform
import time
import json


"""Layout with open camera and capture image buttons"""

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (600, 500)
        play: False
       
    
    ToggleButton:
        text: 'Open Camera'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
        
        background_color: (1, .3, .4, .85)
    Button:
        text: 'Capture Produce'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
        background_color: (1, .3, .4, .85)
        
''')


class CameraClick(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._request_android_permissions()
        self.label1=""


    @staticmethod
    def is_android():
        return platform == 'android'

    def _request_android_permissions(self):
        """
        Requests CAMERA permission on Android.
        """
        if not self.is_android():
            return
        from android.permissions import request_permission, Permission
        request_permission(Permission.CAMERA)



    def capture(self):
        '''
        Function to capture the images and give maintain same name such that it overwrite previously captured image
       
        '''
        
        camera = self.ids['camera']
        camera.export_to_png("image/IMG.png")
        print("Captured")
        self.ids['camera'].play = False
        self.predict()

    def predict(self):

        """This method is to load label files and image captured, and finally predict the captured image"""

       #Image labels and calling predict function for running inference
        
        with open('labels.txt') as json_file:
            test_gen_class_indices= json.load(json_file)    

        model = load_model('vgg16_11.h5')
        image_path = "image/IMG.png"
        img = image.load_img(image_path, target_size=(100, 100))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])

        predict_result = {}
        classes = model.predict(images)
        a = classes.tolist()

        for i in a[0]:
            if i > 0.002:
                pos = a[0].index(i)
                val = i
                for label in test_gen_class_indices.keys():
                    if test_gen_class_indices[label] == pos:
                        predict_result[label] = val
        final_res = {}

        for key in predict_result.keys():
            final_res[key] = predict_result[key] * 100
            print('%s (%.2f%%)' % (key, predict_result[key] * 100))
            final_res_output=str('%s (%.2f%%)' % (key, predict_result[key] * 100))

        if self.label1!="":
             self.remove_widget(self.label1)

        #Return the predicted result to a label added on the fly
        self.label1=Label(text_size=(500, None), text='The captured image is predicted to be ' + str(final_res_output), line_height=1.5,
                            pos_hint={'center_x': 0.5, 'center_y': .85},
                            size_hint=(None, None),
                            halign="center")
        self.add_widget(self.label1)
       
        final_res_output={}
            
            

class TestCamera(App):

    def build(self):
        self.title = 'Farm Produce Recognition'
        return CameraClick()


TestCamera().run()