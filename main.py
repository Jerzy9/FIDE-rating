from flask import Flask, render_template, request
import fide

app = Flask(__name__)

@app.route("/")
def hello_world():
    Ra = 1200
    Rb = 1000
    K = 30
    d = 1
    yours_rating, opponents_rating, yours_diff, opponents_diff, yours_new_rating, opponents_new_rating = fide.EloRating(Ra, Rb, K, d)

    return render_template("index.html",
                           yours_rating=yours_rating,
                           opponents_rating=opponents_rating,
                           yours_diff=yours_diff,
                           opponents_diff=opponents_diff,
                           yours_new_rating=yours_new_rating,
                           opponents_new_rating=opponents_new_rating)


@app.route("/calculate", methods=["POST"])
def calculate():
    your_rating = float(request.form["your_rating"])
    opponents_rating = float(request.form["opponents_rating"])
    score = float(request.form["score"])
    K = float(request.form["K"])

    yours_rating, opponents_rating, yours_diff, opponents_diff, yours_new_rating, opponents_new_rating = \
        fide.EloRating(your_rating, opponents_rating, K, score)

    return render_template("index.html",
                           yours_rating=yours_rating,
                           opponents_rating=opponents_rating,
                           yours_diff=yours_diff,
                           opponents_diff=opponents_diff,
                           yours_new_rating=yours_new_rating,
                           opponents_new_rating=opponents_new_rating)


if __name__ == "__main__":
    app.run(debug=True)
