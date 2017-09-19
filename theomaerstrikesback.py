<<<<<<< HEAD
import tkinter as tk
import winsound
from tkinter import messagebox as msgbox

window = tk.Tk()
window.wm_withdraw()
box = msgbox.Message()

Kenshiro = "omae wa mou shindeiru"
answer = u'no'
while answer == u'no':
    for word in Kenshiro.split():
        msgbox.showinfo("FIST OF THE NORTH STAR", word)

    OtherDudeWhosHeadExplode = "Nani?!!?!?!?!?!?!?!?!"

    msgbox.showinfo("FIST OF THE NORTH STAR", OtherDudeWhosHeadExplode)

    msgbox.showinfo("FIST OF THE NORTH STAR", "Screeching sound")

    winsound.Beep(1000, 1000)

    answer = msgbox.askquestion("FIST OF THE NORTH STAR", "Did head explode?")
=======
import tkinter as TK
import winsound
from tkinter import messagebox
from tkinter import dialog

window = TK.Tk()
window.wm_withdraw()
box = messagebox.Message()

Kenshiro = "omae wa mou shindeiru"
answer = u'no'
while answer == u'no':
    for word in Kenshiro.split():
        messagebox.showinfo("FIST OF THE NORTH STAR",word)

    OtherDudeWhosHeadExplode = "Nani?!!?!?!?!?!?!?!?!"

    messagebox.showinfo("FIST OF THE NORTH STAR",OtherDudeWhosHeadExplode)

    messagebox.showinfo("FIST OF THE NORTH STAR","Screeching sound")

    winsound.Beep(1000,1000)

    answer = messagebox.askquestion("FIST OF THE NORTH STAR","Did head explode?")
>>>>>>> 0d0c0b1c3381e2c59363aafe8f6dbc0637dbc2de
