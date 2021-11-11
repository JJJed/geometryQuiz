from flask import Flask, render_template, redirect, request, url_for
from forms import QuizForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234-asdf-!@#$-ASDF"


@app.route("/", methods=["GET", "POST"])
def home():
    form = QuizForm()
    if form.is_submitted():
        result = request.form
        score = 0
        return render_template("results.html", result=result, score=score)
    return render_template("quiz.html", form=form)


if __name__ == '__main__':
    app.run()
