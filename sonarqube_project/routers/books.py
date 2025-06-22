from flask import Blueprint, request, jsonify
from sonarqube_project.services import book_service

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(book_service.get_all_books())

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.json
    # Missing input validation - SonarQube issue
    book = book_service.create_book(data)
    return jsonify(book), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = book_service.update_book(book_id, data)
    # Bug: a TypeError will be raised if book is None
    if book['id']:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_service.delete_book(book_id):
        return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books/author/<author_name>', methods=['GET'])
def get_books_by_author(author_name):
    # Unused variable - SonarQube issue
    some_unused_variable = "test"
    books = book_service.find_books_by_author(author_name)
    return jsonify(books) 