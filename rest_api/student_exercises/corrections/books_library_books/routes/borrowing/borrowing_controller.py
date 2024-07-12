import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask_smorest import Blueprint

from utils.decorators import authenticated

from .borrowing_service import BorrowingSeervice
from .dto.request.borrow_request import BorrowingRequest
from .dto.response.borrow_response import BorrowResponse, BorrowBookResponse

borrowing = Blueprint("borrowing", "borrowing", url_prefix="/borrowing", description="Borrowing operations")

borrowing_service = BorrowingSeervice()

@borrowing.route("/<book_id>", methods=["POST"])
@authenticated
@borrowing.arguments(BorrowingRequest)
@borrowing.response(status_code=201, schema=BorrowResponse)
@borrowing.response(status_code=400)
def borrow_book(borrow: dict, book_id: str):
  try:
    return borrowing_service.create_borrowing(book_id, borrow), 201
  except ValueError as e:
    return {"error": str(e)}, 400

@borrowing.route("/mine")
@authenticated
@borrowing.response(status_code=200, schema=BorrowBookResponse(many=True))
def get_my_borrowings():
  return borrowing_service.get_all_mine()