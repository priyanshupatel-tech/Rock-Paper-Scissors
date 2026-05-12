# ✂️ Rock Paper Scissors — CLI Game

A fun and interactive **Rock Paper Scissors game** built with Python where you play against the computer! Tracks your score, computer's score, ties, and total games played — all in one session.

---

## 🎮 Features

- 🤜 Play Rock, Paper, or Scissors against the computer
- 🎲 Computer makes a **random choice** every round
- 🏆 Tracks **Your Score** in real time
- 🤖 Tracks **Computer Score** in real time
- 🤝 Tracks **Tied Games** count
- 🔢 Tracks **Total Games Played**
- ✅ Input validation — invalid choices are rejected
- 📊 **Final Scorecard** displayed when you exit
- ♾️ Play as many rounds as you want in one session

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Library:** `random` (built-in)
- **Concepts:** Loops, Conditionals, Input Validation, Score Tracking, Game Logic

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshupatel-tech/Rock-Paper-Scissors.git
   cd Rock-Paper-Scissors
   ```

2. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```

> No external libraries needed — uses Python's built-in `random` module only!

---

## 🖥️ Gameplay Preview

```
=================================== Menu ====================================
1. Play Game
2. Exit Game

Enter your Choice= 1

--------------------------------- Your Choices ------------------------------
Rock
Paper
Scissors

Enter your Choice= rock

-------------------------------------------------------------------------------------
You won! 🎉
Your Score: 1
```

---

## 📊 Final Scorecard (on Exit)

```
Thanks For Playing This Game!
-------------------------------------------------------------------------------------
Your Final Score        = 5
-------------------------------------------------------------------------------------
Computer Final Score    = 3
-------------------------------------------------------------------------------------
Total Tied Games        = 2
-------------------------------------------------------------------------------------
Total Games Played      = 10
-------------------------------------------------------------------------------------
```

---

## 🧠 Game Logic

| Your Choice | Computer Choice | Result |
|-------------|-----------------|--------|
| Rock        | Scissors        | You Win ✅ |
| Paper       | Rock            | You Win ✅ |
| Scissors    | Paper           | You Win ✅ |
| Rock        | Paper           | Computer Wins ❌ |
| Paper       | Scissors        | Computer Wins ❌ |
| Scissors    | Rock            | Computer Wins ❌ |
| Any         | Same            | Tie 🤝 |

---

## 📂 Project Structure

```
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py    # Main game file
└── README.md
```

---

## 💡 Learning Outcomes

- Using Python's `random` module for computer decision making
- Implementing game logic with multiple conditions
- Building a score tracking system with variables
- Input validation to handle wrong user inputs
- Creating an engaging loop-based CLI game

---

## 👨‍💻 Author

**Priyanshu Patel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/priyanshupatel-tech/)
- 💻 [GitHub](https://github.com/priyanshupatel-tech)
