from flask import Flask
import BlackJack
import Player
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def blackjack():
    return True

if __name__ == "__main__":
    app.run()
