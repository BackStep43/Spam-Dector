import tkinter
from tkinter import *
from tkinter import messagebox
from pathlib import Path
import tkinter as tk
import pandas as pd
import re, math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def chcekspam(message):
    data = pd.read_csv("spam.csv", delimiter=",", encoding="latin-1")
    data = data[["Label", "message"]]
    data.head()
    classifier = MultinomialNB()
    vectorizer = CountVectorizer()
    vectorize_message = vectorizer.fit_transform(data['message'].values)
    targets = data['Label'].values
    classifier.fit(vectorize_message, targets)
    examples = [message]
    example_counts = vectorizer.transform(examples)
    predictions = classifier.predict(example_counts)
    print(predictions)
    chcek = ""
    for i in predictions:
        chcek = i
    if chcek == "spam":
        messagebox.showinfo(title="alert", message="Meassage is spam!!")
    else:
        messagebox.showinfo(title="alert", message="Meassage is ham!!")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    393.0,
    324.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FDFAFA",
    highlightthickness=0
)
entry_1.place(
    x=122.0,
    y=222.0,
    width=542.0,
    height=203.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: chcekspam(entry_1.get()),
    relief="flat"
)
button_1.place(
    x=581.0,
    y=464.0,
    width=101.0,
    height=41.0
)

canvas.create_text(
    112.0,
    186.0,
    anchor="nw",
    text="Enter your message",
    fill="#000000",
    font=("Roboto", 20 * -1)
)

canvas.create_text(
    213.0,
    446.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
