import tkinter as tk 
from tkinter import messagebox
class QuizApp:
    def __init__(self):
        self.quiz_data= [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
                "correct_answer": 2
            },
            {
                "question": "Which language is known as the 'mother of all languages'?",
                "options": ["A) Python", "B) C", "C) Latin", "D) Java"],
                "correct_answer": 2
            },
            {
                "question": "Which data type is immutable in Python?",
                "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
                "correct_answer": 2
            }
        ]
        self.current_question_index=0
        self.score=0

        self.window=tk.Tk()
        self.window.title("Quiz App")

        self.question_label=tk.Label(self.window,text="")
        self.question_label.pack()

        self.options_frame=tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons=[]
        for i in range(4):
            button=tk.Button(self.options_frame,text="",width=30,command=lambda i=i:self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button) 
        
        self.next_question_button=tk.Button(self.window,text="Next Question",width=30,command=self.next_question)
        self.next_question_button.pack(pady=10)

    def next_question(self):
        self.current_question_index+=1
        if self.current_question_index== len(self.quiz_data):
            messagebox.showinfo("Quiz Over", "your score is "+str(self.score))
            self.window.quit()
        else:
            self.load_question()

    def check_answer(self,selected_option):
        question_data=self.quiz_data[self.current_question_index]
        answer=question_data["correct_answer"]
        if selected_option== answer:
            self.score=self.score+ 1 
            messagebox.showinfo("Correct","Your answer is correct")
        else:
            messagebox.showinfo("Incorrect","Your answer is Incorrect")

    def load_question(self):
        question_data=self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options=question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])
    def start_quiz(self):
        self.load_question()
        self.window.mainloop()
quiz_app=QuizApp()
quiz_app.start_quiz()


