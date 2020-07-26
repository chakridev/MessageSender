import requests
import json
from tkinter import * #GUI interface
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'API authorization key',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk() #mainwindow GUI is TK
root.title("Message Sender ") #title for window
root.geometry("400x550") #window height and width
font = ("Helvetica", 22, "bold") #font 
textNumber = Entry(root, font=font)#text number field rooting the font
textNumber.pack(fill=X, pady=20)#padding textnumber
textMsg = Text(root)#text is under root
textMsg.pack(fill=X)#text msg padding
sendBtn = Button(root, text="SEND SMS", command=btn_click)#button
sendBtn.pack()
root.mainloop()#to display