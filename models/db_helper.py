import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling as pooling
import sys

# список содержащий слова которые запрещенно вводить пользователю
bans = ['create', 'select', 'drop', 'delete', 'update', 'insert', 'truncate', 'grant', 'revoke',
        '\'', '\"', '\`', '%s']

# функция для проверки запретных строк


def ban_str(checked_list):
    bool_ban = False
    for ban in bans:
        for checked_str in checked_list:
            if ban in checked_str.lower():
                bool_ban = True
    return bool_ban


# получение пула соединения с базой данных
c_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                     pool_size=1,
                                     pool_reset_session=True,
                                     host='localhost',
                                     database='my_app_db',
                                     user='root',
                                     password='TESTO')

# фуекция создает начальную таблицу для записи при регистрации
def create_Users():
    try:
        c_obj = c_pool.get_connection()
        if c_obj.is_connected():
            cursor = c_obj.cursor()
            cursor.execute("CREATE TABLE `Users` " +
                           "(`id` int AUTO_INCREMENT," +
                           "`name` varchar(30) NOT NULL," +
                           "`surname` varchar(30) NOT NULL," +
                           "`buyer_seller` varchar(20) NOT NULL," +
                           "`date_birth` datetime NOT NULL," +
                           "`email` varchar(30) NOT NULL UNIQUE," +
                           "`login` varchar(30) NOT NULL UNIQUE," +
                           "`passw` tinyblob NOT NULL," +
                           "`date` datetime DEFAULT CURRENT_TIMESTAMP," +
                           "PRIMARY KEY(`id`));")
    except Exception:
        e = sys.exc_info()[1]
        print(e.args[0])
    finally:
        if(c_obj.is_connected()):
            cursor.close()
            c_obj.close()


# фуекция создает таблицу для товаров
def create_product():
    ans_result_set = []
    if ban_str(ans_result_set):
        print('вы ввели запретные слова')
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                cursor.execute("CREATE TABLE `products`" +
                               "(`id` int AUTO_INCREMENT," +
                               "`login_seller` varchar(50) NOT NULL," +
                               "`name_product` varchar(50) NOT NULL," +
                               "`category_product` varchar(50) NOT NULL," +
                               "`description_product` varchar(1000) NOT NULL," +
                               "`price_product` int NOT NULL," +
                               "`date` datetime DEFAULT CURRENT_TIMESTAMP," +
                               "PRIMARY KEY(`id`));")
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()

# create_Users()
# create_product()

# функция возвращающая из переданной в нее названия таблицы
# все данные , строки в словарь , а словари в список
def result_set(name_tab):
    results = []
    ans_result_set = [name_tab]
    if ban_str(ans_result_set):
        print('вы ввели запретные слова')
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                cursor.execute("select * from "+name_tab + ";")
                columns = [column[0] for column in cursor.description]
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
        except Error as e:
            print(e)
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return results

# функция возвращающая из переданной в нее названия таблицы
# все данные при условии, строки в словарь , а словар в список
def result_set_where(name_tab, where):
    results = []
    ans_result_set = [name_tab]
    if ban_str(ans_result_set):
        print('вы ввели запретные слова')
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                cursor.execute("select * from "+name_tab + " WHERE "+where + ";")
                columns = [column[0] for column in cursor.description]
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
        except Error as e:
            print(e)
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return results


# функция возвращающает True  если такой пользователь с таким паролем существует
def user_aut(user_login, user_pass):
    bool = False
    ans_user_aut = [user_login]
    if ban_str(ans_user_aut):
        print('вы ввели запретные слова')
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                cursor.execute(
                    "select passw from Users WHERE login = '" + user_login + "' ;")
                rows = cursor.fetchall()
                if str(rows[0][0][26:]) == user_pass:
                    bool = True
                else:
                    bool = False
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool


# функция возвращающает True если этот продавец добавлял этот товар
def seller_product(user_login, num_product):
    bool = False
    ans_seller_product = [user_login, num_product]
    if ban_str(ans_seller_product):
        print('вы ввели запретные слова')
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                cursor.execute(
                    "select id from products WHERE id = " + num_product + " AND login_seller = '" + user_login + "';")
                id = cursor.fetchall()
                if id:
                    if id[0][0] == int(num_product):
                        bool = True
                    else:
                        bool = False
                else:
                    bool = False
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool

