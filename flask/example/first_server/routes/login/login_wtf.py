import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask import Blueprint, request, render_template
from forms.login import RegisterForm

wtf_login = Blueprint("wtf_login", __name__, url_prefix="/wtf")

@wtf_login.route("/login")
def login_wtf_func():
  return ""

@wtf_login.route("/register", methods=["GET", "POST"])
def register_wtf():
  form = RegisterForm(request.form)
  if form.validate():
    email = form.email.data
    pwd = form.pwd.data
    pwd_confirm = form.pwd_confirm.data
    return f'Email: {email}, Password: {pwd}, Confirm password: {pwd_confirm}'
  return render_template('login/wtf/register.html', form=form)

@wtf_login.route("/register/macro", methods=["GET", "POST"])
def register_wtf_macro():
  form = RegisterForm(request.form)
  if form.validate():
    email = form.email.data
    pwd = form.pwd.data
    pwd_confirm = form.pwd_confirm.data
    return f'Email: {email}, Password: {pwd}, Confirm password: {pwd_confirm}'
  return render_template('login/wtf/register_macro.html', form=form)