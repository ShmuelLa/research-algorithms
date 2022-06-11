from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    form = DataForm()
    is_submitted = form.validate_on_submit()
    # return render_template('dynamic-index.html')
    return render_template('dynamic-index.html', form=form)


class DataForm(FlaskForm):
    num_of_agents = IntegerField("Agents", validators=[InputRequired(), NumberRange(1, 5)])
    num_of_objects = IntegerField("Objects", validators=[InputRequired(), NumberRange(2, 5)])
    submit = SubmitField('Submit')

"""
line 31 after:
<div class="collapse navbar-collapse" id="navbar">

<!--        <div class="navbar-nav">-->
<!--          {% if user.is_authenticated %}-->
<!--          <a class="nav-item nav-link" id="home" href="/">Home</a>-->
<!--          <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>-->
<!--          {% else %}-->
<!--          <a class="nav-item nav-link" id="login" href="/login">Login</a>-->
<!--          <a class="nav-item nav-link" id="signUp" href="/sign-up">Sign Up</a>-->
<!--          {% endif %}-->
<!--        </div>-->
"""
if __name__ == "__main__":
    app.run(debug=True)
