from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFloatingActionButton, MDRaisedButton
# from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
# from Helper import screen_helper
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.floatlayout import MDFloatLayout
# from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
# from kivymd.toast import toast
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import time
import numpy as np
import keras
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os
import glob
import shutil

screen_helper = """

ScreenManager:
    MenuScreen:
    MDNavigationLayout:
    TomatoScreen:
    CottonScreen:
    RiceScreen:
    WheetScreen:
    #FileChooser:
    ModelScreen:
    CameraScreen:

<MenuScreen>:
    name: "Menu"
    MDRaisedButton:
        text: "Tomato"
        pos_hint:{"center_x":0.5,"center_y":0.2}
        on_press: root.manager.current = "Tomato"
    MDRaisedButton:
        text: "Cotton"
        pos_hint:{"center_x":0.5,"center_y":0.4}
        on_press: root.manager.current = "Cotton"
    MDRaisedButton:
        text: "Rice"
        pos_hint:{"center_x":0.5,"center_y":0.6}
        on_press: root.manager.current = "Rice"
    MDRaisedButton:
        text: "Wheat"
        pos_hint:{"center_x":0.5,"center_y":0.8}
        on_press: root.manager.current = "Wheet"
    MDNavigationLayout:

<MDNavigationLayout>:
    name: "navigation_layout"
    ScreenManager:

        Screen:

            BoxLayout:
                orientation: 'vertical'

                MDToolbar:
                    title: "AgroApp"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    on_action_button: app.callback(self.icon)

                Widget:


    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"

            Image:
                id:avatar
                size_hint: (1,1)
                source: "IMG_20201231_220705164.jpg"

            MDLabel:
                text: "PVS Karthik"
                halign: "center"
                font_style: "Subtitle1"
                size_hint_y: 0.10

            MDLabel:
                text: "email: karthikpoluri962gmail.com"
                halign: "center"
                font_style: "Subtitle1"
                size_hint_y: 0.10


            ScrollView:
                DrawerList:
                    id: md_list

                    MDList:
                        OneLineIconListItem:
                            text: "Profile"

                            IconLeftWidget:
                                icon: "face-profile"



                        OneLineIconListItem:
                            text: "Upload"

                            IconLeftWidget:
                                icon: "upload"


                        OneLineIconListItem:
                            text: "Logout"

                            IconLeftWidget:
                                icon: "logout"


<TomatoScreen>:
    name: "Tomato"
    MDRaisedButton:
        text: "Upload"
        pos_hint:{"center_x":0.5,"center_y":0.75}
        on_release: root.manager.current = "model_screen"
    MDRaisedButton:
        text: "Camera"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_release: root.manager.current = "camera_screen"
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
    MDNavigationLayout:
<CottonScreen>:
    name: "Cotton"
    MDRaisedButton:
        text: "Upload"
        pos_hint:{"center_x":0.5,"center_y":0.75}
        on_release: root.manager.current = "model_screen"
    MDRaisedButton:
        text: "Camera"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_release: root.manager.current = "camera_screen"
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
    MDNavigationLayout:
<RiceScreen>:
    name:"Rice"
    MDRaisedButton:
        text: "Upload"
        pos_hint:{"center_x":0.5,"center_y":0.75}
        on_release: root.manager.current = "model_screen"
    MDRaisedButton:
        text: "Camera"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_release: root.manager.current = "camera_screen"
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
    MDNavigationLayout:
<WheetScreen>:
    name: "Wheet"
    MDRaisedButton:
        text: "Upload"
        pos_hint:{"center_x":0.5,"center_y":0.75}
        on_release: root.manager.current = "model_screen"
    MDRaisedButton:
        text: "Camera"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_release: root.manager.current = "camera_screen"
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
    MDNavigationLayout:
<CameraScreen>:
    name: "camera_screen"
    CameraLayout:
    MDNavigationLayout:
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
<CameraLayout>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (224, 224)
        play: False
    MDFloatingActionButton:
        text: 'Play'
        icon: "play"
        pos_hint:{"center_x":0.5,"center_y":0.75}  
        on_press: camera.play = not camera.play
    MDFloatingActionButton:
        text: 'Capture'
        icon: "camera"
        pos_hint:{"center_x":0.5,"center_y":0.5}  
        on_press: root.capture()
    MDFloatingActionButton:
        text: 'Predict'
        icon: "camera"
        pos_hint:{"center_x":0.5,"center_y":0.25}  
        on_press: root.predicting_captured_image()

<ModelScreen>:
    name : "model_screen"
    ModelLayout:
    MDNavigationLayout:
    MDFloatingActionButton:
        text: "back"
        icon: "arrow-collapse-left"
        pos_hint:{"center_x":0.9,"center_y":0.1}
        on_release: root.manager.current = "Menu"
<ModelLayout>:
    id:model_layout
    MDBoxLayout:
        orientation: "vertical"
        size: root.width,root.height

        padding:25
        spacing:25

        Image:
            id: my_image
            source: ""

        FileChooserIconView
            id:filechooser
            on_selection: model_layout.selected(filechooser.selection)


        MDRaisedButton:
            text: "submit"
            pos_hint:{"center_x":0.5,"center_y":0}     
            on_press: root.predicting_uploaded_image()


"""
Window.size = (400, 600)


