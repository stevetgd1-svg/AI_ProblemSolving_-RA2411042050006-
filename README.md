# AI_ProblemSolving_-RA2411042050006-

📌 Objective

This project implements Artificial Intelligence problem-solving techniques using interactive web applications. Two problems are solved using different AI algorithms and their performance is compared.

🎮 Problem 1: Tic-Tac-Toe AI
🧠 Description

A web-based Tic-Tac-Toe game where a human player competes against an AI opponent. The AI always chooses the best possible move.

⚙️ Algorithms Used
Minimax Algorithm
Alpha-Beta Pruning
📊 Performance Comparison
Execution Time
Number of Nodes Explored
💡 Features
Interactive 3x3 grid UI
AI responds instantly
Displays time taken and nodes explored

🚚 Problem 3: Travelling Salesman Problem (TSP)
🧠 Description

A route optimization system that calculates the shortest path visiting all cities and returning to the start.

⚙️ Algorithms Used
Brute Force Approach
Nearest Neighbor Heuristic

📊 Performance Comparison
Route Cost
Execution Time

💡 Features
User inputs distance matrix
Displays optimal and heuristic routes
Shows execution time for both methods
🛠️ Technologies Used
Python
Flask (Web Framework)
HTML, CSS, JavaScript

📁 Project Structure
AI_ProblemSolving_/
│
├── tic_tac_toe/
│ ├── app.py
│ ├── templates/
│ │ └── ttt.html
│ └── static/
│ └── style.css
│
├── tsp/
│ ├── app.py
│ ├── templates/
│ │ └── tsp.html
│ └── static/
│ └── style.css
│
├── requirements.txt
├── Procfile
└── README.md

▶️ How to Run
Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Run Tic-Tac-Toe

cd tic_tac_toe
python app.py

Open browser:
http://127.0.0.1:5000

Step 3: Run TSP

cd tsp
python app.py

🌐 Live Website

https://ai-problemsolving-ra2411042050006.onrender.com

📸 Sample Output
<img width="845" height="580" alt="image" src="https://github.com/user-attachments/assets/1d1b29c4-bfaf-403f-befb-028997310995" />


📊 Results Summary
Problem	Algorithm	Performance
Tic-Tac-Toe	Minimax	Explores more nodes
Tic-Tac-Toe	Alpha-Beta	Faster, fewer nodes
TSP	Brute Force	Optimal but slow
TSP	Heuristic	Faster but approximate
✅ Conclusion
Alpha-Beta pruning improves efficiency over Minimax.
Heuristic methods scale better than brute-force for large inputs.
