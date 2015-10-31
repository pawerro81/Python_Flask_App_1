# PAWERRO81
# APP CONFIG
#

def app_configure(app):
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/mysite/flask/baza.db'