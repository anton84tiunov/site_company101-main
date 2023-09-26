import sys
import pymysql
import pymysql.cursors;
import datetime;

def getConnection(): 
    connection = pymysql.connect(host='localhost',
                                # port=3306,
                                 user='db_company101',
                                 password='#4jQtv*#R2{8',                             
                                 database='company101_db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection



def my_create():
    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        sql = "CREATE TABLE test_1(id int  PRIMARY KEY AUTO_INCREMENT, name CHAR(20), age int);"

        cursor.execute(sql)
    finally: 
        connection.close()

#  Insert into test_1 (name, age)values ('anton', 39);
#  Insert into test_1 (name, age)values ('rauan', 26);
#  Insert into test_1 (name, age)values ('ruslan', 27);

def my_insert():
    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        cursor = connection.cursor()  
        sql =  "Insert into test_1 (name, age) " \
            + " values (%s, %s) " 
        cursor.execute(sql, ("grade", 2000) ) 
        connection.commit()  
    finally: 
        connection.close()



def my_query():

    connection = getConnection() 
    sql = "Select name, age from test_1 Where Id=%s " 
    try :
        cursor = connection.cursor() 
        cursor.execute(sql, ( 1 ) )  
        print ("cursor.description: ", cursor.description) 
        print() 
        for row in cursor:
            print (" ----------- ")
            print("Row: ", row)
            print ("name: ", row["name"])
            print ("age: ", row["age"])
    finally:
        connection.close()

def my_querys() -> list[dict]:
    data = [{"err": "err"}]
    connection = getConnection() 
    sql = "Select name, age from test_1" 
    try :
        cursor = connection.cursor() 
        cursor.execute(sql)
        data = cursor.fetchall()  
    except Exception as e:
        print(type(e))    # the exception type
        print(e.args)     # arguments stored in .args
        print(e)
    finally:
        connection.close()
        return data

def my_update():

    connection = getConnection() 
    try :
        cursor = connection.cursor() 
        sql = "Update test_1 set name = %s, age = %s where Id = %s "   
        rowCount = cursor.execute(sql, ("850", 10, 1 ) ) 
        connection.commit()  
        print ("Updated! ", rowCount, " rows") 
    finally:
        connection.close()


def my_delete():

    connection = getConnection()  
    try :
        cursor = connection.cursor() 
        sql = "Delete from test_1 where id = %s"  
        rowCount = cursor.execute(sql, ( 1 ) ) 
        connection.commit()  
        print ("Deleted! ", rowCount, " rows") 
    finally:
        connection.close()



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
                 user_date_birth DATE NOT NULL,
                 user_email VARCHAR(50) UNIQUE NOT NULL,
                 user_login VARCHAR(50) UNIQUE NOT NULL,
                 user_password TINYBLOB NOT NULL,
                 user_date_time_reg DATETIME DEFAULT CURRENT_TIMESTAMP
                );"""

        cursor.execute(sql)
    finally: 
        connection.close()

# create_users()

# добавляет пользователей при регистрации

def insert_user(user_name, user_patronymic, user_surname,\
    user_date_birth, user_email, user_login, user_password):
    bool = 0
    connection = getConnection() 
    try :
        cursor = connection.cursor()   
        sql =  """Insert into users (user_name, user_patronymic, user_surname,
            user_date_birth, user_email, user_login, user_password) 
            values (%s, %s, %s, %s, %s, %s, %s) """
        cursor.execute(sql, (user_name, user_patronymic, user_surname,\
            user_date_birth, user_email, user_login, user_password) ) 
        connection.commit() 
        bool = 1
    except:
        e = sys.exc_info()[1]
        if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_email") > -1:
            bool = 2
            print(e.args[1])
        if e.args[1].find("Duplicate entry") > -1 and e.args[1].find("users.user_login") > -1:
            bool = 3
            print(e.args[1])
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
        print('cursor')
        for row in cursor:
            row = row["user_password"]
    except:
        e = sys.exc_info()[1]
        print('e.args[1]')
        print(e.args[1])
    finally: 
        connection.close()
        print('row')
        print(row)
        return row
   


