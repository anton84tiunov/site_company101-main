
import sys, os, datetime, re, hashlib
import logging
from flask import Flask, render_template, url_for, request, redirect, json, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager, get_jwt, verify_jwt_in_request
from flask_sslify import SSLify
from pkg_resources import require
from werkzeug.utils import secure_filename
import redis

from werkzeug.datastructures import ImmutableMultiDict
# from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager

from utils.config import *;
# import db.myconnutils as db;
import utils.myconnutils as db;
import utils.my_loging as base_loger
from flask import Blueprint
from utils.my_fabrics import create_app, My_app_flask

# from about.about import About
# from contacts.contacts import Contacts
# from market.market import Market
# from services.services import Services
# from work.work import Work
# from search.search import Search
# from useful.useful import Useful
# # from admin.admin import Admin
# from admin.admin import Admin

# app = Flask(__name__)

# app = create_app()
app = My_app_flask()
# app = my_app_flask.app()
# app.config.from_object(FlaskConfig)
# app.config.from_object(JWTConfig)
# jwt = JWTManager(app)
# context = ('./ssl/flutter_flask.crt', './ssl/flutter_flask.key')
# sslify = SSLify(app)


# app.register_blueprint(Contacts, url_prefix='/con')
# app.register_blueprint(About, url_prefix='/about')
# app.register_blueprint(Market, url_prefix='/mark')
# # app.register_blueprint(Market, url_prefix='/mark')
# app.register_blueprint(Services, url_prefix='/serv')
# app.register_blueprint(Work, url_prefix='/work')
# app.register_blueprint(Search, url_prefix='/sear')
# app.register_blueprint(Useful, url_prefix='/usef')
# app.register_blueprint(Admin, url_prefix='/adm')


# # Настройте наше соединение Redis для хранения заблокированных токенов. Вы, вероятно,
# # хотите, чтобы ваш экземпляр redis был настроен на сохранение данных на диск, чтобы перезагрузка
# # не заставляет ваше приложение забывать, что JWT был отозван.
# jwt_redis_blocklist = redis.StrictRedis(
#     host="localhost", port=6379, db=0, decode_responses=True
# )

# # Функция обратного вызова для проверки наличия JWT в черном списке Redis
# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     token_in_redis = jwt_redis_blocklist.get(jti)
#     return token_in_redis is not None


# # Конечная точка для отзыва токена доступа текущего пользователя. Сохраните уникальные JWT
# # идентификатор (jti) в redis. Также установите время жизни (TTL) при сохранении JWT.
# # чтобы он автоматически удалялся из Redis после истечения срока действия токена.
# @app.route("/logout", methods=["DELETE"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     try:
#         jwt_redis_blocklist.set(jti, "", ex=JWTConfig.JWT_ACCESS_TOKEN_EXPIRES)
#         return jsonify(msg="Access token revoked", status=1)
#     except:
#         return jsonify(msg="Access token mot revoked", status=0)




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
        dat = request.json
        print(dat.get('name'))
        print(dat.get('age'))

        data = {}
        
        try:
            data = db.my_querys()
            base_loger.set_log("app", str(data))
        except Exception as e:
            str_err = base_loger.msg_except(e)
            base_loger.set_log("app", str_err)
        
        return jsonify(json.dumps(data, indent=2) )


def main():
    context = ('./ssl/flutter_flask.crt', './ssl/flutter_flask.key')
    app.run(host=server_host, port=server_port, ssl_context = context)




if __name__ == '__main__':
    main()







# from functools import cache, wraps
# import json
# import sys, os, datetime, re, hashlib
# import redis

# from flask import Flask, jsonify, request , Response 
# from flask_jwt_extended import create_access_token, create_refresh_token,  get_jwt_identity, jwt_required, JWTManager, get_jwt, verify_jwt_in_request
# from flask_sslify import SSLify
# from pkg_resources import require
# from werkzeug.utils import secure_filename

# from werkzeug.datastructures import ImmutableMultiDict

# from config import *;
# import db.myconnutils as db;

