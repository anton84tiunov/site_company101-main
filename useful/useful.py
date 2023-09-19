from flask import Blueprint,render_template

Useful = Blueprint('useful', __name__,
                          template_folder='templates', static_folder='static')

@Useful.route('/')
def useful():
    return render_template('useful/useful.html')


