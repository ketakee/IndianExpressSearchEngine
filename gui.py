# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:04:46 2016

@author: Ketakee Nimavat
"""
import tkinter 
import webbrowser

def callback(event):
    webbrowser.open_new(r"http://www.google.com")

root = Tk()
link = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()
