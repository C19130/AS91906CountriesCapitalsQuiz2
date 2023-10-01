import tkinter as tk
from tkinter import messagebox

# Quiz data (Question: [Options, Correct Option Index])
quiz_data = {
    "What is the capital of France?": [["Berlin", "Paris", "London", "Rome"], 1],
    "What is the capital of Japan?": [["Tokyo", "Beijing", "Seoul", "Bangkok"], 0],
    "What is the capital of Australia?": [["Canberra", "Sydney", "Melbourne", "Perth"], 0],
    "What is the capital of Brazil?": [["Rio de Janeiro", "Sao Paulo", "Brasilia", "Buenos Aires"], 2],
    "What is the capital of Canada?": [["Ottawa", "Toronto", "Montreal", "Vancouver"], 0],
}

class CapitalCityQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Capital City Quiz")
        self.geometry("400x300")
        self.score = 0
        self.question_index = 0
        self.user_answers = {}
        self.create_widgets()

    def create_widgets(self):
        self.start_quiz()

    def start_quiz(self):
        self.question_label = tk.Label(self, text="", font=("Arial", 14), wraplength=300)
        self.question_label.pack(pady=10)

        self.option_var = tk.StringVar()
        self.option_buttons_frame = tk.Frame(self)
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self.option_buttons_frame, text="", variable=self.option_var, value=i)
            self.option_buttons.append(option_button)
            option_button.pack(anchor=tk.W)
        self.option_buttons_frame.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question_button = tk.Button(self, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_question_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.question_index < len(quiz_data):
            question, options_data = list(quiz_data.items())[self.question_index]
            options, correct_index = options_data
            self.question_label.config(text=question)
            self.option_var.set(-1)  # Deselect any previous selection
            for i, option_button in enumerate(self.option_buttons):
                option_button.config(text=options[i], state=tk.NORMAL)

            self.submit_button.config(state=tk.NORMAL)
            self.next_question_button.config(state=tk.DISABLED)
        else:
            self.show_results()

    def check_answer(self):
        selected_index = int(self.option_var.get())
        if selected_index == -1:
            messagebox.showerror("Error", "Please select an answer before submitting.")
            return

        question, options_data = list(quiz_data.items())[self.question_index]
        correct_answer_index = options_data[1]

        if selected_index == correct_answer_index:
            self.score += 1
        self.user_answers[question] = options_data[0][selected_index]

        for option_button in self.option_buttons:
            option_button.config(state=tk.DISABLED)

        self.submit_button.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        self.show_question()

    def show_results(self):
        result_message = f"You scored {self.score} out of {len(quiz_data)}!\n\n"
        messagebox.showinfo("Quiz Results", result_message)
        self.destroy()
        # If you want to reset the quiz and start again, you can create a method for it and call it here.

if __name__ == "__main__":
    app = CapitalCityQuiz()
    app.mainloop()
