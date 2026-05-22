#!/usr/bin/env python3
"""
define a function called filter_datum
function get_logger
"""

import logging
import re
from typing import List, Tuple
import os
import mysql.connector
from mysql.connector import connection


PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')


def get_db() -> connection.MySQLConnection:
    """
    Connects to the MySQL database using
    credentials from environment variables.
    """

    # Fetching credentials from environment variables with defaults

    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    # Establishing the connection to the database

    conn = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return conn


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    logging.Formatter
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """class initialization"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR
                )


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    filter_datum functioni
    parameters:
        fieds: list
        redaction: string
        message: string
        separator
    """

    pattern = '|'.join(f'(?<={field}=)[^{separator}]+' for field in fields)
    return re.sub(pattern, redaction, message)


def get_logger() -> logging.Logger:
    """function get logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def main():
    """Main function to retrieve and display data from users table."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)

    for row in cursor:
        message = "; ".join(f"{key}={value}" for key, value in row.items())
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
