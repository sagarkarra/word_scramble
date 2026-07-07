import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble Game")
        self.root.resizable(False, False)

        # Word lists categorized by difficulty tier
        self.difficulty_words = {
            "Easy": ["CAT", "DOG", "FISH", "BIRD", "FROG", "LION", "DUCK", "DEER"],
            "Medium": ["PYTHON", "TKINTER", "VARIABLE", "FUNCTION", "COMPUTER", "PROGRAM"],
            "Hard": ["ALGORITHM", "ENCAPSULATION", "POLYMORPHISM", "ASYNCHRONOUS", "FRAMEWORK"]
        }
        
        # State management tracks
        self.current_word = ""
        self.scrambled_word = ""
        self.score = 0
        self.total_rounds = 0
        self.time_left = 45
        self.game_over = False
        self.timer_job = None
        self.dark_mode = False

        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        # Top Frame for Stats & Theme Selector
        self.stats_frame = tk.Frame(self.root, bg="#2c3e50")
        self.stats_frame.pack(fill="x", padx=10, pady=5)

        self.timer_label = tk.Label(self.stats_frame, text="Time: 45s", font=("Helvetica", 12), bg="#2c3e50", fg="white")
        self.timer_label.pack(side="left", padx=10, pady=5)

        self.score_label = tk.Label(self.stats_frame, text="Score: 0/0", font=("Helvetica", 12), bg="#2c3e50", fg="white")
        self.score_label.pack(side="left", padx=10, pady=5)

        # Theme Toggle Button (Top Right)
        self.theme_btn = tk.Button(self.stats_frame, text="🌙 Dark Mode", font=("Helvetica", 10), 
                                   command=self.toggle_theme, bg="#34495e", fg="white")
        self.theme_btn.pack(side="right", padx=10, pady=5)

        # Difficulty Selector Dropdown
        self.diff_var = tk.StringVar(value="Medium")
        self.diff_dropdown = ttk.Combobox(self.stats_frame, textvariable=self.diff_var, values=["Easy", "Medium", "Hard"], width=8, state="readonly")
        self.diff_dropdown.pack(side="right", padx=10, pady=5)
        self.diff_dropdown.bind("<<ComboboxSelected>>", lambda e: self.reset_game())

        # Middle Frame for Game Content
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(padx=20, pady=15)

        self.scrambled_label = tk.Label(self.game_frame, text="", font=("Helvetica", 28, "bold"), fg="#2980b9")
        self.scrambled_label.pack(pady=10)

        self.entry = tk.Entry(self.game_frame, font=("Helvetica", 18), justify="center")
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_answer())

        # Hint Display Label
        self.hint_label = tk.Label(self.game_frame, text="", font=("Helvetica", 11, "italic"), fg="#7f8c8d")
        self.hint_label.pack(pady=5)

        # Bottom Frame for Buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(fill="x", padx=20, pady=10)

        self.submit_btn = tk.Button(self.btn_frame, text="Submit", font=("Helvetica", 11, "bold"), bg="#2ecc71", fg="white", command=self.check_answer)
        self.submit_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.hint_btn = tk.Button(self.btn_frame, text="Hint", font=("Helvetica", 11), bg="#f1c40f", fg="black", command=self.show_hint)
        self.hint_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.reveal_btn = tk.Button(self.btn_frame, text="Reveal (-1)", font=("Helvetica", 11), bg="#d35400", fg="white", command=self.reveal_word)
        self.reveal_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.skip_btn = tk.Button(self.btn_frame, text="Skip", font=("Helvetica", 11), bg="#e74c3c", fg="white", command=self.next_round)
        self.skip_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.reset_btn = tk.Button(self.btn_frame, text="Reset", font=("Helvetica", 11), bg="#34495e", fg="white", command=self.reset_game)
        self.reset_btn.pack(side="left", fill="x", expand=True, padx=2)

    def scramble_string(self, word):
        char_list = list(word)
        while True:
            random.shuffle(char_list)
            scrambled = "".join(char_list)
            if scrambled != word or len(word) <= 1:
                return scrambled

    def reset_game(self):
        # Cancel running timers to prevent duplicates
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.score = 0
        self.total_rounds = 0
        self.time_left = 45
        self.game_over = False
        
        self.score_label.config(text="Score: 0/0")
        self.timer_label.config(text="Time: 45s", fg="white")
        
        self.next_round()
        self.update_timer()
        self.apply_current_theme()

    def update_timer(self):
        if self.game_over:
            return

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}s")
            if self.time_left <= 10:
                self.timer_label.config(fg="#e74c3c") # Red alert color
            self.timer_job = self.root.after(1000, self.update_timer)
        else:
            self.game_over = True
            messagebox.showinfo("Time's Up!", f"Game Over!\nFinal Score: {self.score}/{self.total_rounds}")
            self.reset_game()

    def show_hint(self):
        if self.game_over or not self.current_word:
            return
        first_letter = self.current_word[0]
        word_length = len(self.current_word)
        self.hint_label.config(text=f"Hint: Word starts with '{first_letter}' and has {word_length} letters.")

    def reveal_word(self):
        if self.game_over or not self.current_word:
            return
        
        self.total_rounds += 1
        self.score = max(0, self.score - 1) # Deduct 1 point, prevent negative score
        self.score_label.config(text=f"Score: {self.score}/{self.total_rounds}")
        
        messagebox.showinfo("Answer Revealed", f"The word was: {self.current_word}")
        self.next_round()

    def next_round(self):
        if self.game_over:
            return

        selected_diff = self.diff_var.get()
        word_pool = self.difficulty_words[selected_diff]
        
        self.current_word = random.choice(word_pool)
        self.scrambled_word = self.scramble_string(self.current_word)
        
        self.scrambled_label.config(text=self.scrambled_word)
        self.hint_label.config(text="") # Clear old hint
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_answer(self):
        if self.game_over:
            return

        user_guess = self.entry.get().strip().upper()
        if not user_guess:
            return
            
        self.total_rounds += 1
        
        if user_guess == self.current_word:
            self.score += 1
            messagebox.showinfo("Correct!", f"Nicely done! '{self.current_word}' is right!")
        else:
            messagebox.showerror("Incorrect", f"Wrong choice!\nIt was: '{self.current_word}'")

        self.score_label.config(text=f"Score: {self.score}/{self.total_rounds}")
        self.next_round()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_current_theme()

    def apply_current_theme(self):
        if self.dark_mode:
            # Dark Theme Palette
            bg_color = "#1a252f"
            fg_scrambled = "#3498db"
            fg_hint = "#bdc3c7"
            entry_bg = "#2c3e50"
            entry_fg = "white"
            self.theme_btn.config(text="☀️ Light Mode", bg="#ecf0f1", fg="black")
        else:
            # Light Theme Palette (Default)
            bg_color = "#f8f9fa"
            fg_scrambled = "#2980b9"
            fg_hint = "#7f8c8d"
            entry_bg = "white"
            entry_fg = "black"
            self.theme_btn.config(text="🌙 Dark Mode", bg="#34495e", fg="white")

        # Apply configurations across UI elements
        self.root.config(bg=bg_color)
        self.game_frame.config(bg=bg_color)
        self.btn_frame.config(bg=bg_color)
        self.scrambled_label.config(bg=bg_color, fg=fg_scrambled)
        self.hint_label.config(bg=bg_color, fg=fg_hint)
        self.entry.config(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordScrambleGame(root)
    root.mainloop()
