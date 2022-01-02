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
        fide.rating(your_rating, opponents_rating, K, score)

    return render_template("index.html",
                           yours_new_rating=yours_new_rating,
                           opponents_new_rating=opponents_new_rating)


@app.route("/initial")
def initial():
    return render_template("initial.html")


@app.route("/initial", methods=["POST"])
def initial_calculate():
    calculations, initial_ranking = 0, 0
    try:
        avg_rating = float(request.form["avg_rating"])
        score = float(request.form["score"])
        n = float(request.form["n"])
        if score > n or n < 5:
            raise Exception()

    except:
        return render_template("initial.html",
                               initial_ranking="",
                               calculations="błąd")

    initial_ranking, calculations = fide.initial_rating(avg_rating, score, n)

    return render_template("initial.html", initial_ranking=initial_ranking, calculations=calculations)


if __name__ == "__main__":
    app.run(debug=True)
