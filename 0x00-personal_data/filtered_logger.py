#!/usr/bin/env python3
""" This module contains a function to obfuscate log messages"""

import re

def filter_datum(fields, redaction, message, separator):
    """Function to obfuscate PII fields in log files"""
    pattern = rf'({"|".join(fields)})=.*?({separator})'
    obfuscated = re.sub(pattern, r"\1="+redaction+r"\2", message)
    return obfuscated
