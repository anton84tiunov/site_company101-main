from flask import Blueprint,render_template

Work = Blueprint('work', __name__,
                          template_folder='templates', static_folder='static')

@Work.route('/')
def work():
    return render_template('work/work.html')