# функция возвращающая False  если пользователь не зарегистрироваллся
def insert_Users(name, surname, buyer_seller, date_birth, email, login, passw):
    bool = False
    ans_insert_users = [name, surname, buyer_seller, date_birth, email, login]
    if ban_str(ans_insert_users):
        print('вы ввели запретные слова')
        bool = False
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                sql_insert_query = """INSERT INTO Users (name, surname, buyer_seller, date_birth,
                                    email, login, passw) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                insert_tuple = (name, surname, buyer_seller,
                                date_birth, email, login, passw)
                cursor.execute(sql_insert_query, insert_tuple)
                # c_obj.commit()
                cursor.execute("CREATE TABLE `user_" + login + "`" +
                               "(`id` int AUTO_INCREMENT," +
                               "`name_product` varchar(50) NOT NULL," +  # имя продукта
                               "`category_product` varchar(50) NOT NULL," +
                               "`num_product` int NOT NULL," +  # номер продукта в таблице товаров
                               "`price` int NOT NULL," +  # цена на момент операции
                               "`act` varchar(30) NOT NULL," +  # название операции
                               "`act_opponent` varchar(50) DEFAULT NULL," +  # имя оппонента если есть
                               "`date` datetime DEFAULT CURRENT_TIMESTAMP," +  # время операции
                               "PRIMARY KEY(`id`));")
                c_obj.commit()
                bool = True
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool


# функция возвращающая False  если продукт не добавился
def insert_product(login_seller, name_product, category_product, description_product, price_product):
    bool = False
    ans_insert_product = [login_seller, name_product,
                          category_product, description_product, price_product]
    if ban_str(ans_insert_product):
        print('вы ввели запретные слова')
        bool = False
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                sql_insert_query = """INSERT INTO products (login_seller, name_product, category_product,
                                      description_product, price_product) 
                                      VALUES (%s,%s,%s,%s,%s)"""
                insert_tuple = (login_seller, name_product,
                                category_product, description_product, price_product)
                cursor.execute(sql_insert_query, insert_tuple)
                cursor.execute("select id from products WHERE login_seller = '" + login_seller +
                               "' AND name_product = '" + name_product + "' AND category_product = '" + category_product +
                               "' AND description_product = '" + description_product + "' AND price_product = " + price_product + ";")
                num_product = cursor.fetchall()[0][0]
                sql_insert_query_2 = "INSERT INTO user_" + login_seller + \
                                     "(name_product, category_product, num_product, price, act, act_opponent)" \
                                     "VALUES (%s,%s,%s,%s,%s,%s)"
                insert_tuple_2 = (name_product,category_product, num_product, price_product, 'add_product', login_seller)
                cursor.execute(sql_insert_query_2, insert_tuple_2)
                c_obj.commit()
                bool = True
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool

# функция возвращающая True если данные в таблице замененны
def update_Users(tab_name, upd_colum_name, new_value, condition, condition_value):
    bool = False
    ans_update_users = [tab_name, upd_colum_name,
                        new_value, condition, condition_value]
    if ban_str(ans_update_users):
        print('вы ввели запретные слова')
        bool = False
    else:
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                sql_update_query = "UPDATE " + tab_name + " SET " + \
                                   upd_colum_name + " = %s WHERE " + condition + " = %s "
                update_tuple = (new_value, condition_value)
                cursor.execute(sql_update_query, update_tuple)
                c_obj.commit()
                bool = True
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool

# функция возвращающая False  если продукт не изменен
def update_product(num_product, login_seller, name_product, category_product, description_product, price_product):
    bool = False
    ans_insert_product = [num_product, login_seller, name_product,
                          category_product, description_product, price_product]
    if ban_str(ans_insert_product):
        print('вы ввели запретные слова')
        bool = False
    else:
        print(login_seller)
        try:
            c_obj = c_pool.get_connection()
            if c_obj.is_connected():
                cursor = c_obj.cursor()
                sql_insert_query = """UPDATE products SET description_product = %s , price_product = %s 
                                      WHERE ID = %s """
                insert_tuple = (description_product, price_product, int(num_product))
                cursor.execute(sql_insert_query, insert_tuple)

                sql_insert_query_2 = "INSERT INTO user_" + login_seller + \
                                     "(name_product, category_product, num_product, price, act, act_opponent)" \
                                     "VALUES (%s,%s,%s,%s,%s,%s)"
                insert_tuple_2 = (name_product,category_product, num_product, price_product, 'update_product', login_seller)
                cursor.execute(sql_insert_query_2, insert_tuple_2)
                c_obj.commit()
                bool = True
        except Error as e:
            print(e)
            bool = False
        finally:
            if(c_obj.is_connected()):
                cursor.close()
                c_obj.close()
    return bool
