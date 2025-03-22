from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]
players = ['X', 'O']
current_player = 0

def print_board():
    return [
        "|{}|{}|{}|".format(board[0], board[1], board[2]),
        "|{}|{}|{}|".format(board[3], board[4], board[5]),
        "|{}|{}|{}|".format(board[6], board[7], board[8])
    ]

def is_victory(icon):
    return any([
        board[0] == board[1] == board[2] == icon,
        board[3] == board[4] == board[5] == icon,
        board[6] == board[7] == board[8] == icon,
        board[0] == board[3] == board[6] == icon,
        board[1] == board[4] == board[7] == icon,
        board[2] == board[5] == board[8] == icon,
        board[0] == board[4] == board[8] == icon,
        board[2] == board[4] == board[6] == icon
    ])

def is_draw():
    return " " not in board

@app.route('/')
def index():
    return render_template('index.html', board=print_board(), current_player=players[current_player])

@app.route('/move', methods=['POST'])
def move():
    global current_player
    choice = int(request.form['choice']) - 1

    if 0 <= choice < 9 and board[choice] == ' ':
        board[choice] = players[current_player]
        if is_victory(players[current_player]):
            return jsonify({"status": f"Player {players[current_player]} wins!"})
        if is_draw():
            return jsonify({"status": "It's a draw!"})
        current_player = 1 - current_player
        return jsonify({"status": "Next turn"})
    else:
        return jsonify({"status": "Invalid move. Try again."})

if __name__ == "__main__":
    app.run(debug=True)
