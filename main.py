from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.progressbar import ProgressBar
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import TextInput
import time
from kivy.lang import Builder
import qrcode
import os
from PIL import Image
from user import screen_helper

x = ""


class MainScreen(Screen):
    def getbackenddata(self):
        backenddata = self.ids.inputdata.text
        print(backenddata)
        global x
        x = backenddata


class QRSaveScreen(Screen):

    def reset_changes(self):
        self.ids.filename.helper_text = ""
        self.ids.filename.helper_text_mode = "on_focus"
        self.ids.filename.opacity = 1
        self.ids.extension.opacity = 1
        self.ids.savebutton.disabled = False
        self.ids.backbutton.disabled = False
        self.ids.backbutton.opacity = 1
        self.ids.savebutton.opacity = 1
        self.ids.pb.opacity = 0
        self.ids.pb.value = 0
        self.ids.donebutton.opacity = 0
        self.ids.donebutton.disabled = True
        self.ids.statusLabel.text = ""
        self.ids.filename.text = ""
        self.ids.extension.text = ""

    def getfilename(self):
        name = self.ids.filename.text
        ext = str(self.ids.extension.text)
        if ext.startswith('.'):
            ext = ext[1:]
        files = [f for f in os.listdir(".") if os.path.isfile(f)]
        ext = ext.lower()
        if ext == 'png' or ext == 'jpg' or ext == 'jpeg':
            final = name + "." + ext
        else:
            final = name + ".png"
        print(final)
        if final in files:
            self.ids.filename.helper_text = "File Name already exist"
            self.ids.filename.helper_text_mode = "persistent"
        else:
            self.ids.filename.helper_text = "Saving"
            self.ids.filename.helper_text_mode = "persistent"
            self.ids.savebutton.disabled = True
            self.ids.backbutton.disabled = True
            self.ids.backbutton.opacity = 0
            self.ids.savebutton.opacity = 0
            self.ids.filename.opacity = 0
            self.ids.extension.opacity = 0
            self.ids.pb.opacity = 1
            time.sleep(2)
            file_path = QRSaveScreen.store_data(final)
            time.sleep(1)
            if file_path:
                self.ids.pb.value = 100
                self.ids.donebutton.opacity = 1
                self.ids.donebutton.disabled = False
                self.ids.statusLabel.text = "QR Generated in " + file_path

    def store_data(arg):
        global x
        backend_data = x
        print(backend_data)
        filename = arg
        print(filename)
        x = filename
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        # for key in data:
        #    qr.add_data(data[key])
        #    qr.add_data("\n")
        qr.add_data(backend_data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', backcolor='white')

        # fileName = input()
        # Save_as = input()
        # FileName = fileName + '.' + Save_as
        # qr_image = qrcode.make('Poda sotta!!!')
        qr_image.save(filename)
        print(os.getcwd())
        path = os.getcwd()
        files = [f for f in os.listdir(".") if os.path.isfile(f)]
        print(files)
        f1 = 0
        while (f1 == 0):
            if filename in files:
                f1 = 1
        return path


class ResultScreen(Screen):
    pass

    # savedbackenddata = MainScreen.getinput
    # savedfilename = QRSaveScreen.getfilename
    # print("FileName: ", savedfilename)
    # print("Backend Data: ", savedbackenddata)


sm = ScreenManager()
sm.add_widget(MainScreen(name='menu'))
sm.add_widget(QRSaveScreen(name='savescreen'))
sm.add_widget(ResultScreen(name='final'))


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        # self.inputdata = Builder.load_string(user.username_input)
        # self.inputdata = TextInput(multiline=False)
        # screen.add_widget(self.inputdata)
        # Button = button.MDRectangleFlatButton(text='Generate',
        #                               pos_hint={'center_x': 0.5, 'center_y': 0.4},
        #                               on_release=self.store_data)
        # screen.add_widget(self.inputdata)
        # screen.add_widget(Button)
        return screen


if __name__ == '__main__':
    app = MainApp()
    app.run()
