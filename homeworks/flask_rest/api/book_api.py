import http
from types import MethodType

from flask import Blueprint, Response, jsonify, make_response, request


book_router = Blueprint('book', __name__, url_prefix='/book')

books = [{"title":"first book","author":"an author","color":"red"}]

@book_router.route('')
def get_all():
        return jsonify(books)

@book_router.route('', methods=['POST'])
def add():
    book = {
            "title": request.json.get("title"),
            "author": request.json.get("author"),
            "color": request.json.get("color")
        }
    books.append(book)
    return jsonify(book), http.HTTPStatus.CREATED

@book_router.route('/<string:title>', methods=['GET'])
def get_by_title(title):    
    for book in books:
        if book["title"] == title:
            selectedbook= book    
    return jsonify(selectedbook)