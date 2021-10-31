import flask
from todoapp import app, db, bcrypt, login_manager, current_user, login_user, login_required, logout_user
from flask import redirect, render_template, url_for, request, flash
from todoapp.db_models import AddToList, User
from todoapp.forms import *

login_manager.login_view = "login"
login_manager.login_message = "Login to view the page!"
login_manager.login_message_category = "alert_warning"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
            return redirect(url_for("home"))
    if form.validate_on_submit():
        user = User.query.filter_by(username=str(form.username.data.capitalize())).first()
        if user:
            if user.password and bcrypt.check_password_hash(user.password, form.password.data) :
                login_user(user)
                user.is_active
                flash(f"Welcome back, "+user.username+"!", "alert_info")
                return redirect(url_for("home"))
            else:
                flash(f"Invalid  Password!", "alert_danger")            
        else:
            flash(f"Invalid Username!", "alert_danger")           
    return render_template("login.html", name="Login", form=form)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignupForm()
    if current_user.is_authenticated:
            return redirect(url_for("home"))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
        form.password.data).decode("utf-8")
        username=str(form.username.data.capitalize())
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Created Account successfuly!", "alert_success")
        return redirect(url_for("login"))
    return render_template("signup.html", name="Signup", form=form)

@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    if current_user.is_authenticated:
        list = AddToList.query.all()
        form = TodoForm()
        dellform = DellForm()
        if request.method == "POST":
            if form.addbtn.data:
                data = form.input.data
                list = AddToList(string=data, author=current_user)
                db.session.add(list)
                db.session.commit()
            return redirect(url_for("home"))

        return render_template("home.html", name='Home', form=form, dellform= dellform,list=list)
    return redirect(url_for("login"))

@app.route("/dell/<task>")
@login_required
def dell(task):
    db.session.query(AddToList).filter(AddToList.id==task).delete()
    db.session.commit()
    print(task)
    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))