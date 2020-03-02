from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)
print(__name__)
# Creamos una lista de 2 diccionarios

books = [
    {
        'name': 'El despertar de la fuerza',
        'price': '7.99',
        'isbn': 630157748
    },
    {
        'name': 'El retorno del Yedi',
        'price': '10.99',
        'isbn': 1254782114
    }
]


def valid_book_object(book_object):
    if "name" in book_object and "price" in book_object and "isbn" in book_object:
        return True
    else:
        return False


@app.route('/')
def hello_world():
    return 'TotesPutes'


# GET /books/ISBN_NUMBER
@app.route('/books')
def get_books():
    return jsonify({'libros': books})


# POST /books. This method allow users to add new books to the dictionary
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if valid_book_object(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
# Esto sirve para devolver un 201 response, content created.
        response = Response("",201, mimetype='application/json')
        response.headers['Location'] = "books/" + str(new_book['isbn'])
        return response
    else:
        invalid_book_error_msg = {
            "error": "Invalid book objet passed in request",
            "helpString": "Data passed in similar to thist"
        }
        response = Response(json.dumps(invalid_book_error_msg), status=400, mimetype='application/json')
        return response
# GET /books
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name:': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)


app.run(port=5000)
