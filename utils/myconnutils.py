import sys
import pymysql
import pymysql.cursors;
import datetime;
import utils.my_loging as base_loger

def getConnection(): 
    connection = pymysql.connect(host='localhost',
                                # port=3306,
                                 user='db_company101',
                                 password='#4jQtv*#R2{8',                             
                                 database='company101_db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# user_pass SHA-256
def create_users():
    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        sql = """CREATE TABLE users(
                 user_id int  PRIMARY KEY AUTO_INCREMENT,
                 user_name VARCHAR(20) NOT NULL,
                 user_patronymic VARCHAR(20) NOT NULL,
                 user_surname VARCHAR(20) NOT NULL,
                 user_phone VARCHAR(20) NOT NULL,
                 user_date_birth DATE NOT NULL,
                 user_email VARCHAR(50) UNIQUE NOT NULL,
                 user_login VARCHAR(50) UNIQUE NOT NULL,
                 user_password TINYBLOB NOT NULL,
                 user_access_level int DEFAULT 1,
                 user_date_time_reg DATETIME DEFAULT CURRENT_TIMESTAMP
                );"""

        cursor.execute(sql)
    finally: 
        connection.close()

def create_category():
    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        sql = """CREATE TABLE category(
                 category_id int  PRIMARY KEY AUTO_INCREMENT,
                 category_name VARCHAR(20) NOT NULL
                );"""

        cursor.execute(sql)
    finally: 
        connection.close()


def create_product():
    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        sql = """CREATE TABLE products(
                 product_id int  PRIMARY KEY AUTO_INCREMENT,
                 product_name VARCHAR(20) NOT NULL,
                 product_price int NOT NULL,
                 product_category_id int NOT NULL,
                 product_date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
                 product_user_create_id VARCHAR(20) NOT NULL,
                 product_discription VARCHAR(50),
                 product_path_to_img VARCHAR(50) NOT NULL,
                 product_availability BOOLEAN,
                 FOREIGN KEY (product_category_id)  REFERENCES category (category_id),
                 FOREIGN KEY (product_category_id)  REFERENCES users (user_id)
                );"""
        cursor.execute(sql)
    finally: 
        connection.close()


def insert_user(user_surname, user_name, user_patronymic, user_phome,\
    user_date_birth, user_email, user_login, user_password):
    bool = 0
    user_access_level = 0
    connection = getConnection() 
    try :
        cursor = connection.cursor()   
        sql =  """Insert into users (user_name, user_patronymic, user_surname, user_phone,
            user_date_birth, user_email, user_login, user_password, user_access_level) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
        cursor.execute(sql, (user_name, user_patronymic, user_surname, user_phome,\
            user_date_birth, user_email, user_login, user_password, user_access_level) ) 
        connection.commit() 
        bool = 1
    except Exception as e:
        str_err = base_loger.msg_except(e)
        base_loger.set_log("app", str_err)
        e = sys.exc_info()[1]
        if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_email") > -1:
            bool = 2
        elif e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_login") > -1:
            bool = 3
        else:
            bool = 4
        print(e.args[1])
    finally: 
        connection.close()
        return bool


# определяет хэш пароля пользователя если он существует

def select_user_password(user_login):
    row = ''
    connection = getConnection() 
    try :
        cursor = connection.cursor()   
        sql =  """Select user_password from users Where user_login=%s """
        cursor.execute(sql, (user_login) ) 
        connection.commit() 
        # print('cursor')
        for row in cursor:
            row = row["user_password"]
    except Exception as e:
        str_err = base_loger.msg_except(e)
        base_loger.set_log("app", str_err)
        e = sys.exc_info()[1]
        print('e.args[1]', e.args[1])
        row = 'error'
    finally: 
        connection.close()
        # print('row', type(row), row)
        return row
















# def my_create():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = "CREATE TABLE test_1(id int  PRIMARY KEY AUTO_INCREMENT, name CHAR(20), age int);"

#         cursor.execute(sql)
#     finally: 
#         connection.close()

# #  Insert into test_1 (name, age)values ('anton', 39);
# #  Insert into test_1 (name, age)values ('rauan', 26);
# #  Insert into test_1 (name, age)values ('ruslan', 27);

# def my_insert():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         cursor = connection.cursor()  
#         sql =  "Insert into test_1 (name, age) " \
#             + " values (%s, %s) " 
#         cursor.execute(sql, ("grade", 2000) ) 
#         connection.commit()  
#     finally: 
#         connection.close()



# def my_query():

#     connection = getConnection() 
#     sql = "Select name, age from test_1 Where Id=%s " 
#     try :
#         cursor = connection.cursor() 
#         cursor.execute(sql, ( 1 ) )  
#         print ("cursor.description: ", cursor.description) 
#         print() 
#         for row in cursor:
#             print (" ----------- ")
#             print("Row: ", row)
#             print ("name: ", row["name"])
#             print ("age: ", row["age"])
#     finally:
#         connection.close()

# def my_querys() -> list[dict]:
#     data = [{"err": "err"}]
#     connection = getConnection() 
#     sql = "Select name, age from test_1" 
#     try :
#         cursor = connection.cursor() 
#         cursor.execute(sql)
#         data = cursor.fetchall()  
#     except Exception as e:
#         print(type(e))    # the exception type
#         print(e.args)     # arguments stored in .args
#         print(e)
#     finally:
#         connection.close()
#         return data

# def my_update():

#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = "Update test_1 set name = %s, age = %s where Id = %s "   
#         rowCount = cursor.execute(sql, ("850", 10, 1 ) ) 
#         connection.commit()  
#         print ("Updated! ", rowCount, " rows") 
#     finally:
#         connection.close()


# def my_delete():

#     connection = getConnection()  
#     try :
#         cursor = connection.cursor() 
#         sql = "Delete from test_1 where id = %s"  
#         rowCount = cursor.execute(sql, ( 1 ) ) 
#         connection.commit()  
#         print ("Deleted! ", rowCount, " rows") 
#     finally:
#         connection.close()







# # user_pass SHA-256
# def create_users():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = """CREATE TABLE users(
#                  user_id int  PRIMARY KEY AUTO_INCREMENT,
#                  user_name VARCHAR(20) NOT NULL,
#                  user_patronymic VARCHAR(20) NOT NULL,
#                  user_surname VARCHAR(20) NOT NULL,
#                  user_date_birth DATE NOT NULL,
#                  user_email VARCHAR(50) UNIQUE NOT NULL,
#                  user_login VARCHAR(50) UNIQUE NOT NULL,
#                  user_password TINYBLOB NOT NULL,
#                  user_date_time_reg DATETIME DEFAULT CURRENT_TIMESTAMP
#                 );"""

#         cursor.execute(sql)
#     finally: 
#         connection.close()

# # create_users()

# # добавляет пользователей при регистрации

# def insert_user(user_name, user_patronymic, user_surname,\
#     user_date_birth, user_email, user_login, user_password):
#     bool = 0
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Insert into users (user_name, user_patronymic, user_surname,
#             user_date_birth, user_email, user_login, user_password) 
#             values (%s, %s, %s, %s, %s, %s, %s) """
#         cursor.execute(sql, (user_name, user_patronymic, user_surname,\
#             user_date_birth, user_email, user_login, user_password) ) 
#         connection.commit() 
#         bool = 1
#     except:
#         e = sys.exc_info()[1]
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_email") > -1:
#             bool = 2
#             print(e.args[1])
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_login") > -1:
#             bool = 3
#             print(e.args[1])
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return bool


# # определяет хэш пароля пользователя если он существует

# def select_user_password(user_login):
#     row = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select user_password from users Where user_login=%s """
#         cursor.execute(sql, (user_login) ) 
#         connection.commit() 
#         print('cursor')
#         for row in cursor:
#             row = row["user_password"]
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print('row')
#         print(row)
#         return row
   


# import mysql.connector
# from mysql.connector import Error
# from mysql.connector.connection import MySQLConnection
# from mysql.connector import pooling as pooling
# import sys

# # список содержащий слова которые запрещенно вводить пользователю
# bans = ['create', 'select', 'drop', 'delete', 'update', 'insert', 'truncate', 'grant', 'revoke',
#         '\'', '\"', '\`', '%s']

# # функция для проверки запретных строк


# def ban_str(checked_list):
#     bool_ban = False
#     for ban in bans:
#         for checked_str in checked_list:
#             if ban in checked_str.lower():
#                 bool_ban = True
#     return bool_ban


# # получение пула соединения с базой данных
# c_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
#                                      pool_size=1,
#                                      pool_reset_session=True,
#                                      host='localhost',
#                                      database='my_app_db',
#                                      user='root',
#                                      password='TESTO')

# # фуекция создает начальную таблицу для записи при регистрации
# def create_Users():
#     try:
#         c_obj = c_pool.get_connection()
#         if c_obj.is_connected():
#             cursor = c_obj.cursor()
#             cursor.execute("CREATE TABLE `Users` " +
#                            "(`id` int AUTO_INCREMENT," +
#                            "`name` varchar(30) NOT NULL," +
#                            "`surname` varchar(30) NOT NULL," +
#                            "`buyer_seller` varchar(20) NOT NULL," +
#                            "`date_birth` datetime NOT NULL," +
#                            "`email` varchar(30) NOT NULL UNIQUE," +
#                            "`login` varchar(30) NOT NULL UNIQUE," +
#                            "`passw` tinyblob NOT NULL," +
#                            "`date` datetime DEFAULT CURRENT_TIMESTAMP," +
#                            "PRIMARY KEY(`id`));")
#     except Exception:
#         e = sys.exc_info()[1]
#         print(e.args[0])
#     finally:
#         if(c_obj.is_connected()):
#             cursor.close()
#             c_obj.close()


# # фуекция создает таблицу для товаров
# def create_product():
#     ans_result_set = []
#     if ban_str(ans_result_set):
#         print('вы ввели запретные слова')
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 cursor.execute("CREATE TABLE `products`" +
#                                "(`id` int AUTO_INCREMENT," +
#                                "`login_seller` varchar(50) NOT NULL," +
#                                "`name_product` varchar(50) NOT NULL," +
#                                "`category_product` varchar(50) NOT NULL," +
#                                "`description_product` varchar(1000) NOT NULL," +
#                                "`price_product` int NOT NULL," +
#                                "`date` datetime DEFAULT CURRENT_TIMESTAMP," +
#                                "PRIMARY KEY(`id`));")
#         except Exception:
#             e = sys.exc_info()[1]
#             print(e.args[0])
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()

# # create_Users()
# # create_product()

# # функция возвращающая из переданной в нее названия таблицы
# # все данные , строки в словарь , а словари в список
# def result_set(name_tab):
#     results = []
#     ans_result_set = [name_tab]
#     if ban_str(ans_result_set):
#         print('вы ввели запретные слова')
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 cursor.execute("select * from "+name_tab + ";")
#                 columns = [column[0] for column in cursor.description]
#                 for row in cursor.fetchall():
#                     results.append(dict(zip(columns, row)))
#         except Error as e:
#             print(e)
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return results

# # функция возвращающая из переданной в нее названия таблицы
# # все данные при условии, строки в словарь , а словар в список
# def result_set_where(name_tab, where):
#     results = []
#     ans_result_set = [name_tab]
#     if ban_str(ans_result_set):
#         print('вы ввели запретные слова')
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 cursor.execute("select * from "+name_tab + " WHERE "+where + ";")
#                 columns = [column[0] for column in cursor.description]
#                 for row in cursor.fetchall():
#                     results.append(dict(zip(columns, row)))
#         except Error as e:
#             print(e)
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return results


# # функция возвращающает True  если такой пользователь с таким паролем существует
# def user_aut(user_login, user_pass):
#     bool = False
#     ans_user_aut = [user_login]
#     if ban_str(ans_user_aut):
#         print('вы ввели запретные слова')
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 cursor.execute(
#                     "select passw from Users WHERE login = '" + user_login + "' ;")
#                 rows = cursor.fetchall()
#                 if str(rows[0][0][26:]) == user_pass:
#                     bool = True
#                 else:
#                     bool = False
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool


# # функция возвращающает True если этот продавец добавлял этот товар
# def seller_product(user_login, num_product):
#     bool = False
#     ans_seller_product = [user_login, num_product]
#     if ban_str(ans_seller_product):
#         print('вы ввели запретные слова')
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 cursor.execute(
#                     "select id from products WHERE id = " + num_product + " AND login_seller = '" + user_login + "';")
#                 id = cursor.fetchall()
#                 if id:
#                     if id[0][0] == int(num_product):
#                         bool = True
#                     else:
#                         bool = False
#                 else:
#                     bool = False
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool

# # функция возвращающая False  если пользователь не зарегистрироваллся
# def insert_Users(name, surname, buyer_seller, date_birth, email, login, passw):
#     bool = False
#     ans_insert_users = [name, surname, buyer_seller, date_birth, email, login]
#     if ban_str(ans_insert_users):
#         print('вы ввели запретные слова')
#         bool = False
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 sql_insert_query = """INSERT INTO Users (name, surname, buyer_seller, date_birth,
#                                     email, login, passw) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#                 insert_tuple = (name, surname, buyer_seller,
#                                 date_birth, email, login, passw)
#                 cursor.execute(sql_insert_query, insert_tuple)
#                 # c_obj.commit()
#                 cursor.execute("CREATE TABLE `user_" + login + "`" +
#                                "(`id` int AUTO_INCREMENT," +
#                                "`name_product` varchar(50) NOT NULL," +  # имя продукта
#                                "`category_product` varchar(50) NOT NULL," +
#                                "`num_product` int NOT NULL," +  # номер продукта в таблице товаров
#                                "`price` int NOT NULL," +  # цена на момент операции
#                                "`act` varchar(30) NOT NULL," +  # название операции
#                                "`act_opponent` varchar(50) DEFAULT NULL," +  # имя оппонента если есть
#                                "`date` datetime DEFAULT CURRENT_TIMESTAMP," +  # время операции
#                                "PRIMARY KEY(`id`));")
#                 c_obj.commit()
#                 bool = True
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool


# # функция возвращающая False  если продукт не добавился
# def insert_product(login_seller, name_product, category_product, description_product, price_product):
#     bool = False
#     ans_insert_product = [login_seller, name_product,
#                           category_product, description_product, price_product]
#     if ban_str(ans_insert_product):
#         print('вы ввели запретные слова')
#         bool = False
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 sql_insert_query = """INSERT INTO products (login_seller, name_product, category_product,
#                                       description_product, price_product) 
#                                       VALUES (%s,%s,%s,%s,%s)"""
#                 insert_tuple = (login_seller, name_product,
#                                 category_product, description_product, price_product)
#                 cursor.execute(sql_insert_query, insert_tuple)
#                 cursor.execute("select id from products WHERE login_seller = '" + login_seller +
#                                "' AND name_product = '" + name_product + "' AND category_product = '" + category_product +
#                                "' AND description_product = '" + description_product + "' AND price_product = " + price_product + ";")
#                 num_product = cursor.fetchall()[0][0]
#                 sql_insert_query_2 = "INSERT INTO user_" + login_seller + \
#                                      "(name_product, category_product, num_product, price, act, act_opponent)" \
#                                      "VALUES (%s,%s,%s,%s,%s,%s)"
#                 insert_tuple_2 = (name_product,category_product, num_product, price_product, 'add_product', login_seller)
#                 cursor.execute(sql_insert_query_2, insert_tuple_2)
#                 c_obj.commit()
#                 bool = True
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool

# # функция возвращающая True если данные в таблице замененны
# def update_Users(tab_name, upd_colum_name, new_value, condition, condition_value):
#     bool = False
#     ans_update_users = [tab_name, upd_colum_name,
#                         new_value, condition, condition_value]
#     if ban_str(ans_update_users):
#         print('вы ввели запретные слова')
#         bool = False
#     else:
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 sql_update_query = "UPDATE " + tab_name + " SET " + \
#                                    upd_colum_name + " = %s WHERE " + condition + " = %s "
#                 update_tuple = (new_value, condition_value)
#                 cursor.execute(sql_update_query, update_tuple)
#                 c_obj.commit()
#                 bool = True
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool

# # функция возвращающая False  если продукт не изменен
# def update_product(num_product, login_seller, name_product, category_product, description_product, price_product):
#     bool = False
#     ans_insert_product = [num_product, login_seller, name_product,
#                           category_product, description_product, price_product]
#     if ban_str(ans_insert_product):
#         print('вы ввели запретные слова')
#         bool = False
#     else:
#         print(login_seller)
#         try:
#             c_obj = c_pool.get_connection()
#             if c_obj.is_connected():
#                 cursor = c_obj.cursor()
#                 sql_insert_query = """UPDATE products SET description_product = %s , price_product = %s 
#                                       WHERE ID = %s """
#                 insert_tuple = (description_product, price_product, int(num_product))
#                 cursor.execute(sql_insert_query, insert_tuple)

#                 sql_insert_query_2 = "INSERT INTO user_" + login_seller + \
#                                      "(name_product, category_product, num_product, price, act, act_opponent)" \
#                                      "VALUES (%s,%s,%s,%s,%s,%s)"
#                 insert_tuple_2 = (name_product,category_product, num_product, price_product, 'update_product', login_seller)
#                 cursor.execute(sql_insert_query_2, insert_tuple_2)
#                 c_obj.commit()
#                 bool = True
#         except Error as e:
#             print(e)
#             bool = False
#         finally:
#             if(c_obj.is_connected()):
#                 cursor.close()
#                 c_obj.close()
#     return bool





# import sys
# import pymysql
# import pymysql.cursors;
# import datetime;

# def getConnection(): 
#     connection = pymysql.connect(host='localhost',
#                                 # port=3306,
#                                  user='user_flatter_flask_1',
#                                  password='Pass_db_flatter_flask1#',                             
#                                  database='db_flatter_flask_1',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor)
#     return connection



# ###############################################################################
                        
# #                                    users                                    #

# ###############################################################################

# # user_pass SHA-256
# def create_users():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = """CREATE TABLE users(
#                  user_id int  PRIMARY KEY AUTO_INCREMENT,
#                  user_name VARCHAR(20) NOT NULL,
#                  user_patronymic VARCHAR(20) NOT NULL,
#                  user_surname VARCHAR(20) NOT NULL,
#                  user_phone VARCHAR(20) NOT NULL,
#                  user_date_birth DATE NOT NULL,
#                  user_email VARCHAR(50) UNIQUE NOT NULL,
#                  user_login VARCHAR(50) UNIQUE NOT NULL,
#                  user_password TINYBLOB NOT NULL,
#                  user_date_time_reg DATETIME DEFAULT CURRENT_TIMESTAMP
#                 );"""

#         cursor.execute(sql)
#     finally: 
#         connection.close()


# #################################  insert  #################################


# # добавляет пользователей при регистрации

# def insert_user(user_name, user_patronymic, user_surname, user_phone,\
#     user_date_birth, user_email, user_login, user_password):
#     bool = 0
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Insert into users (user_name, user_patronymic, user_surname,
#             user_phone, user_date_birth, user_email, user_login, user_password) 
#             values (%s, %s, %s, %s, %s, %s, %s, %s) """
#         cursor.execute(sql, (user_name, user_patronymic, user_surname, user_phone,\
#             user_date_birth, user_email, user_login, user_password) ) 
#         connection.commit() 
#         bool = 1
#     except:
#         e = sys.exc_info()[1]
#         # проверяем ошибку на 'такая почта уже используется'
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_email") > -1:
#             bool = 2
#         # проверяем ошибку на 'такой логин уже используется'
#         elif e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_login") > -1:
#             bool = 3
#         # неизвестная ошибка базы данных
#         else:
#             bool = 4
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print(type(bool))
#         return bool

# #################################  select  #################################

# # определяет хэш пароля пользователя если он существует

# def select_user_password(user_login):
#     row = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select user_password from users Where user_login=%s """
#         cursor.execute(sql, (user_login) ) 
#         connection.commit() 
#         for row in cursor:
#             row = row["user_password"]
#     except:
#         e = sys.exc_info()[1]
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return row
   

# def select_user_id(user_login):
#     row = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select user_id from users Where user_login=%s """
#         cursor.execute(sql, (user_login) ) 
#         connection.commit() 
#         print('cursor')
#         for row in cursor:
#             row = row["user_id"]
#     except:
#         e = sys.exc_info()[1]
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return row

# ###############################################################################
                        
# #                                 categories                                  #

# ###############################################################################



# def create_categories():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = """CREATE TABLE categories(
#                  category_id int  PRIMARY KEY AUTO_INCREMENT,
#                  category_name VARCHAR(20) UNIQUE NOT NULL,
#                  category_discription VARCHAR(500) NOT NULL,
#                  category_owner int  NOT NULL,
#                  category_date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
#                  FOREIGN KEY (category_owner)  REFERENCES users(user_id)
#                 );"""

#         cursor.execute(sql)
#     finally: 
#         connection.close()


# #################################  insert  #################################

# def insert_category(category_name, category_discription, category_owner):
#     bool = 0
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Insert into categories (category_name, category_discription, category_owner) 
#             values (%s, %s, %s) """
#         cursor.execute(sql, (category_name, category_discription, category_owner) ) 
#         connection.commit() 
#         bool = 1
#     except:
#         e = sys.exc_info()[1]
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("categories.category_name") > -1:
#             bool = 2
#             print(e.args[1])
#         # Cannot add or update a child row: a foreign key constraint fails (`db_flatter_flask_1`.`categories`, CONSTRAINT `categories_ibfk_1` FOREIGN KEY (`category_owner`) REFERENCES `users` (`user_id`))
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_login") > -1:
#             bool = 3
#             print(e.args[1])
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print('bool_cat', bool)
#         return bool

# #################################  select  #################################


# def select_categories():
#     res = []
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select category_name from categories"""
#         cursor.execute(sql) 
#         connection.commit() 
#         rows = cursor.fetchall()
#         for row in rows:
#             res.append(row['category_name'])
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print('res')
#         print(res)
#         return res

# def select_categories_count():
#     res = []
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select category_name , count(ads.ad_categories)  as count_ads from categories INNER JOIN ads ON (categories.category_id=ads.ad_categories) group by categories.category_name;"""
#         cursor.execute(sql) 
#         connection.commit() 
#         rows = cursor.fetchall()
#         print(rows)
#         for row in rows:
#             res.append([row['category_name'], row['count_ads']])
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print('res')
#         print(res)
#         return res

# def select_category_id(category_name):
#     row = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select category_id from categories Where category_name=%s """
#         cursor.execute(sql, (category_name) ) 
#         connection.commit() 
#         print('cursor')
#         for row in cursor:
#             row = row["category_id"]
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         print('row')
#         print(row)
#         return row

# ###############################################################################
                        
# #                                     ads                                    #

# ###############################################################################



# def create_ads():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = """CREATE TABLE ads(
#                  ad_id int  PRIMARY KEY AUTO_INCREMENT,
#                  ad_name VARCHAR(20) NOT NULL,
#                  ad_categories int  NOT NULL,
#                  ad_price int NOT NULL,
#                  ad_phones JSON,
#                  ad_mails JSON,
#                  ad_discription VARCHAR(500) NOT NULL,
#                  ad_photes VARCHAR(20) NOT NULL,
#                  ad_owner int  NOT NULL,
#                  ad_date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
#                  UNIQUE(ad_name, ad_categories, ad_owner),
#                  FOREIGN KEY (ad_categories)  REFERENCES categories(category_id),
#                  FOREIGN KEY (ad_owner)  REFERENCES users(user_id)
#                 );"""

#         cursor.execute(sql)
#     finally: 
#         connection.close()

# #################################  insert  #################################

# def insert_ad(ad_name, ad_categories, ad_price, ad_phones, ad_mails, ad_discription, ad_photes, ad_owner):
#     bool = 0
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Insert into ads (ad_name, ad_categories, ad_price, ad_phones, ad_mails, ad_discription, ad_photes, ad_owner) 
#             values (%s, %s, %s, %s, %s, %s, %s, %s) """
#         cursor.execute(sql, (ad_name, ad_categories, ad_price, ad_phones, ad_mails, ad_discription, ad_photes, ad_owner) ) 
#         connection.commit() 
#         bool = 1
#     except:
#         e = sys.exc_info()[1]
#         # проверяет есть ли у пользователя в данной категории обьявление с таким же названием
#         if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("ads.ad_name") > -1:
#             bool = 2
#             print(e.args[1])
#         else:
#             bool = 3
#             print(e.args[1])
#     finally: 
#         connection.close()
#         return bool

# #################################  select  #################################


# def select_category_ads(ad_category_id):
#     res = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =  """Select * from ads Where ad_categories=%s """
#         cursor.execute(sql, (ad_category_id) ) 
#         connection.commit() 
#         res = cursor.fetchall();
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return res


# def select_category_ads2(ad_category_id):
#     res = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =   """SELECT ads.*, users.user_name as user_name, users.user_surname as user_surname, categories.category_name as category_name
#                     FROM ads INNER JOIN users ON (ads.ad_owner=users.user_id) INNER JOIN categories ON (ads.ad_categories=categories.category_id)
#                     WHERE ads.ad_categories=%s;"""
#         cursor.execute(sql, (ad_category_id) ) 
#         connection.commit() 
#         res = cursor.fetchall();
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return res


# def select_user_ads(ad_owner_id):
#     res = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =   """SELECT ads.*, users.user_name as user_name, users.user_surname as user_surname, categories.category_name as category_name
#                     FROM ads INNER JOIN users ON (ads.ad_owner=users.user_id) INNER JOIN categories ON (ads.ad_categories=categories.category_id)
#                     WHERE ads.ad_owner=%s;"""
#         cursor.execute(sql, (ad_owner_id) ) 
#         connection.commit() 
#         res = cursor.fetchall();
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return res

# def select_user_id_owner(ad_owner_id):
#     res = ''
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql =   """SELECT ads.*, users.user_name as user_name
#                     FROM ads INNER JOIN users ON (ads.ad_owner=users.user_id) INNER JOIN categories ON (ads.ad_categories=categories.category_id)
#                     WHERE ads.ad_owner=%s;"""
#         cursor.execute(sql, (ad_owner_id) ) 
#         connection.commit() 
#         res = cursor.fetchall();
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#     finally: 
#         connection.close()
#         return res

# #################################  update  #################################


# def update_ad(ad_name, ad_price, ad_discription, ad_phones, ad_mails, ad_id, ad_owner):
#     res = '0'
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor()   
#         sql = "Update ads set ad_name = %s, ad_price = %s, ad_discription = %s, ad_phones = %s, ad_mails = %s where ad_id = %s AND ad_owner = %s "   
#         rowCount = cursor.execute(sql, (ad_name, ad_price, ad_discription, ad_phones, ad_mails, ad_id, ad_owner) ) 
#         connection.commit()  
#         res = '1'
#     except:
#         e = sys.exc_info()[1]
#         print('e.args[1]')
#         print(e.args[1])
#         res = '0'
#     finally: 
#         connection.close()
#         print('res', res)
#         return res




# create_users()
# create_categories()
# create_ads()





# def my_create():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = "CREATE TABLE test_1(id int  PRIMARY KEY AUTO_INCREMENT, name CHAR(20), age int);"

#         cursor.execute(sql)
#     finally: 
#         connection.close()


# def my_insert():
#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         cursor = connection.cursor()  
#         sql =  "Insert into test_1 (name, age) " \
#             + " values (%s, %s) " 
#         cursor.execute(sql, ("grade", 2000) ) 
#         connection.commit()  
#     finally: 
#         connection.close()



# def my_query():

#     connection = getConnection() 
#     sql = "Select name, age from test_1 Where Id=%s " 
#     try :
#         cursor = connection.cursor() 
#         cursor.execute(sql, ( 1 ) )  
#         print ("cursor.description: ", cursor.description) 
#         print() 
#         for row in cursor:
#             print (" ----------- ")
#             print("Row: ", row)
#             print ("name: ", row["name"])
#             print ("age: ", row["age"])
#     finally:
#         connection.close()


# def my_update():

#     connection = getConnection() 
#     try :
#         cursor = connection.cursor() 
#         sql = "Update test_1 set name = %s, age = %s where Id = %s "   
#         rowCount = cursor.execute(sql, ("850", 10, 1 ) ) 
#         connection.commit()  
#         print ("Updated! ", rowCount, " rows") 
#     finally:
#         connection.close()


# def my_delete():

#     connection = getConnection()  
#     try :
#         cursor = connection.cursor() 
#         sql = "Delete from test_1 where id = %s"  
#         rowCount = cursor.execute(sql, ( 1 ) ) 
#         connection.commit()  
#         print ("Deleted! ", rowCount, " rows") 
#     finally:
#         connection.close()
