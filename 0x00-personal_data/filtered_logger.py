#!/usr/bin/env python3
"""
This module that returns the log message obfuscated
"""


import re
from typing import Any


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> Any:
    """ A function that returns the log message obfuscated """
    pattern = (r"(?<=\b(" + "|".join(map(re.escape, fields)) + r")=)"
                  r"[^" + re.escape(separator) + r"]+")
    return re.sub(pattern, redaction, message)
