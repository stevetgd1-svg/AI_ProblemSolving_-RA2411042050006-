from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

nodes = 0

def check_winner(b):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] != "":
            return b[w[0]]
    return None

def is_draw(b):
    return "" not in b

def moves(b):
    return [i for i in range(9) if b[i] == ""]

def minimax(b, depth, is_max):
    global nodes
    nodes += 1

    winner = check_winner(b)
    if winner == "O": return 10 - depth
    if winner == "X": return depth - 10
    if is_draw(b): return 0

    if is_max:
        best = -1000
        for m in moves(b):
            b[m] = "O"
            best = max(best, minimax(b, depth+1, False))
            b[m] = ""
        return best
    else:
        best = 1000
        for m in moves(b):
            b[m] = "X"
            best = min(best, minimax(b, depth+1, True))
            b[m] = ""
        return best

@app.route("/")
def home():
    return render_template("ttt.html")

@app.route("/move", methods=["POST"])
def move():
    global nodes
    nodes = 0

    data = request.json
    board = data["board"]

    best = -1000
    move = -1

    start = time.time()

    for i in moves(board):
        board[i] = "O"
        val = minimax(board, 0, False)
        board[i] = ""

        if val > best:
            best = val
            move = i

    end = time.time()

    return jsonify({
        "move": move,
        "time": end-start,
        "nodes": nodes
    })

if __name__ == "__main__":
    app.run()