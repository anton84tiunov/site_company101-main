from flask import Blueprint,render_template

Search = Blueprint('search', __name__,
                          template_folder='templates', static_folder='static')

@Search.route('/')
def search():
    return render_template('search/search.html')


