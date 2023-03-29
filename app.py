from flask import Flask, render_template
import pokemon

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route(f'/<name>', methods=["GET"])
def type(name):
    type = pokemon.type(name)
    return type


if __name__ == "__main__":
    app.run(debug=True)