#!/usr/bin/env python3
""" This module contains a function to obfuscate log messages"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
