from flask import Blueprint,render_template

Services = Blueprint('services', __name__,
                          template_folder='templates', static_folder='static')

@Services.route('/')
def services():
    return render_template('services/services.html')