# app = Flask(__name__)
# app.config.from_object(FlaskConfig)
# app.config.from_object(JWTConfig)
# jwt = JWTManager(app)
# context = ('./ssl/flutter_flask.crt', './ssl/flutter_flask.key')
# sslify = SSLify(app)


# ###############################################################################
                        
# #                                    redis                                    #

# ############################################################################### 


# # Настройте наше соединение Redis для хранения заблокированных токенов. Вы, вероятно,
# # хотите, чтобы ваш экземпляр redis был настроен на сохранение данных на диск, чтобы перезагрузка
# # не заставляет ваше приложение забывать, что JWT был отозван.
# jwt_redis_blocklist = redis.StrictRedis(
#     host="localhost", port=6379, db=0, decode_responses=True
# )

# # Функция обратного вызова для проверки наличия JWT в черном списке Redis
# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     token_in_redis = jwt_redis_blocklist.get(jti)
#     return token_in_redis is not None


# # Конечная точка для отзыва токена доступа текущего пользователя. Сохраните уникальные JWT
# # идентификатор (jti) в redis. Также установите время жизни (TTL) при сохранении JWT.
# # чтобы он автоматически удалялся из Redis после истечения срока действия токена.
# @app.route("/logout", methods=["DELETE"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     try:
#         jwt_redis_blocklist.set(jti, "", ex=JWTConfig.JWT_ACCESS_TOKEN_EXPIRES)
#         return jsonify(msg="Access token revoked", status=1)
#     except:
#         return jsonify(msg="Access token mot revoked", status=0)

# ###############################################################################
                        
# #                                    users                                    #

# ###############################################################################

# # обрабатывает запрос при регистрации

# @app.route('/registration', methods=['GET', 'POST'])
# def registration_user():
#     if request.method == 'GET':
#         print('m get')
#     if request.method == 'POST':
#         request_data = request.get_json()
#         print(request_data)
#         name = request_data['name']
#         patronymic = request_data['patronymic']
#         surname = request_data['surname']
#         datebirth = request_data['datebirth'][0:10]
#         phone = request_data['phone']
#         email = request_data['email']
#         login = request_data['login']
#         password = request_data['password']
#         if name == None or name == '' or len(name) < 2 or not re.fullmatch("[A-Za-z]{2,}", name)\
#                 or patronymic == None or patronymic == '' or len(patronymic) < 2 or not re.fullmatch("[A-Za-z]{2,}", patronymic)\
#                 or surname == None or surname == '' or len(surname) < 2 or not re.fullmatch("[A-Za-z]{2,}", surname)\
#                 or not re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", datebirth)\
#                 or phone == None or phone == '' or len(phone) != 11 or not re.fullmatch(r"[0-9]{11}", phone)\
#                 or email == None or email == '' or len(email) < 7 or not re.fullmatch(r"^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", email)\
#                 or login == None or login == '' or len(login) < 2 or not re.fullmatch("[A-Za-z0-9]{2,}", login)\
#                 or password == None or password == ''  or len(password) < 8 :
#                 # or request_data['password'] == None or request_data['password'] == ''  or len(request_data['password']) < 8 or not re.fullmatch('[A-Z]', request_data['password']) or not re.fullmatch('[a-z]', request_data['password']) or not re.fullmatch('[0-9]', request_data['password']) or not re.fullmatch('[@#$%^&*]', request_data['password']):
           
#             return jsonify({'status': 5})

#         salt = os.urandom(32)
#         key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 8351)
#         storage = salt + key 
#         print(storage)
#         print(datebirth)

#         bool = db.insert_user(name, patronymic, surname, phone, datetime.datetime.strptime(datebirth, '%Y-%m-%d').date(), email, login, storage)
#         print(type(bool))
#         return jsonify({'status': bool}) 


# # обрабатывает запрос при авторизации

# @app.route('/authorization', methods=['GET', 'POST'])
# def authorization_user():
#     if request.method == 'GET':
#         print('authorization get')
#     if request.method == 'POST':
#         request_data = request.get_json()
#         login = request_data['login']
#         password = request_data['password']
#         print(request_data)
#         if login == None or login == '' or len(login) < 2 or not re.fullmatch("[A-Za-z0-9]{2,}", login)\
#                 or password == None or password == ''  or len(password) < 8 :
#             return jsonify({'status': 5})

