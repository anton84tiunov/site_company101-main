from flask import Blueprint,render_template

Contacts = Blueprint('contacts', __name__,
                          template_folder='templates', static_folder='static')

@Contacts.route('/')
def contacts():
    return render_template('contacts/contacts.html')


