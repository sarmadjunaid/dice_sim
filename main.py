import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry('400x400')
root.title('Rool the Dice')

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="Hello from Dicer!", fg="light green", bg="dark green", font="Helvetica 16 bold italic")
HeadingLabel.pack()

dice = ['die1.PNG', 'die2.PNG', 'die3.PNG', 'die4.PNG', 'die5.PNG', 'die6.PNG']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack(expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text="Roll the Dice", fg="blue", command=rolling_dice)
button.pack(expand = True)

root.mainloop()