class MenuScreen(Screen):
    pass


class MDNavigationLayout(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class TomatoScreen(Screen):
    pass


class CottonScreen(Screen):
    pass


class RiceScreen(Screen):
    pass


class WheetScreen(Screen):
    pass


class ModelScreen(Screen):
    pass


class ModelLayout(MDBoxLayout):
    def selected(self, filename):
        try:
            self.filename = filename
            self.ids.my_image.source = self.filename[0]
            self.path = self.ids.my_image.source = self.filename[0]
            string = filename[0]
            print(string)
            src_dir = string
            dst_dir = "C:\\Users\\P V S Karthik\\PycharmProjects\\Agriculture_AI_App\\Uploaded images\\"
            for file in glob.iglob(src_dir):
                shutil.copy(file, dst_dir)
            print("Copied to Uploaded images folder")
        except:
            pass

    def predict_leaf(self, path, model):
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            print(img_path)
        print()
        print(img_path)
        img_path = load_img(img_path, target_size=(224, 224))
        image = img_path
        img_array = np.expand_dims(image, axis=0)
        image = preprocess_input(img_array)
        prediction = np.round(model.predict(image))
        return prediction

    def predicting_uploaded_image(self):
        model_path = "Tomato_leaf_disease_ditection_01.model"
        model = keras.models.load_model(model_path)
        path = "C:\\Users\\P V S Karthik\\PycharmProjects\\Agriculture_AI_App\\Uploaded images\\"
        predictions = self.predict_leaf(path, model)
        print(predictions)
        back_button = MDFlatButton(text="Back", pos_hint={"center_x": 0.5, "center_y": 0.25},
                                   on_press=self.close_dialog)
        if predictions[0,1] == 1:
            self.dialog = MDDialog(title='Your Prediction',
                                   text="Detected disease is {}".format("Tomato___Bacterial_spot"), size_hint=(0.9, 1),
                                   buttons=[back_button])
            self.dialog.open()
        elif predictions[0, 0] == 0:
            self.dialog = MDDialog(title='Your Prediction', text="Please enter the correct image",
                                   size_hint=(0.9, 1), buttons=[back_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class CameraScreen(Screen):
    pass


class CameraLayout(MDBoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        path = "C:\\Users\\P V S Karthik\\PycharmProjects\\Agriculture_AI_App\\Captured_images\\"
        camera.export_to_png(path + "IMG_{}.png".format(timestr))
        print("Captured")

    def predict_leaf(self, path, model):
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
        image = load_img(img_path, target_size=(224, 224))
        # image  = img_path
        img_array = np.expand_dims(image, axis=0)
        image = preprocess_input(img_array)
        prediction = np.round(model.predict(image))
        return prediction

    def predicting_captured_image(self):
        model_path = "Tomato_leaf_disease_ditection_01.model"
        model = keras.models.load_model(model_path)
        path = "C:\\Users\\P V S Karthik\\PycharmProjects\\Agriculture_AI_App\\Captured_images\\"
        predictions = self.predict_leaf(path, model)
        back_button = MDFlatButton(text="Back", pos_hint={"center_x": 0.5, "center_y": 0.25},
                                   on_press=self.close_dialog)
        if predictions[:0] == 1.0:
            self.dialog = MDDialog(title='Your Prediction',
                                   text="Detected disease is {}".format("Tomato___Bacterial_spot"), size_hint=(0.9, 1),
                                   buttons=[back_button])
            self.dialog.open()
        else:
            self.dialog = MDDialog(title='Your Prediction', text="Please enter the correct image",
                                   size_hint=(0.9, 1), buttons=[back_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


sm = ScreenManager()
sm.add_widget(MenuScreen(name="Menu"))
sm.add_widget(TomatoScreen(name="Tomato"))
sm.add_widget(CottonScreen(name="Cotton"))
sm.add_widget(RiceScreen(name="Rice"))
sm.add_widget(WheetScreen(name="Wheet"))
sm.add_widget(ModelScreen(name="model_screen"))
sm.add_widget(CameraScreen(name="camera_screen"))
sm.add_widget(MDNavigationLayout(name="navigation_layout"))


class Trial_01(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(screen_helper)
        return screen


Trial_01().run()
