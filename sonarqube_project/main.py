from flask import Flask
from sonarqube_project.routers.books import books_bp

app = Flask(__name__)

app.register_blueprint(books_bp)

if __name__ == '__main__':
    # Setting debug to True is a security hotspot that SonarQube will flag
    app.run(debug=True)
