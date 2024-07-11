class User():
  def __init__(self, id="", firstname="", lastname="", username="", password="", salt="", *args, **kwrgs):
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
    self.salt = salt
  
  def __repr__(self):
    return f"<User {self.username}>"
