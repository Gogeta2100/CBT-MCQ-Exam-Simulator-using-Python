import tkinter as tk
from tkinter import ttk  # For table in result screen
import time  # For time tracking
from tkinter import filedialog

class MCQTestGUI:
    def __init__(self, root, total_questions=30, test_title="QM minor test upto H atom"):
        self.root = root
        self.root.title(test_title)  # Set the title of the test window
        self.root.geometry("800x600")

        self.total_questions = total_questions
        self.test_title = test_title
        self.test_submitted = False  # Flag to indicate if test is submitted


        # Title label
        self.title_label = tk.Label(self.root, text=self.test_title, font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.timer_label = tk.Label(self.root, text="Time Left: 90:00", font=("Arial", 14))
        self.timer_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Questions and options (you can add more questions as needed)
        self.questions = [
            {
                "question": "Question 1: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 2: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 3: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 4: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 5: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 6: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 7: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 8: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 9: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 10: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 11: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 12: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
             {
                "question": "Question 13: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 14: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 15: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 16: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 17: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 18: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 19: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 20: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 21: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 22: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 23: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 24: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
             {
                "question": "Question 25: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 26: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 27: What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
            },
            {
                "question": "Question 28: What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Question 29: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            },
            {
                "question": "Question 30: Who developed the theory of relativity?",
                "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Bohr"],
                "answer": "B"
            }
        ]
        
        # Adjust total questions to be the number of questions provided, if fewer
        self.total_questions = min(self.total_questions, len(self.questions))

        # Responses, marked for review, and time tracking for each question
        self.responses = [""] * self.total_questions
        self.marked_for_review = [False] * self.total_questions
        self.time_spent_per_question = [0] * self.total_questions  # Time spent on each question in seconds
        self.current_question_index = 0
        self.question_start_time = time.time()  # Start tracking time for the first question

        # Create question and option UI
        self.create_question_ui()

        # Create navigation panel on the right side with 3 columns and 10 rows for navigation buttons
        self.create_navigation_panel()

        self.start_time = 90 * 60  # 90 minutes in seconds
        self.update_timer()

    def create_question_ui(self):
        self.question_frame = tk.Frame(self.root)
        self.question_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

        # Question label
        self.question_label = tk.Label(self.question_frame, text=self.questions[self.current_question_index]["question"], font=("Arial", 14))
        self.question_label.pack()

        # Radio buttons for options
        self.selected_option = tk.StringVar(value="")
        self.option_buttons = []
        for i, option in enumerate(self.questions[self.current_question_index]["options"]):
            rb = tk.Radiobutton(self.question_frame, text=option, variable=self.selected_option, value=option[0], font=("Arial", 12))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        # Navigation and Action Buttons below the question
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_question, font=("Arial", 12))
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.grid(row=0, column=1, padx=5)

        self.mark_button = tk.Button(self.button_frame, text="Mark for Review", command=self.mark_for_review, font=("Arial", 12))
        self.mark_button.grid(row=0, column=2, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear Response", command=self.clear_response, font=("Arial", 12))
        self.clear_button.grid(row=0, column=3, padx=5)

        self.submit_button = tk.Button(self.button_frame, text="Submit Test", command=self.submit_test, font=("Arial", 12))
        self.submit_button.grid(row=0, column=4, padx=5)

    def create_navigation_panel(self):
        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.grid(row=1, column=1, padx=20, pady=20, sticky="ne")

        self.nav_buttons = []
        for i in range(self.total_questions):
            row = i % 10  # Arrange buttons in 10 rows
            col = i // 10  # Arrange buttons in 3 columns
            btn = tk.Button(self.navigation_frame, text=f"{i+1}", width=3, font=("Arial", 12), command=lambda i=i: self.jump_to_question(i))
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.nav_buttons.append(btn)

        self.update_nav_button_colors()

    def update_question_ui(self):
        self.question_label.config(text=self.questions[self.current_question_index]["question"])
        self.selected_option.set(self.responses[self.current_question_index])
        for i, option in enumerate(self.questions[self.current_question_index]["options"]):
            self.option_buttons[i].config(text=option)

        self.update_nav_button_colors()

    def update_nav_button_colors(self):
        for i in range(self.total_questions):
            if self.responses[i] != "" and self.marked_for_review[i]:
                self.nav_buttons[i].config(bg="purple")  # Answered + Marked for Review
            elif self.responses[i] != "":
                self.nav_buttons[i].config(bg="green")  # Answered questions
            elif self.marked_for_review[i]:
                self.nav_buttons[i].config(bg="yellow")  # Marked for review
            else:
                self.nav_buttons[i].config(bg="red")  # Unanswered questions

    def next_question(self):
        self.save_response()
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.update_question_ui()
            self.question_start_time = time.time()  # Start tracking time for the new question

    def prev_question(self):
        self.save_response()
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.update_question_ui()
            self.question_start_time = time.time()  # Start tracking time for the new question

    def jump_to_question(self, index):
        self.save_response()
        self.current_question_index = index
        self.update_question_ui()
        self.question_start_time = time.time()  # Start tracking time for the new question

    def save_response(self):
        self.responses[self.current_question_index] = self.selected_option.get()
        time_spent = time.time() - self.question_start_time  # Time spent on this question
        self.time_spent_per_question[self.current_question_index] += int(time_spent)

    def mark_for_review(self):
        self.marked_for_review[self.current_question_index] = True
        self.update_nav_button_colors()

    def clear_response(self):
        self.selected_option.set("")
        self.responses[self.current_question_index] = ""
        self.update_nav_button_colors()

    def submit_test(self):
        self.save_response()
        self.test_submitted = True  # Set the flag to stop the timer
        self.show_result_table()


    def show_result_table(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Test Result")
        result_window.geometry("500x400")

        # Add "Save Result" button at the top-left corner
        save_button = tk.Button(result_window, text="Save Result", command=self.save_result, font=("Arial", 12))
        save_button.pack(anchor="nw", padx=10, pady=10)

        # Title in the result window
        result_title_label = tk.Label(result_window, text=self.test_title, font=("Arial", 16, "bold"))
        result_title_label.pack(anchor="ne", padx=10, pady=10)

        # Summary of the test (attempted, unanswered, marked, etc.)
        attempted = sum([1 for r in self.responses if r != ""])
        unanswered = self.total_questions - attempted
        marked = sum(self.marked_for_review)
        answered_marked = sum([1 for i in range(self.total_questions) if self.responses[i] != "" and self.marked_for_review[i]])

        summary_label = tk.Label(result_window, text=f"Attempted: {attempted} | Unanswered: {unanswered} | Marked for Review: {marked} | Answered & Marked: {answered_marked}", font=("Arial", 12))
        summary_label.pack(pady=10)

        # Display result in tabular form
        table_frame = tk.Frame(result_window)
        table_frame.pack(fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(table_frame, columns=("Question", "Response", "Marked for Review", "Time Spent"), show='headings')
        tree.heading("Question", text="Q.No")
        tree.heading("Response", text="Response")
        tree.heading("Marked for Review", text="Marked for Review")
        tree.heading("Time Spent", text="Time Spent (seconds)")

        # Insert data into the table
        for i in range(self.total_questions):
            question_num = i + 1
            response = self.responses[i] if self.responses[i] != "" else "X"  # Show "X" for unanswered questions
            marked = "Yes" if self.marked_for_review[i] else "No"
            time_spent = self.time_spent_per_question[i]
            tree.insert("", "end", values=(question_num, response, marked, time_spent))

        tree.pack(fill=tk.BOTH, expand=True)

    def save_result(self):
        # Open a file save dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
        
        if not file_path:
            return  # If no file is chosen, do nothing

        # Prepare the data to save (format as needed)
        data_to_save = f"Test Title: {self.test_title}\n\n"
        data_to_save += "Q.No | Response | Marked for Review | Time Spent (seconds)\n"
        data_to_save += "-" * 50 + "\n"

        for i in range(self.total_questions):
            question_num = i + 1
            response = self.responses[i] if self.responses[i] != "" else "X"
            marked = "Yes" if self.marked_for_review[i] else "No"
            time_spent = self.time_spent_per_question[i]
            data_to_save += f"{question_num}    | {response}   | {marked}          | {time_spent}\n"

        # Write the data to the selected file
        with open(file_path, 'w') as file:
            file.write(data_to_save)

        # Optionally, show a confirmation message (you can use a dialog box or just a print statement)
        print(f"Results saved to {file_path}")




    def update_timer(self):
        if not self.test_submitted:  # Only update the timer if the test is not submitted
            minutes, seconds = divmod(self.start_time, 60)
            self.timer_label.config(text=f"Time Left: {minutes:02}:{seconds:02}")
            if self.start_time > 0:
                self.start_time -= 1
                self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Enable full-screen mode

    # Allow exiting full-screen mode with 'Esc'
    root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))

    app = MCQTestGUI(root)
    root.mainloop()

