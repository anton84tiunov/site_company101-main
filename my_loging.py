import logging
import logging.handlers

# filemode='w'

def set_log(name, msg):
    """функция для инициализации loger для ведения лог файлов"""
    logger = logging.getLogger(name)
    # FORMAT = 'asctime: %(asctime)s, name: %(name)s, levelname: %(levelname)s, message: %(message)s\n ------------------------------\n'
    FORMAT = ' %(asctime)s, %(name)s, %(levelname)s, %(message)s\n ------------------------------\n'
    
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    # fn = logging.handlers.RotatingFileHandler(filename='app_logs/pdf_editor.log')
    fn = logging.FileHandler(filename='my_logs/all.log')
    fn.setFormatter(logging.Formatter(FORMAT))
    fn.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fn)
    logger.debug(msg)