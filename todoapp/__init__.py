from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

app = Flask(__name__)
app.config["SECRET_KEY"]="Hi there how are you are you ok are you fine so!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from todoapp import routes, db_models
