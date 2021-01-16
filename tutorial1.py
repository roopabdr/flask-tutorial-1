from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "hello" # defining a session with the help of secret key

# @app.route("/<name>")
# def home(name):
@app.route("/")
def home():
    return render_template("index.html", content="Testing")
@app.route("/about")
def about():
    return render_template("about.html", content="About Me")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user # used for sessions for a given user with naming the dictionary key as 'user"
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    # verify the user is actully logged in
    if "user" in session:
        user = session["user"] # checking for a particular user with the key as "user"
        return f"<h1>{user}</h1>" # this is how we're getting data from the session instead of a URL parameter
    else:
        return redirect(url_for("login"))

# below is the code snippet to pass parameters on the URL and then use it process as part of the function code
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name} !"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True) # debug=True helps keep the server alive and detect changes as and when they happen 