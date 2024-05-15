from .user import User
from .dto.response.user_response import UserResponse

from firebase_admin.firestore import DocumentReference, DocumentSnapshot

def toUserResponse(user: User) -> UserResponse:
  return UserResponse().dump(user)


def toDict(user: User) -> dict:
  return {
    "id": user.id,
    "firstname": user.firstname,
    "lastname": user.lastname,
    "username": user.username,
    "email": user.email,
    "password": user.password,
    "salt": user.salt,
  }

def toEntity(user_data: dict | DocumentReference | DocumentSnapshot) -> User:
  u = User()
  if isinstance(user_data, DocumentReference):
    u.id = user_data.id
    user_data = user_data.get().to_dict()
    u.salt = user_data["salt"]
  elif isinstance(user_data, DocumentSnapshot):
    u.id = user_data.id
    user_data = user_data.to_dict()
    u.salt = user_data["salt"]
  
  u.firstname = user_data["firstname"]
  u.lastname = user_data["lastname"]
  u.username = user_data["username"]
  u.email = user_data["email"]
  u.password = user_data["password"]
  return u
