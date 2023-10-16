from datetime import datetime
from datetime import timedelta
from datetime import timezone

# server_host = "192.168.1.104"
# server_host = "192.168.58.138"
# server_host = "172.16.0.106"
server_host = "localhost"

server_port = 3344

class FlaskConfig(object):
    DEBUG = True

class JWTConfig(object):
    JWT_TOKEN_LOCATION=["headers", "json"]
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(hours=1)
    # JWT_ALGORITHM='HS256'
    JWT_SECRET_KEY='secret_key'

