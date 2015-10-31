from application import app
from flask import Blueprint, render_template
from application.models import *

main = Blueprint('application', __name__, template_folder='templates')

@app.route('/')
def index():
    building1 = Buildings("budynek7",1)
    db.session.add(building1)
    db.session.commit()
    return render_template("index.htm")


@app.route("/users")
def userlist():
    users = [user for user in Users.query.all()]
    return render_template("users.htm", users=users)
