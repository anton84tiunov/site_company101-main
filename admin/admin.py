import sys, os, datetime, re, hashlib
import logging
from flask import Flask, Blueprint, render_template, url_for, request, redirect, json, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager, get_jwt, verify_jwt_in_request
from flask_sslify import SSLify
from pkg_resources import require
from werkzeug.utils import secure_filename
import utils.myconnutils as db;
import utils.my_loging as base_loger
import redis

from werkzeug.datastructures import ImmutableMultiDict
# from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager





Admin = Blueprint('admin', __name__,
                          template_folder='templates', static_folder='static')


@Admin.route('/')
def admin():
    return render_template('admin/admin_authorization.html')

@Admin.route('/log/')
def admin_log():
    if os.path.isfile("my_logs/all.log"):
        text = open("my_logs/all.log","r", encoding="utf-8").read()
    else:
        text = "не найдено"
    return render_template('admin/log.html', text=text)



# # обрабатывает запрос при регистрации

@Admin.route('/reg/', methods=['GET', 'POST'])
def registration_user():
    if request.method == 'GET':
        return render_template('admin/admin_registration.html')
    if request.method == 'POST':
    
        print(type(jsonify(request.get_json())))
        print(jsonify(request.get_json()))
        return jsonify(request.get_json())
        # request_data = request.get_json()
        # print(request_data)
        # name = request_data['name']
        # patronymic = request_data['patronymic']
        # surname = request_data['surname']
        # datebirth = request_data['datebirth'][0:10]
        # phone = request_data['phone']
        # email = request_data['email']
        # login = request_data['login']
        # password = request_data['password']
        # if name == None or name == '' or len(name) < 2 or not re.fullmatch("[A-Za-z]{2,}", name)\
        #         or patronymic == None or patronymic == '' or len(patronymic) < 2 or not re.fullmatch("[A-Za-z]{2,}", patronymic)\
        #         or surname == None or surname == '' or len(surname) < 2 or not re.fullmatch("[A-Za-z]{2,}", surname)\
        #         or not re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", datebirth)\
        #         or phone == None or phone == '' or len(phone) != 11 or not re.fullmatch(r"[0-9]{11}", phone)\
        #         or email == None or email == '' or len(email) < 7 or not re.fullmatch(r"^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", email)\
        #         or login == None or login == '' or len(login) < 2 or not re.fullmatch("[A-Za-z0-9]{2,}", login)\
        #         or password == None or password == ''  or len(password) < 8 :
        #         # or request_data['password'] == None or request_data['password'] == ''  or len(request_data['password']) < 8 or not re.fullmatch('[A-Z]', request_data['password']) or not re.fullmatch('[a-z]', request_data['password']) or not re.fullmatch('[0-9]', request_data['password']) or not re.fullmatch('[@#$%^&*]', request_data['password']):
           
        #     return jsonify({'status': 5})

        # salt = os.urandom(32)
        # key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 8351)
        # storage = salt + key 
        # print(storage)
        # print(datebirth)

        # bool = db.insert_user(name, patronymic, surname, phone, datetime.datetime.strptime(datebirth, '%Y-%m-%d').date(), email, login, storage)
        # print(type(bool))
        # return jsonify({'status': bool}) 


# обрабатывает запрос при авторизации

@Admin.route('/auth/', methods=['GET', 'POST'])
def authorization_user():
    if request.method == 'GET':
        return render_template('admin/admin_authorization.html')
    if request.method == 'POST':
        request_data = request.get_json()
        login = request_data['login']
        password = request_data['password']
        print(request_data)
        if login == None or login == '' or len(login) < 2 or not re.fullmatch("[A-Za-z0-9]{2,}", login)\
                or password == None or password == ''  or len(password) < 8 :
            return jsonify({'status': 5})

        db_pass = db.select_user_password(login)
        if db_pass == '':
            return jsonify({'status': 0})
        salt_db = db_pass[:32]
        key_db = db_pass[32:]
        if key_db == hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_db, 8351):
            access_token = create_access_token(identity=login)
            refresh_token = create_refresh_token(identity=login)
            return jsonify({'status': 1, 'access_token': access_token, 'refresh_token': refresh_token})
        else :
          return jsonify({'status': 2})


@Admin.route('/test_jwt', methods=['POST'])
@jwt_required()
def test_jwt():
    request_data = request.get_json()
    print(request_data)
    return jsonify({'ok?': 'ok ok ok'})


@Admin.route("/refresh_jwt", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    request_data = request.get_json()
    print(request_data)
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)
    return jsonify({'status': '1', 'access_token': access_token, 'refresh_token': refresh_token})
