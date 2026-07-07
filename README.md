# 🔤 Word Scramble Game Using Python Tkinter

A fun and interactive **Word Scramble Game** developed using **Python** and **Tkinter**. In this game, players must guess the correct word from a scrambled version before the timer runs out. The game offers multiple difficulty levels, hints, score tracking, a countdown timer, and a light/dark theme for an engaging user experience.

---

## 📌 Features

- 🎮 Three difficulty levels:
  - Easy
  - Medium
  - Hard
- 🔀 Randomly scrambled words
- ⏱️ Countdown timer
- 💡 Hint system
- 👀 Reveal answer option (with score penalty)
- ⏭️ Skip current word
- 📊 Live score tracking
- 🌙 Light/Dark mode toggle
- 🔄 Restart game option
- ⌨️ Press **Enter** to submit answers
- 🖥️ Clean and attractive graphical interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- ttk Widgets
- Random Module
- Messagebox
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Word-Scramble-Game/
│
├── main.py          # Main application source code
└── README.md        # Project documentation
```

---

## 📋 Requirements

- Python 3.x

Tkinter is included with Python, so no additional installation is required.

Verify Tkinter installation:

```bash
python -m tkinter
```

---

## 🚀 How to Run

1. Download or clone the repository.

2. Navigate to the project folder.

3. Run the application:

```bash
python main.py
```

4. Select a difficulty level and start solving scrambled words.

---

## 🎮 How to Play

1. Choose a difficulty level:
   - Easy
   - Medium
   - Hard

2. A scrambled word will appear on the screen.

3. Type your answer in the input box.

4. Press **Enter** or click **Submit**.

5. If your answer is correct:
   - Your score increases by **1**.

6. If your answer is incorrect:
   - The correct word is displayed.

7. Continue solving words until the timer reaches zero.

---

## 🎚️ Difficulty Levels

| Difficulty | Word Type | Time Limit |
|------------|-----------|-----------:|
| Easy | Short and simple words | 45 Seconds |
| Medium | Programming and technology words | 45 Seconds |
| Hard | Advanced computer science terms | 45 Seconds |

---

## 💡 Hint Feature

Click the **Hint** button to display:

- First letter of the word
- Total number of letters

Example:

```text
Hint:
Word starts with 'P'
Length: 6 letters
```

---

## 👀 Reveal Word Feature

Click **Reveal (-1)** to:

- Display the correct answer
- Deduct **1 point**
- Automatically move to the next word

---

## 📊 Scoring System

- ✅ Correct Answer = **+1 Point**
- 👀 Reveal Word = **-1 Point**
- ❌ Wrong Answer = **0 Points**
- ⏭️ Skip = No score change

The score is displayed as:

```text
Score: Correct Answers / Total Rounds
```

---

## 🌙 Theme Support

The application includes two display modes:

- ☀️ Light Mode
- 🌙 Dark Mode

Users can switch themes anytime using the **Theme Toggle** button.

---

## 🎯 Learning Outcomes

This project demonstrates:

- GUI development using Tkinter
- Object-Oriented Programming (OOP)
- Event-driven programming
- Random word generation
- String manipulation
- Countdown timer implementation
- Theme switching
- Score management
- User input validation
- Interactive game design

---

## 🔮 Future Enhancements

- 🏆 High score leaderboard
- 🔊 Sound effects
- 🎵 Background music
- 📚 Larger word dictionary
- 🌐 Online multiplayer mode
- 🖼️ Image-based word hints
- 📈 Difficulty progression
- 💾 Save game progress
- 🎨 Additional color themes
- ☁️ Cloud-based score storage

---

## ⚠️ Limitations

- Uses a predefined word list.
- No online multiplayer support.
- Scores are not saved after closing the application.
- No speech or pronunciation feature.
- Timer is fixed for all difficulty levels.
