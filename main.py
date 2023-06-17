from flask import  Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def word(word):
    filepath = "dictionary.csv"
    df = pd.read_csv(filepath)
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"definition": definition,
            "word": word}


if __name__ == "__main__":
    app.run(debug=True, port=5001)