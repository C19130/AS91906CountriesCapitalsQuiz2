import tkinter as tk
from tkinter import messagebox
import random

# Quiz data (Question: [Options, Correct Option Index])
quiz_data = {
    "What is the capital of France?": [["Berlin", "Paris", "London", "Rome"], 1],
    "What is the capital of Japan?": [["Tokyo", "Beijing", "Seoul", "Bangkok"], 0],
    "What is the capital of Australia?": [["Canberra", "Sydney", "Melbourne", "Perth"], 0],
    "What is the capital of Brazil?": [["Rio de Janeiro", "Sao Paulo", "Brasilia", "Buenos Aires"], 2],
    "What is the capital of Canada?": [["Ottawa", "Toronto", "Montreal", "Vancouver"], 0],
    "What is the capital of India?": [["Delhi", "Mumbai", "Kolkata", "Chennai"], 0],
    "What is the capital of China?": [["Beijing", "Shanghai", "Guangzhou", "Shenzhen"], 0],
    "What is the capital of Germany?": [["Berlin", "Hamburg", "Munich", "Cologne"], 0],
    "What is the capital of Italy?": [["Rome", "Milan", "Naples", "Turin"], 0],
    "What is the capital of South Africa?": [["Johannesburg", "Cape Town", "Pretoria", "Durban"], 1],
}

class CapitalCityQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Capital City Quiz")
        self.geometry("400x300")
        self.configure(bg="#ffb7ce")
        self.score = 0
        self.question_index = 0
        self.user_answers = {}
        self.questions = []
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Capital Cities Quiz", font=("Arial", 24), bg="#ffb7ce", fg="white")
        self.title_label.pack(pady=20)
      

        self.start_button = tk.Button(self, text="Start Quiz", font=("Arial", 16), command=self.start_quiz, bg="white", fg="#ffb7ce")
        self.start_button.pack(pady=10)

        self.instructions_button = tk.Button(self, text="Instructions", font=("Arial", 16), command=self.show_instructions, bg="white", fg="#ffb7ce")
        self.instructions_button.pack(pady=10)

    def start_quiz(self):
        self.questions = self.generate_quiz()
        self.score = 0
        self.question_index = 0
        self.user_answers = {}
        self.title_label.destroy()
        self.start_button.destroy()
        self.instructions_button.destroy()
        self.create_quiz_widgets()

    def generate_quiz(self):
        all_questions = list(quiz_data.keys())
        random.shuffle(all_questions)
        return all_questions[:4]

    def create_quiz_widgets(self):
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

        self.quit_button = tk.Button(self, text="Quit", command=self.return_to_start_menu)
        self.quit_button.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            options_data = quiz_data[question]
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

        question = self.questions[self.question_index]
        options_data = quiz_data[question]
        correct_answer_index = options_data[1]

        if selected_index == correct_answer_index:
            self.score += 1
        self.user_answers[question] = (options_data[0][selected_index], options_data[0][correct_answer_index])

        for option_button in self.option_buttons:
            option_button.config(state=tk.DISABLED)

        self.submit_button.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        self.show_question()

    def show_results(self):
        result_message = f"You scored {self.score} out of {len(self.questions)}!\n\n"
        result_message += "Here are the questions you got wrong:\n\n"

        all_correct = True
        for question, (user_answer, correct_answer) in self.user_answers.items():
            if user_answer != correct_answer:
                all_correct = False
                result_message += f"Q: {question}\n"
                result_message += f"Your Answer: {user_answer}\n"
                result_message += f"Correct Answer: {correct_answer}\n\n"

        if all_correct:
            result_message = "Congratulations! You got all the questions right!\n\n" \
                             "Great job!"
        else:
            result_message = result_message.strip()

        messagebox.showinfo("Quiz Results", result_message)
        self.return_to_start_menu()

    def return_to_start_menu(self):
        self.question_index = 0
        self.score = 0
        self.user_answers = {}
        self.question_label.destroy()
        self.option_buttons_frame.destroy()
        self.submit_button.destroy()
        self.next_question_button.destroy()
        self.quit_button.destroy()
        self.create_widgets()

    def show_instructions(self):
        instructions_text = "Welcome to the Capital City Quiz!\n\n"\
                            "You will be presented with questions about the capitals of different countries.\n"\
                            "For each question, four possible answers will be provided.\n"\
                            "Choose the correct answer by clicking on it.\n"\
                            "After selecting an answer, press the 'Submit' button to lock it in.\n"\
                            "Press the 'Next Question' button to move to the next question.\n"\
                            "At the end of the quiz, your score will be displayed, and you will be provided with feedback on your answers.\n"\
                            "Good luck!"
        messagebox.showinfo("Instructions", instructions_text)


if __name__ == "__main__":
    app = CapitalCityQuiz()
    app.mainloop()
