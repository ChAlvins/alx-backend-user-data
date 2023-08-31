#!/usr/bin/env python3
"""filter_datum module"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Returns filtered values from log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_db() -> mysql.connector.connection.MYSQLConnection:
    """Connection to MySQL environment """
    user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password=os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database=os.getenv('PERSONAL_DATA_DB_NAME')
    db_connect = mysql.connector.connect(user=user,
                                         password=password,
                                         host=host,
                                         database=db_name)
    return db_connect


def get_logger() -> logging.Logger:
    """function that returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    target_handler = logging.StreamHandler()
    target_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(PII_FIELDS)
    target_handler.setFormatter(formatter)

    logger.addHandler(target_handler)
    return logger


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
