import logging
import logging.handlers
import traceback as tr

# filemode='w'

def msg_except( exc ) -> str:

    error = tr.TracebackException(exc_type =type(exc),exc_traceback = exc.__traceback__ , exc_value =exc).stack[-1]
    str_err = 'сообщение: << {} >> . файл: {}  . строка: {} .  где: {}'.format(exc,
                error.filename,
                error.lineno,
                error.line
                )
    return str_err





def set_log(name, msg):
    """функция для инициализации loger для ведения лог файлов"""
    logger = logging.getLogger(name)
    FORMAT = ' %(asctime)s, %(name)s, %(levelname)s, %(message)s .\n '
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    fn = logging.FileHandler(filename='my_logs/all.log')
    fn.setFormatter(logging.Formatter(FORMAT))
    fn.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fn)
    logger.debug(msg)