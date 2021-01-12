from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# @app.route("/<name>")
# def home(name):
@app.route("/")
def home():
    return render_template("index.html", content="Testing")
@app.route("/about")
def about():
    return render_template("about.html", content="About Me")
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name} !"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True) # debug=True helps keep the server alive and detect changes as and when they happen 