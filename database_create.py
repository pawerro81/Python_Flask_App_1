from application import app
from application.models import *

# PAWERRO81
# CREATE DATABASE 
# 

with app.app_context():
   db.drop_all()
   db.create_all()
   
   role1 = Roles("Admin","admin")
   role2 = Roles("Technik","technik")
   role3 = Roles(u"Właściciel","wlasciciel")
   role4 = Roles("Kierownik","kierownik")

   user1 = Users("a","a",u"Paweł",u"Pasternak","pavelo@gmail.com",1,role1)

   building1 = Buildings("budynek1",1)
   
   object1 = Objects("Obiekt1",u"Marszałkowska","Warszawa","00-891","111/1",1,building1)
   object2 = Objects("Obiekt2",u"Marszałkowska","Warszawa","00-891","111/2",1,building1)
   
   db.session.add(role1)
   db.session.add(role2)
   db.session.add(role3)
   db.session.add(role4)
   
   db.session.add(user1)
   
   db.session.add(building1)
   
   db.session.add(object1)
   db.session.add(object2)

   db.session.commit()

