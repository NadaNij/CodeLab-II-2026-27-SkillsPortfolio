from tkinter import *
def switch_to_frame(frame):
    frame.tkraise()


root = Tk()
root.config(bg="#FFFFFF")
root.title("Multiple Frames Example")
root.geometry('400x400')
label_title = Label(root, text="Working with multiple frames", font=('Roboto',18), bg='#FFFFFF',fg='#234567')
label_title.place(x=40, y=0)

import random
Total_Questions=10
level=""
question_number=0
score=0
correct_answer=0
attempt=1

def randomInt(level):
    if level=="Easy":
        return random.randint(1,9)
    elif level=="Medium":
            return random.randint(10,99)
    else:
            return random.randint(1000,9999)

def decideOperation():
      return random.choice(['+','-'])

def start_quiz(chosen_level, colour):
    global level, question_number, score
    level = chosen_level
    question_number = 0
    score = 0
    for w in (frame_quiz, progress_label, question_label, feedback_label):
        w.config(bg=colour)
    switch_to_frame(frame_quiz)
    displayProblem() #check

def displayProblem():
    global question_number, correct_answer
    if question_number == Total_Questions:
        displayResults()
        return
    question_number += 1
    num1 = randomInt(level)
    num2 = randomInt(level)
    op = decideOperation()
    correct_answer = num1 + num2 if op == '+' else num1 - num2
    progress_label.config(text=f"Question {question_number} of {Total_Questions}")
    question_label.config(text=f"What is {num1} {op} {num2}?")
    answer_entry.delete(0, END)
    feedback_label.config(text="")
    submit_button.config(state=NORMAL)

def isCorrect():
    global score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Please enter a whole number")
        return
    submit_button.config(state=DISABLED)
    if user_answer == correct_answer:
        score += 10
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(text=f"Wrong, the answer was {correct_answer}")
    root.after(1200, displayProblem)
def displayResults():
    if score > 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    results_label.config(text=f"Score: {score} / 100\nGrade: {grade}")
    switch_to_frame(frame_results)
# Create Frame 1
frame1 = Frame(root,bg="#234567")

label1 = Label(frame1, text="Pick a mode for questions", font=('Roboto',16),bg= '#234567', fg='#ffffff')
label1.pack(pady=5)
Button(frame1, text="Easy", width=20, fg="#ffffff", bg="#345678",
       command=lambda: start_quiz("Easy", "green")).pack(pady=10)
Button(frame1, text="Medium", width=20, fg="#ffffff", bg="#345678",
       command=lambda: start_quiz("Medium", "orange")).pack(pady=10)
Button(frame1, text="Hard ", width=20, fg="#ffffff", bg="#345678",
       command=lambda: start_quiz("Hard", "red")).pack(pady=10)
frame1.place(x=0, y=50, width=400, height=400)








# Quiz frame (shared by all levels)
frame_quiz = Frame(root, bg="green")
progress_label = Label(frame_quiz, text="", font=('Roboto',12), bg='green', fg='#ffffff')
progress_label.pack(pady=10)
question_label = Label(frame_quiz, text="", font=('Roboto',18), bg='green', fg='#ffffff')
question_label.pack(pady=10)
answer_entry = Entry(frame_quiz, font=('Roboto',14), width=10)
answer_entry.pack(pady=5)
answer_entry.bind("<Return>", lambda event: isCorrect())
submit_button = Button(frame_quiz, text="Submit", fg="#ffffff", bg="#234567", command=isCorrect)
submit_button.pack(pady=5)
feedback_label = Label(frame_quiz, text="", font=('Roboto',12), bg='green', fg='#ffffff')
feedback_label.pack(pady=10)
frame_quiz.place(x=0, y=50, width=400, height=400)

# Results frame
frame_results = Frame(root, bg="#234567")
results_label = Label(frame_results, text="", font=('Roboto',18), bg='#234567', fg='#ffffff')
results_label.pack(pady=40)
Button(frame_results, text="Go to home", fg="#ffffff", bg="#345678",
       command=lambda: switch_to_frame(frame1)).pack()
frame_results.place(x=0, y=50, width=400, height=400)

# Initially, show Frame 1

switch_to_frame(frame1)





root.mainloop()