from flask import Blueprint,render_template

About = Blueprint('about', __name__,
                          template_folder='templates', static_folder='static')

@About.route('/')
def about():
    return render_template('about/about.html')


