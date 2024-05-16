from flask.views import MethodView
from flask_smorest import Blueprint

from .books_service import BooksService
from .dto.response.books_reponse import BookFullResponse, BooksResponse
from .dto.request.books_create import CreateBook
from .books_mapper import to_entity


books = Blueprint("books", "books", url_prefix="/books", description="books routes")

books_service = BooksService()

@books.route("/")
class BooksController(MethodView):
  @books.response(status_code=200, schema=BooksResponse)
  def get(self):
    return {"books": books_service.get_all()}
  
  @books.arguments(CreateBook)
  @books.response(status_code=201, schema=BookFullResponse)
  def post(self, book: dict):
    return books_service.create_book(to_entity(book))