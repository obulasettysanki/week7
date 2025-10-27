from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        return redirect(url_for("greet", name=name, email=email))
    return render_template("registration.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "Friend")
    email = request.args.get("email", "unknown@example.com")
    return render_template("greetings.html", name=name, email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)