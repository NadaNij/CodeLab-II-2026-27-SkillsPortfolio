from tkinter import *
def switch_to_frame(frame):
    frame.tkraise()


root = Tk()
root.config(bg="#FFFFFF")
root.title("Multiple Frames Example")
root.geometry('400x400')
label_title = Label(root, text="Working with multiple frames", font=('Roboto',18), bg='#FFFFFF',fg='#234567')
label_title.place(x=40, y=0)




import random, os

# Load the jokes once, at the start
jokes = []
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "randomJokes.txt")
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if "?" in line:
            setup, punchline = line.split("?", 1)   # split at the FIRST question mark only
            jokes.append((setup + "?", punchline))

current_punchline = ""

def tell_joke():
    global current_punchline
    setup, current_punchline = random.choice(jokes)

    punchline_label.config(text="")                           
    switch_to_frame(frame2)          # hide the old punchline

def show_punchline():
    punchline_label.config(text=current_punchline)

frame1 = Frame(root,bg="#9BC6F1")
Button(frame1, text="Alexa tell me a Joke", width=20, fg="#ffffff", bg="#345678",
       command=tell_joke).pack(pady=5)
setup_label = Label(frame1, text="", font=('Roboto',14), bg='#234567', fg='#ffffff', wraplength=360)
setup_label.pack(pady=5)

frame2 = Frame(root,bg="#9BC6F1")

Button(frame2, text="Show Punchline", width=20, fg="#ffffff", bg="#345678",
       command=show_punchline).pack(pady=5)


punchline_label = Label(frame1, text="", font=('Roboto',14), bg='#234567', fg='#ffffff', wraplength=360)
punchline_label.pack(pady=5)

Button(frame2, text="Next Joke", width=20, fg="#ffffff", bg="#345678",
       command=tell_joke).pack(pady=5)

Button(frame2, text="Quit", width=20, fg="#ffffff", bg="#345678",
       command=root.destroy).pack(pady=5)

frame1.place(x=0, y=50, width=400, height=350)
frame2.place(x=0, y=50, width=400, height=350)
switch_to_frame(frame1)

root.mainloop()