from flask import Flask, render_template, request, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def fazer_login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Apenas demonstração visual.
    # Aqui futuramente entraria a validação real do usuário.
    if username and password:
        return redirect(url_for("home"))

    return "Preencha todos os campos."


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
