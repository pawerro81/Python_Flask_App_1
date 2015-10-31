from flask.ext.sqlalchemy import SQLAlchemy

# PAWERRO81
# DATABASE TABLE MAPPING CLASS IN FLASK
#

db = SQLAlchemy()


#TABLE USERS
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30))
    password = db.Column(db.String(60))
    user_name = db.Column(db.String(30))
    user_surname = db.Column(db.String(60))
    user_email = db.Column(db.String(60))
    user_active = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    role = db.relationship('Roles',
                             backref=db.backref('roles', lazy='joined'))

    def __init__(self, login, password, name, surname, email, active, role):
        self.login = login
        self.password = password
        self.user_name = name
        self.user_surname = surname
        self.user_email = email
        self.role = role
        self.user_active = active

    def __repr__(self):
        return '<User %r>' % (self.login)




#TABLE USERS ROLES
class Roles(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(30))
    role_symbol = db.Column(db.String(30))
 
    def __init__(self, name, symbol):
        self.role_name = name
        self.role_symbol = symbol

    def __repr__(self):
        return '<Role %r>' % (self.role_name)




#TABLE OBJECTS
class Objects(db.Model):
    object_id = db.Column(db.Integer, primary_key=True)
    object_name = db.Column(db.String(50))
    object_street = db.Column(db.String(50))
    object_city = db.Column(db.String(50))  
    object_postcode = db.Column(db.String(6))  
    object_localnumber = db.Column(db.String(10))     
    object_active = db.Column(db.Integer)
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.building_id'))
    building = db.relationship('Buildings',
                             backref=db.backref('buildings', lazy='joined'))
    def __init__(self, name, street, city, postcode, localnumber, active, building):
        self.object_name = name
        self.object_street = street
        self.object_city = city
        self.object_postcode = postcode
        self.object_localnumber = localnumber
        self.object_active = active
        self.building = building

    def __repr__(self):
        return '<Object %r>' % (self.object_name)




#TABLE BUILDINGS
class Buildings(db.Model):
    building_id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(30))
    building_active = db.Column(db.Integer)
 
    def __init__(self, name, active):
        self.building_name = name
        self.building_active = active

    def __repr__(self):
        return '<Building %r>' % (self.building_name)

