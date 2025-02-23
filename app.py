from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Charger.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    login = db.Column(db.Text, nullable=False)
    surname = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text, nullable=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def log_in():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/stocks")
def stocks():
    return render_template("stocks.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        surname = request.form['surname']
        password = request.form['password']
        mail = request.form['mail']

        post = Post(name=name, password=password, login=login, surname=surname, mail=mail)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/")
        except:
            return 'Error'
    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)



