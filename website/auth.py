from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=["GET", "POST"])
def register():
    
     if request.method == 'POST':
          email = request.form.get('email')
          if len(email) < 10: flash("Not a valid email address", category='error')
          else: 
               new_user = User(email=email)
               db.session.add(new_user)
               db.session.commit()
               flash("Thank you, email submitted.", category="success")
               return redirect(url_for("views.home"))
               

    
     return render_template("register.html")