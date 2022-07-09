from flask import Flask

from api.user_api import user_router
from api.book_api import book_router
app = Flask(__name__)

app.register_blueprint(user_router)
app.register_blueprint(book_router)


status_code_created = 201


@app.route('/')
def index():
    return "hello world12"


if __name__ == '__main__':
    app.run(port=5000,  host='0.0.0.0',debug=True)
