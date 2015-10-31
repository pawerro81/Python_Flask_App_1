from flask import Flask
from application.config import app_configure
from application.models import db

# PAWERRO81
# INIT APP
#

app = Flask(__name__)
app_configure(app)
db.init_app(app)