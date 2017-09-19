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