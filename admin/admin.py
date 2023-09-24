from flask import Blueprint,render_template

Admin = Blueprint('admin', __name__,
                          template_folder='templates', static_folder='static')


@Admin.route('/')
def admin():
    return render_template('admin/admin_authorization.html')


