from flask import Flask, render_template, request, redirect, url_for
from quiz_bowl_flask import Game

app = Flask(__name__)

game = Game()

game.cat = ["Science"]
game.diff = ["1"]
strict = 0.8

@app.route("/")
def home():
    if game.current_question is None:
        game.next_question()
    return render_template(
        "index.html",
        question=game.current_question.text,
        answer=game.current_question.answer
    )

@app.route("/answer", methods=["POST"])
def answer():

    question = game.current_question.text
    user_answer = request.form["user_answer"]
    
    if game.submit_answer(user_answer):
        result = "Correct!"
    else:
        result = "Incorrect!"
    
    

    return render_template(
        "index.html",
        question=question,
        result=result,
        score = game.score
    )

@app.route("/next", methods=["POST"])
def next():
    game.next_question()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)