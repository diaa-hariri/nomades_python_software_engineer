class Book:
  def __init__(self, isbn:str="", title: str="", authors: list=[]) -> None:
    self.isbn = isbn
    self.title = title
    self.authors = authors
  
  def __repr__(self) -> str:
    return f"{self.isbn} => {self.title} written by {self.authors})"