#         db_pass = db.select_user_password(login)
#         if db_pass == '':
#             return jsonify({'status': 0})
#         salt_db = db_pass[:32]
#         key_db = db_pass[32:]
#         if key_db == hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_db, 8351):
#             access_token = create_access_token(identity=login)
#             refresh_token = create_refresh_token(identity=login)
#             return jsonify({'status': 1, 'access_token': access_token, 'refresh_token': refresh_token})
#         else :
#           return jsonify({'status': 2})


# @app.route('/test_jwt', methods=['POST'])
# @jwt_required()
# def test_jwt():
#     request_data = request.get_json()
#     print(request_data)
#     return jsonify({'ok?': 'ok ok ok'})


# @app.route("/refresh_jwt", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     request_data = request.get_json()
#     print(request_data)
#     identity = get_jwt_identity()
#     access_token = create_access_token(identity=identity)
#     refresh_token = create_refresh_token(identity=identity)
#     return jsonify({'status': '1', 'access_token': access_token, 'refresh_token': refresh_token})


# ###############################################################################
                        
# #                                 categories                                  #

# ###############################################################################


# @app.route('/create_category', methods=['POST'])
# @jwt_required()
# def create_category():
#     request_data = request.get_json()
#     print(request_data)
#     category_name = request_data['category_name']
#     category_discription = request_data['category_discription']
#     identity = get_jwt_identity()
#     user_id = db.select_user_id(identity)

#     if category_name == None or category_name == '' or len(category_name) < 2 or not re.fullmatch("[A-Za-z]{2,}", category_name)\
#                 or category_discription == None or category_discription == '' or len(category_discription) < 2 :
#         return jsonify({'status': '5'})
#     res = 'ok'
#     print(res)
#     res = db.insert_category(category_name, category_discription, user_id)
#     return jsonify({'ok?': str(res)})


# @app.route('/select_categories', methods=['POST'])
# @jwt_required()
# def select_categories():
#     request_data = request.get_json()
#     categories = db.select_categories()
#     # db.select_categories_count
#     print(request_data)
#     return jsonify({'categories': categories})

# @app.route('/select_categories_count', methods=['POST'])
# @jwt_required()
# def select_categories_count():
#     request_data = request.get_json()
#     categories = db.select_categories_count()
#     print(request_data)
#     return jsonify({'categories': categories})



# ###############################################################################
                        
# #                                     ads                                    #

# ###############################################################################


# @app.route('/create_ad', methods=['POST'])
# @jwt_required()
# def create_ad():
#     request_data = request.get_json()
#     print(request_data)
#     ad_name = request_data['ad_name']
#     ad_categories = request_data['ad_categories']
#     ad_price = request_data['ad_price']
#     ad_phones = request_data['ad_phones']
#     ad_mails = request_data['ad_mails']
#     ad_discription = request_data['ad_discription']
#     # ad_photes = request_data['ad_photes']
#     ad_photes = '/' + get_jwt_identity()

#     identity = get_jwt_identity()
#     ad_owner = db.select_user_id(identity)

#     ad_categories_id = db.select_category_id(ad_categories)

#     if ad_name == None or ad_name == '' or len(ad_name) < 2 \
#                 or ad_owner == None  \
#                 or ad_categories_id == None or ad_categories_id == '' \
#                 or ad_price == None  \
#                 or ad_discription == None or ad_discription == '' or len(ad_discription) < 2 :
#         return jsonify({'status': '5'})
#     res = 'ok'
#     # print(res)
#     res = db.insert_ad(ad_name, ad_categories_id, ad_price, ad_phones, ad_mails,ad_discription, ad_photes, ad_owner)
#     return jsonify({'status': str(res)})

# @app.route('/select_category_ads', methods=['POST'])
# @jwt_required()
# def select_category_ads():
#     request_data = request.get_json()
#     ad_category = request_data['category']
#     ad_category_id = db.select_category_id(ad_category)
    
