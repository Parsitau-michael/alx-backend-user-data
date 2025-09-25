#!/usr/bin/env python3
""" This module contains a function to obfuscate log messages"""

import re
from typing import List
import logging


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
        """Formats values in incoming log records"""
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION,
                                  record.msg, RedactingFormatter.SEPARATOR)
        final = super().format(record)
        return final


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """
    Function to obfuscate PII fields in log files

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: Log message to process
        separator: Character separating fields in the message

    Returns:
        Obfuscated log message with PII fields redacted
    """
    pattern = rf'({"|".join(fields)})=.*?({separator})'
    obfuscated = re.sub(pattern, r"\1="+redaction+r"\2", message)
    return obfuscated
