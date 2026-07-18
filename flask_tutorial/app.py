from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Leave my sweater on the porch"

if __name__ == "__main__":
    app.run(debug=True)