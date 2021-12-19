from flask import Flask, render_template, request
import fide

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    your_rating, opponents_rating, K, score = 0, 0, 0, 0
    try:
        your_rating = float(request.form["your_rating"])
        opponents_rating = float(request.form["opponents_rating"])
        score = float(request.form["score"])
        K = float(request.form["K"])

    except:
        return render_template("index.html",
                               yours_new_rating="błąd",
                               opponents_new_rating="błąd")

    yours_new_rating, opponents_new_rating = \
        fide.EloRating(your_rating, opponents_rating, K, score)

    return render_template("index.html",
                           yours_new_rating=yours_new_rating,
                           opponents_new_rating=opponents_new_rating)


if __name__ == "__main__":
    app.run(debug=True)
