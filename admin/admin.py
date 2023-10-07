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

from utils.config import *;
from utils.my_fabrics import create_app

from werkzeug.datastructures import ImmutableMultiDict
# from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager



Admin = Blueprint('admin', __name__,
                          template_folder='templates', static_folder='static')
# app = create_app()

# Admin.config.from_object(JWTConfig)
# e

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
        request_data = request.get_json()

        surname = request_data['usersurname']
        name = request_data['username']
        patronymic = request_data['userpatronymic']
        phone = request_data['userphone']
        datebirth = request_data['userdate_birth']
        email = request_data['useremail']
        login = request_data['userlogin']
        password = request_data['pass1']

        if name == None or name == '' or len(name) < 2 or not re.fullmatch("^[A-Za-z]{2,15}$", name)\
                or patronymic == None or patronymic == '' or len(patronymic) < 2 or not re.fullmatch("^[A-Za-z]{2,15}$", patronymic)\
                or surname == None or surname == '' or len(surname) < 2 or not re.fullmatch("^[A-Za-z]{2,15}$", surname)\
                or not re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", datebirth)\
                or phone == None or phone == '' or len(phone) != 11 or not re.fullmatch(r"8[0-9]{10}", phone)\
                or email == None or email == '' or len(email) < 7 or not re.fullmatch(r"^[a-z0-9.]{2,20}@[a-z0-9.]{2,10}$$", email)\
                or login == None or login == '' or len(login) < 2 or not re.fullmatch("^[a-zA-Z0-9_]{2,15}$", login)\
                or password == None or password == ''  or len(password) < 8 or not re.fullmatch("^.*(?=.{8,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$", password):
                # or request_data['password'] == None or request_data['password'] == ''  or len(request_data['password']) < 8 or not re.fullmatch('[A-Z]', request_data['password']) or not re.fullmatch('[a-z]', request_data['password']) or not re.fullmatch('[0-9]', request_data['password']) or not re.fullmatch('[@#$%^&*]', request_data['password']):

            print("status 5")
            base_loger.set_log("app", str(request_data) + "def registration_user() validation" )
            return jsonify({'status': 5})

        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 83)
        storage = salt + key 
        # print("storage", type(storage), storage)

        bool = db.insert_user( surname, name, patronymic, phone, datetime.datetime.strptime(datebirth, '%Y-%m-%d').date(), email, login, storage)
        print(type(bool))
        print(bool)
        return jsonify({'status': bool}) 


# обрабатывает запрос при авторизации

@Admin.route('/auth/', methods=['GET', 'POST'])
def authorization_user():
    if request.method == 'GET':
        return render_template('admin/admin_authorization.html')
    if request.method == 'POST':
        request_data = request.get_json()
        login = request_data['login']
        password = request_data['pass']
        if login == None or login == '' or len(login) < 2 or not re.fullmatch("[A-Za-z0-9]{2,}", login)\
                or password == None or password == ''  or len(password) < 8 :
            return jsonify({'status': 5})

        db_pass = db.select_user_password(login)
        if db_pass == '':
            return jsonify({'status': 3})
        salt_db = db_pass[:32]
        key_db = db_pass[32:]
        if key_db == 'error':
            return jsonify({'status': 4})
        key_brow = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_db, 83)
        if key_db == key_brow:
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

    
# db_pass     <class 'bytes'> b'.\x1bd\xa2.\xbb\xa6BQ\xcd\x83.\xef\xe1Yw\x05\xf8\x98\xdb\xdd\xbc\xa2P\x8a\xb8\xe0\xc2\xa8\xc1R\xfd\xf9\xf8\xd12\xe19\xab>\xb8.q(\xc3o\xe43W,\x1c\x13s\x85\x02M/\x84\\,0\x90n\xb8'
# key_brow    <class 'bytes'> b'\xf9\xf8\xd12\xe19\xab>\xb8.q(\xc3o\xe43W,\x1c\x13s\x85\x02M/\x84\\,0\x90n\xb8'
