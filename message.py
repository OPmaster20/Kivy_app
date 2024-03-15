
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

texts = Label(text='No any input! ')
popup = Popup(title='Warning', content=texts)
popup.size_hint = (.2,.20)
popup.auto_dismiss = True
def mess1(code):
    global texts,popup
    if code == 1:
        popup.content = texts
    elif code == 2:
        texts.text = 'Username is NULL! '
        popup.content = texts
    elif code == 3:
        texts.text = 'Password is NULL! '
        popup.content = texts
    elif code == 4:
        texts.text = 'Verification code error'
        popup.content = texts
        popup.size_hint = (.3,.20)
    elif code == 5:
        texts.text = 'Verification code is NULL'
        popup.content = texts
        popup.size_hint = (.3,.20)
    elif code == 6:
        texts.text = 'Database connection failed'
        popup.content = texts
        popup.size_hint = (.3, .20)
    elif code == 7:
        texts.text = 'Email is empty'
        popup.content = texts
        popup.size_hint = (.3, .20)
    elif code == 8:
        texts.text = "Account does not exist"
        popup.content = texts
        popup.size_hint = (.5, .20)
    popup.open()

def mess2(code):
    global texts,popup
    if code == 1:
        texts.text = "Verification code is incorrect"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 2:
        texts.text = "Passwords are inconsistent"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 3:
        texts.text = "Length cannot exceed 15"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 4:
        texts.text = "There is a problem with the email format"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 5:
        texts.text = "Text is NULL"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 6:
        texts.text = "No music to play"
        popup.content = texts
        popup.size_hint = (.5, .20)
    elif code == 7:
        texts.text = "Password format is wrong"
        popup.content = texts
        popup.size_hint = (.5, .20)

    popup.open()
def work1(code):
    global texts,popup
    if code == 1:
        texts.text = "Verification code is correct"
        popup.content = texts
        popup.size_hint = (.5, .20)

    elif code == 2:
        texts.text = "sign in successfully"
        popup.content = texts
        popup.size_hint = (.3, .20)
    elif code == 3:
        texts.text = "exit successfully"
        popup.content = texts
        popup.size_hint = (.3, .20)

    popup.open()

