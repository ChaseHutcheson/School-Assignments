from tkinter import *
import tkinter as tk
import pyttsx3

def clearText():
    textInput.delete(1.0, END)

def readText():
    engine=pyttsx3.init()
    engine.say(textInput.get(1.0, END))
    engine.runAndWait()

root = tk.Tk()

root.geometry("600x400")
root.title("Sekol TTS")

title = tk.Label(root, text="Input Text Here:", font=("Arial", 18))
title.pack(padx=0, pady=10)

v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

textInput = tk.Text(root, height=9, font=('Arial', 16), yscrollcommand=v.set)
textInput.pack(padx=10, pady=5)

read = tk.Button(root, text="Read", font=('Arial', 18), command=readText)
read.pack(padx=5, pady=5)

clear = tk.Button(root, text="Clear", font=('Arial', 18), command=clearText)
clear.pack(padx=5, pady=5)

root.mainloop()