#     ads = db.select_category_ads(ad_category_id)
#     print(ads)
#     return jsonify({'ads': ads})


# @app.route('/select_category_ads2', methods=['POST'])
# @jwt_required()
# def select_category_ads2():
#     request_data = request.get_json()
#     ad_category = request_data['category']
#     ad_category_id = db.select_category_id(ad_category)
    
#     ads = db.select_category_ads2(ad_category_id)
#     print(ads)
#     # print(sys.getsizeof(ads))
#     return jsonify({'ads': ads})


# @app.route('/select_user_ads', methods=['POST'])
# @jwt_required()
# def select_user_ads():
#     request_data = request.get_json()
#     identity = get_jwt_identity()
#     user_id = db.select_user_id(identity)
    
#     ads = db.select_user_ads(user_id)
#     print(ads)
#     return jsonify({'ads': ads})

# @app.route('/update_ad', methods=['POST'])
# @jwt_required()
# def update_ad():
#     request_data = request.get_json()


#     ad_id = request_data['ad_id']
#     ad_name = request_data['ad_name']
#     ad_price = request_data['ad_price']
#     ad_phones = request_data['ad_phones']
#     ad_mails = request_data['ad_mails']
#     ad_discription = request_data['ad_discription']


#     identity = get_jwt_identity()
#     ad_owner = db.select_user_id(identity)

#     if ad_name == None or ad_name == '' or len(ad_name) < 2 \
#                 or ad_id == None \
#                 or ad_price == None  \
#                 or ad_phones == None\
#                 or ad_mails == None\
#                 or ad_discription == None or ad_discription == '' or len(ad_discription) < 2 :
#         return jsonify({'status': '5'})
#     # res = 'ok'
#     # print(res)
#     res = db.update_ad(ad_name, ad_price, ad_discription, ad_phones, ad_mails, ad_id, ad_owner)
#     print(res)
#     return jsonify({'status': str(res)})






# ###############################################################################
                        
# #                              my decorator                                  #

# ###############################################################################

# def admin_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             try:

#                 verify_jwt_in_request()
#                 claims = get_jwt()
#                 print('claims', claims)
#                 if claims["toha"]:
#                     return fn(*args, **kwargs)
#                 else:
#                     return jsonify(msg="Admins only!"), 403
#             except:
#                 e = sys.exc_info()
#                 print(e)
#                 print(e)
#             return jsonify(msg="Admins only!"), 403
#         return decorator

#     return wrapper

# ###############################################################################
                        
# #                                     file                                   #

# ###############################################################################

# @app.route('/upload_file', methods=['POST'])
# @jwt_required()
# # @admin_required()
# def upload_file():
#     parsed_string = json.loads(request.form['my_data'])
#     print(type(parsed_string['map']['1']))

#     identity = get_jwt_identity()
#     print(identity)

#     print(request.files)
#     file = request.files['file']
#     if not os.path.isdir('app/image/' + identity):
#         os.mkdir('app/image/' + identity)
#     filename = secure_filename(file.filename)
#     file.save(os.path.join('app/image/' + identity + '/', filename))

#     return jsonify({'ads': 'ads'})


# if __name__ == '__main__':
#     # app.run(host=server_host, port=server_port)
#     context = ('./ssl/flutter_flask.crt', './ssl/flutter_flask.key')
#     app.run(host=server_host, port=server_port, ssl_context = context)




# method        request <class 'str'>
# scheme        request <class 'str'>
# server        request <class 'tuple'>
# root_path     request <class 'str'> 
# path          request <class 'str'>
# query_string  request <class 'bytes'>
# headers       request <class 'werkzeug.datastructures.EnvironHeaders'>
# remote_addr   request <class 'str'>
# environ       request <class 'dict'>
# shallow       request <class 'bool'>
# url_rule      request <class 'werkzeug.routing.Rule'>
    # rule                         request <class 'str'>
    # is_leaf                      request <class 'bool'>
    # map                          request <class 'werkzeug.routing.Map'>
    # strict_slashes
    # merge_slashes
    # subdomain
    # host
    # defaults
    # build_only
    # alias
    # websocket
    # methods
    # endpoint# default_mimetype
