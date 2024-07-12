API_KEY = "AIzaSyDLI8JUaSbQxF7Fosg3YQWC-ZyVv1HKSTY"

def google_books_get_by_isbn(isbn: str) -> dict:
  import requests
  url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}"
  response = requests.get(url)
  if response.status_code != 200:
    raise Exception("Google Books API error")
  return response.json()