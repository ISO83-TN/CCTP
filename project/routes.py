from flask import Blueprint, render_template

# Créer un blueprint nommé 'main'
main = Blueprint('main', __name__)

@main.route('/')
def home():
    projects = [
        {"id": 1, "name": "Projet A", "client": "Client X"},
        {"id": 2, "name": "Projet B", "client": "Client Y"}
    ]
    return render_template('home.html', projects=projects)

@main.route('/test')
def test():
    return render_template('test.html')
