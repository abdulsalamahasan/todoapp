from flask import flash
from todoapp import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, validators, ValidationError
from todoapp.db_models import User


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    login = SubmitField("Login")


class SignupForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=8, max=35)])
    con_password = PasswordField("Confirm Password", [validators.DataRequired(), validators.EqualTo("password")])
    signup = SubmitField("Signup")
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username=str(username.data.capitalize())).first()
        if user:
            raise ValidationError("Username is already taken!")

class TodoForm(FlaskForm):
    input = StringField("Add to the list: ", [validators.DataRequired()])
    checkbox = SubmitField("✔️")
    addbtn = SubmitField("Add")


class DellForm(FlaskForm):
    id = IntegerField([validators.DataRequired()]) 
    dellbtn = SubmitField("Dell")

