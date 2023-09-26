import logging
import sys, os, datetime, re, hashlib
from flask import Flask, render_template, url_for, request, redirect, json, jsonify
import traceback as tr
# from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager

from config import *;
# import db.myconnutils as db;
import myconnutils as db;
import my_loging as base_loger


from config import *;

from flask import Blueprint

from about.about import About
from contacts.contacts import Contacts
from market.market import Market
from services.services import Services
from work.work import Work
from search.search import Search
from useful.useful import Useful
from admin.admin import Admin


app = Flask(__name__)

app.config.from_object(FlaskConfig)
# app.config.from_object(JWTConfig)
# jwt = JWTManager(app)


app.register_blueprint(Contacts, url_prefix='/con')
app.register_blueprint(About, url_prefix='/about')
app.register_blueprint(Market, url_prefix='/mark')
# app.register_blueprint(Market, url_prefix='/mark')
app.register_blueprint(Services, url_prefix='/serv')
app.register_blueprint(Work, url_prefix='/work')
app.register_blueprint(Search, url_prefix='/sear')
app.register_blueprint(Useful, url_prefix='/usef')
app.register_blueprint(Admin, url_prefix='/adm')


# обработка данных на странице home.html
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        dat = request.json
        print(dat.get('name'))
        print(dat.get('age'))
        data = db.my_querys()
        return jsonify(json.dumps(data, indent=2) )
    
    if request.method == 'GET':
        list_images = os.listdir('./static/img/slider_home')
        return render_template('home/home.html', slider_images = list_images, path_to_slider = "/static/img/slider_home/")


@app.route('/home_test/', methods=['POST', 'GET'])
def home_test():

    if request.method == 'POST':

        try:
            ssssss()
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            str_err = 'сообщение: << {} >> . файл: {}  . строка: {} .  где: {}'.format(e,
                error.filename,
                error.lineno,
                error.line
                )
            base_loger.set_log("app", str_err)
        dat = request.json
        print(dat.get('name'))
        print(dat.get('age'))
        data = db.my_querys()
        return jsonify(json.dumps(data, indent=2) )

def main():
    app.run(host=server_host, port=server_port)



if __name__ == '__main__':
    main()


