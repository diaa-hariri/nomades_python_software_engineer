from flask import session, redirect, url_for
from functools import wraps

def authenticated(func):
  @wraps(func)
  def inner_func(*args, **kwargs):
    if not ("loggedin" in session and session["loggedin"]):
      return redirect(url_for("login"))
    return func(*args, **kwargs)
  
  return inner_func