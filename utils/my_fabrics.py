import os
from flask import Flask
from utils.config import *;
from flask_sslify import SSLify
from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager, get_jwt, verify_jwt_in_request


def create_app():

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    app.config.from_object(JWTConfig)
    jwt = JWTManager(app)

   #initialization of extension instances
#    mail.init_app(app)
#    mail.app = app

   # register the authentication blueprint
    from about.about import About
    from contacts.contacts import Contacts
    from market.market import Market
    from services.services import Services
    from work.work import Work
    from search.search import Search
    from useful.useful import Useful
    # from admin.admin import Admin
    from admin.admin import Admin

    app.register_blueprint(Contacts, url_prefix='/con')
    app.register_blueprint(About, url_prefix='/about')
    app.register_blueprint(Market, url_prefix='/mark')
    # app.register_blueprint(Market, url_prefix='/mark')
    app.register_blueprint(Services, url_prefix='/serv')
    app.register_blueprint(Work, url_prefix='/work')
    app.register_blueprint(Search, url_prefix='/sear')
    app.register_blueprint(Useful, url_prefix='/usef')
    app.register_blueprint(Admin, url_prefix='/adm')



    return app



class My_app_flask(Flask):
   def __init__(self):
      super().__init__(__name__)


      # self.app = Flask(__name__)
      self.config.from_object(FlaskConfig)
      self.config.from_object(JWTConfig)
      self.jwt = JWTManager(self)

      from about.about import About
      from contacts.contacts import Contacts
      from market.market import Market
      from services.services import Services
      from work.work import Work
      from search.search import Search
      from useful.useful import Useful
      # from admin.admin import Admin
      from admin.admin import Admin

      self.register_blueprint(Contacts, url_prefix='/con')
      self.register_blueprint(About, url_prefix='/about')
      self.register_blueprint(Market, url_prefix='/mark')
      # app.register_blueprint(Market, url_prefix='/mark')
      self.register_blueprint(Services, url_prefix='/serv')
      self.register_blueprint(Work, url_prefix='/work')
      self.register_blueprint(Search, url_prefix='/sear')
      self.register_blueprint(Useful, url_prefix='/usef')
      self.register_blueprint(Admin, url_prefix='/adm')





