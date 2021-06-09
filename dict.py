# Import all required libraries
from PyDictionary import PyDictionary
from tkinter import *
# Create Objects
dictionary = PyDictionary()
win = Tk()
#Give Dimensions to ur window u can also enlarge ur window if not so then give its max and min size
win.geometry("700x400")
#Title of your window
win.title("Dictionary")
def dict():
	meaning.config(text=dictionary.meaning(word.get()))
	synonym.config(text=dictionary.synonym(word.get()))
	antonym.config(text=dictionary.antonym(word.get()))

# Add Labels, Button and Frames
Label(win, text="Dictionary", font=("Helvetica 20 bold"), fg="Green").pack(pady=10)

# Frame 1
frame = Frame(win)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(win)
Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

# Frame 3
frame2 = Frame(win)
Label(frame2, text="Synonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

# Frame 4
frame3 = Frame(win)
Label(frame3, text="Antonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(win, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()

# Execute Tkinter
win.mainloop()