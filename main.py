from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class FilmForm(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 7.5:', validators=[DataRequired()])
    review = StringField('Your review:', validators=[DataRequired()])
    submit = SubmitField('Done!')


class AddForm(FlaskForm):
    title = StringField('Movie title:', validators=[DataRequired()])
    submit = SubmitField('Add movie!')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description= db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000) , nullable=False)
    img_url = db.Column(db.String(1000) , nullable=False)

    def __repr__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"


db.create_all()


@app.route("/")
def home():
    movie_list = Movie.query.all()
    return render_template("index.html", movie_list=movie_list)


@app.route("/edit/<int:id>",  methods=["GET", "POST"])
def edit(id):
    form = FilmForm()
    modifyMovie = Movie.query.get(id)
    if request.method == "POST":
        review = form.review.data
        rating =form.rating.data
        modifyMovie.rating = rating
        modifyMovie.review = review
        db.session.commit()
        all_movie = Movie.query.all()
        return render_template("index.html", movie_list=all_movie)
    return render_template("edit.html", form=form, modifyMovie=modifyMovie)


@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    modifyMovie = Movie.query.get(id)
    db.session.delete(modifyMovie)
    db.session.commit()
    movie_list = Movie.query.all()
    return render_template("index.html", movie_list=movie_list)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    return render_template("add.html", form= form)


if __name__ == '__main__':
    app.run(debug=True)
