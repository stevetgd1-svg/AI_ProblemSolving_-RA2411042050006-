from flask import Flask, render_template, request, jsonify
import itertools, time

app = Flask(__name__)

def brute(matrix):
    n = len(matrix)
    cities = list(range(n))
    best_cost = float("inf")
    best_path = []

    for p in itertools.permutations(cities):
        cost = 0
        for i in range(n-1):
            cost += matrix[p[i]][p[i+1]]
        cost += matrix[p[-1]][p[0]]

        if cost < best_cost:
            best_cost = cost
            best_path = p

    return best_path, best_cost

def heuristic(matrix):
    n = len(matrix)
    visited = [False]*n
    path = [0]
    visited[0] = True

    for _ in range(n-1):
        last = path[-1]
        nxt = min(
            [(matrix[last][j], j) for j in range(n) if not visited[j]]
        )[1]
        path.append(nxt)
        visited[nxt] = True

    return path

@app.route("/")
def home():
    return render_template("tsp.html")

@app.route("/solve", methods=["POST"])
def solve():
    matrix = request.json["matrix"]

    s = time.time()
    bf_path, bf_cost = brute(matrix)
    bf_time = time.time()-s

    s = time.time()
    nn_path = heuristic(matrix)
    nn_time = time.time()-s

    return jsonify({
        "bf_path": bf_path,
        "bf_cost": bf_cost,
        "bf_time": bf_time,
        "nn_path": nn_path,
        "nn_time": nn_time
    })

if __name__ == "__main__":
    app.run()