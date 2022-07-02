from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class AppInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.user_score = 0
        # window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        # label score
        self.score = Label(text=f"Score : {self.user_score}", highlightthickness=0,
                           bg=THEME_COLOR, font=("Arial", 12), fg="white")
        self.score.grid(row=0, column=1, pady=20, padx=20)
        # canvas
        self.canvas = Canvas(width=300, height=250, background="white")
        self.show_question = self.canvas.create_text(150, 125, text="This is a question",
                                                     font=("Arial", 12), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        # button
        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, background=THEME_COLOR,
                                     command=self.true_button)
        self.correct_button.grid(row=2, column=0, pady=30)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, background=THEME_COLOR,
                                   command=self.false_button)
        self.false_button.grid(row=2, column=1)

        self.game_question()

        self.window.mainloop()

    def game_question(self):
        self.correct_button.config(state="active")
        self.false_button.config(state="active")
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            the_question = self.quiz.next_question()
            self.canvas.itemconfig(self.show_question, text=f"{the_question}")
        else:
            self.canvas.configure(bg="white")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.show_question, text="No more question left")

    def true_button(self):
        check_answer = self.quiz.check_answer("True")
        self.give_feedback(check_answer)

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.correct_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if is_right:
            self.canvas.configure(bg="green")
            self.user_score += 1
            self.score.configure(text=f"Score = {self.user_score}")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.game_question)
