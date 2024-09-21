from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(
    __name__,
    template_folder='/var/www/rt_inspect/templates',
    static_folder='/var/www/rt_inspect/static',
    static_url_path='/static'
)

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://rt_inspect_user:Vikimeli01_@localhost/rt_inspect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes, models
