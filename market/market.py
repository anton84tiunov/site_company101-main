from flask import Blueprint,render_template

Market = Blueprint('market', __name__,
                          template_folder='templates', static_folder='static')

@Market.route('/')
def market():
    return render_template('market/market.html')


