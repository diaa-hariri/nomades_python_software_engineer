from flask import Flask
from flask_smorest import Api

from routes.users.users_controller import users
from routes.books.books_controller import books

server = Flask(__name__)

class APIConfig:
  API_TITLE = "Books Library API V1"
  API_VERSION = "v1"
  OPENAPI_VERSION = "3.0.2"
  OPENAPI_URL_PREFIX = "/"
  OPENAPI_SWAGGER_UI_PATH = "/docs"
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  OPENAPI_REDOC_PATH = "/redoc"
  OPENAPI_REDOC_UI_URL = "https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js"

server.config.from_object(APIConfig)

api = Api(server)

api.register_blueprint(users)
api.register_blueprint(books)

@server.route("/")
def index():
  return {"message": "Hello, World!"}

if __name__ == "__main__":
  server.run(debug=True, port=8080, host="0.0.0.0")