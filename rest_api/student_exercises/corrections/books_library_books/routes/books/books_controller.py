import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask.views import MethodView
from flask_smorest import Blueprint

from utils.decorators import authenticated

from .dto.request.books_create import BooksCreate
from .dto.response.books_response import BooksResponse

from .books_service import BookService

books = Blueprint('books', 'books', url_prefix='/books', description='Books Library Books')
books_service = BookService()

@books.route('/')
class BooksCollection(MethodView):
  @authenticated
  @books.response(200, BooksResponse(many=True))
  def get(self):
    return books_service.get_all()


  @authenticated
  @books.arguments(BooksCreate)
  @books.response(201, BooksResponse)
  def post(self, new_book: dict):
    return books_service.create_book(new_book)