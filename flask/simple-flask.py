from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return '<!-- contenu de index.html ...'

@app.route('/page.html')
def page():
    """
    retourne le contenu de la page page.html
    """
    return '<!-- contenu de page.html ...'
