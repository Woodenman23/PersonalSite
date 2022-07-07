from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=["GET", "POST"])
def register():
     data = request.form
     if request.method == 'POST':
          email = data.get('email')

          flash("Not a valid email address", category='error')
       


    
     return render_template("register.html")