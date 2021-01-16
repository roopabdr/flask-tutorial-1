from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello" # defining a session with the help of secret key
app.permanent_session_lifetime = timedelta(minutes=5) # setting permanent sessions - this helps maintain the session even though the browser is closed
# app.permanent_session_lifetime = timedelta(days=5) # setting permanent sessions in days

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
        session.permanent = True # sets a given or logged in session permanently for no. of days or minutes it has been set to
        user = request.form["nm"]
        session["user"] = user # used for sessions for a given user with naming the dictionary key as 'user"
        flash("Login Successful !")
        return redirect(url_for("user", usr=user))
    else:
        if "user" in session:
            flash("Already logged in !")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    # verify the user is actully logged in
    if "user" in session:
        user = session["user"] # checking for a particular user with the key as "user"
        return render_template("user.html", user=user)
        # return f"<h1>{user}</h1>" # this is how we're getting data from the session instead of a URL parameter
    else:
        flash("You're not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():    
    if "user" in session:
        user = session["user"]
        flash(f"You have been successfully logged out, {user}", "info") # pass a message to be flashed on the login page upon successfully logging out
    
    session.pop("user", None) # clearing a session on logout
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