screen_helper = '''
ScreenManager:
    MainScreen:
    QRSaveScreen:
    ResultScreen:

<MainScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Generate'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:
            #it checks whether inputdata is not NULL, If not null then it goes to savescreen
            root.manager.current = 'savescreen' if inputdata.text != '' else None
            inputdata.text=''
        on_press: root.getbackenddata()
    MDTextField:
        id: inputdata
        hint_text: "Enter the data"
        required: True
        helper_text_mode: "on_focus"
        helper_text: "This field is required"
        icon_right: "email"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300

<QRSaveScreen>:
    name: 'savescreen'
    #While leaving the screen the changes are resetted
    on_leave: root.reset_changes()
    
    MDRectangleFlatButton:
        id: backbutton
        text: 'Back'
        pos_hint: {'center_x':0.4,'center_y':0.3}
        opacity: 1
        disabled: False
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        id: savebutton
        text: 'Save'
        pos_hint: {'center_x':0.6,'center_y':0.3}
        opacity: 1
        disabled: False
        on_press: root.getfilename()
    MDRectangleFlatButton:
        id: donebutton
        text: 'Done'
        pos_hint: {'center_x':0.5,'center_y':0.25}
        opacity: 0
        on_press: root.manager.current = 'final'
        disabled: True
    
    MDTextField:
        id: filename
        hint_text: "Filename"
        helper_text_mode: "on_focus"
        helper_text: ""
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        opacity: 1
        width:300
    MDTextField:
        id: extension
        hint_text: "Format"
        helper_text: "png,jpg,jpeg"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        opacity: 1
        width:300
    ProgressBar: 
        id: pb
        value: 25
        min: 0
        max: 100
        opacity: 0
        pos_hint: {'x':.1,'y':0.1} 
        size_hint_x: .8
    MDLabel:
        id: statusLabel
        text: ""
        halign: "center"
        valgin: 'top'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

<ResultScreen>:
    name: 'final'
    MDRectangleFlatButton:
        text: 'Create New QR'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.25,0.125)
        on_press: root.manager.current = 'menu'
'''