from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TRACK PLAN RANKER"

if __name__ == "__main__":
    app.run(debug=True)