# json_module
# autocorrect_location_header
# max_cookie_size















# __module__
# __doc__
# default_mimetype
# json_module
# autocorrect_location_header
# max_cookie_size




# {
# 'method': 'POST'
# , 'scheme': 'https',
#  'server': ('192.168.1.82', 3345), 
# 'root_path': '', 
# 'path': '/upload_file',
#  'query_string': b'', 
# 'headers': EnvironHeaders(
# [
# ('User-Agent', 'Dart/2.17 (dart:io)'),
#  ('Acceptheader', 'application/json'),
#  ('Accept-Encoding', 'gzip'),
#  ('Content-Length', '105943'),
#  ('Host', '192.168.1.82:3345'),
#  ('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTMxNTg0OCwianRpIjoiM2U0OGVlNWQtOWI1YS00MmRiLWFiMzYtN2NmMjM5OWEzOTU2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvaGEiLCJuYmYiOjE2NTUzMTU4NDgsImV4cCI6MTY1NTMxNTg1OH0.ZCPlQTtBNdb1BYDkcxVMuXUDRcsAjkwfbcVNbut1Mfw'),
#  ('Content-Type', 'multipart/form-data; boundary=dart-http-boundary-y4GCjkweNb8P6Lk0AhfnL5RCyrPTAVLVGI1JN3uIDaJemJ9aHPi')
# ]
# ),
#  'remote_addr': '192.168.1.82',
#  'environ': {
# 'wsgi.version': (1, 0),
#  'wsgi.url_scheme': 'https',
#  'wsgi.input': <_io.BufferedReader name=4>,
#  'wsgi.errors': <_io.TextIOWrapper name='<stderr>' 
# mode='w' encoding='utf-8'>, 
# 'wsgi.multithread': True, 
# 'wsgi.multiprocess': False, 
# 'wsgi.run_once': False,
#  'werkzeug.socket': <ssl.SSLSocket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.82', 3345),
#  raddr=('192.168.1.82', 45020)>, 
# 'SERVER_SOFTWARE': 'Werkzeug/2.1.2',
#  'REQUEST_METHOD': 'POST',
#  'SCRIPT_NAME': '', 
# 'PATH_INFO': '/upload_file',
#  'QUERY_STRING': '',
#  'REQUEST_URI': '/upload_file', 
# 'RAW_URI': '/upload_file', 
# 'REMOTE_ADDR': '192.168.1.82', 
# 'REMOTE_PORT': 45020,
#  'SERVER_NAME': '192.168.1.82',
#  'SERVER_PORT': '3345', '
# SERVER_PROTOCOL': 'HTTP/1.1',
#  'HTTP_USER_AGENT': 'Dart/2.17 (dart:io)', 
# 'HTTP_ACCEPTHEADER': 'application/json', 
# 'HTTP_ACCEPT_ENCODING': 'gzip', 
# 'CONTENT_LENGTH': '105943',
#  'HTTP_HOST': '192.168.1.82:3345', 
# 'HTTP_AUTHORIZATION': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTMxNTg0OCwianRpIjoiM2U0OGVlNWQtOWI1YS00MmRiLWFiMzYtN2NmMjM5OWEzOTU2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRvaGEiLCJuYmYiOjE2NTUzMTU4NDgsImV4cCI6MTY1NTMxNTg1OH0.ZCPlQTtBNdb1BYDkcxVMuXUDRcsAjkwfbcVNbut1Mfw',
#  'CONTENT_TYPE': 'multipart/form-data; boundary=dart-http-boundary-y4GCjkweNb8P6Lk0AhfnL5RCyrPTAVLVGI1JN3uIDaJemJ9aHPi',
#  'werkzeug.request': <Request 'https://192.168.1.82:3345/upload_file' [POST]>},
#  'shallow': False, 
# 'url_rule': <Rule '/upload_file' (POST, OPTIONS) -> upload_file>, 
# 'view_args': {},
#  'host': '192.168.1.82:3345', 
# 'url': 'https://192.168.1.82:3345/upload_file'}