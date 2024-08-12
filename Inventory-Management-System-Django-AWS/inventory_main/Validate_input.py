import re
import logging
from django.core.exceptions import ValidationError


logger = logging.getLogger('custom_logger')
logger.setLevel(logging.INFO)



def validate(data):
    print("validate")
        
    if not isinstance(data, str):
        logger.warning("Invalid input: input must be a string")
        raise ValidationError("Invalid input: input must be a string")
        return False
    
    # Check for SQL Injection patterns
    sql_injection_patterns = [
        re.compile(r'(--|\b(select|union|insert|update|delete|drop|alter)\b)', re.IGNORECASE),
        re.compile(r'(\bexec\b|\bexecute\b)', re.IGNORECASE)
    ]
    for pattern in sql_injection_patterns:
        if pattern.search(data):
            logger.warning(f"SQL injection attempt detected: {data}")
            raise ValueError("Invalid input: possible SQL injection detected")
            return False
            #raise ValidationError("Invalid input: possible SQL injection detected")

    # Check for XSS patterns
    xss_patterns = [
        re.compile(r'<script.*?>.*?</script>', re.IGNORECASE),
        re.compile(r'javascript:', re.IGNORECASE)
    ]
    for pattern in xss_patterns:
        if pattern.search(data):
            logger.warning("Invalid input: possible XSS detected")
            raise ValidationError("Invalid input: possible XSS detected")
            return False

    # Check for command injection patterns
    command_injection_patterns = [
        re.compile(r'(\||;|&|`|\$|\(|\)|<|>|\[|\]|\{|\}|\*|\?|!|~)', re.IGNORECASE),
        re.compile(r'(\bsh\b|\bbash\b|\bperl\b|\bpython\b|\bphp\b)', re.IGNORECASE)
    ]
    for pattern in command_injection_patterns:
        if pattern.search(data):
            logger.warning("Invalid input: possible command injection detected")
            raise ValidationError("Invalid input: possible command injection detected")
            return False

    # Check for LDAP injection patterns
    ldap_injection_patterns = [
        re.compile(r'(\(|\)|&|\||=)', re.IGNORECASE)
    ]
    for pattern in ldap_injection_patterns:
        if pattern.search(data):
            logger.warning("Invalid input: possible LDAP injection detected")
            raise ValidationError("Invalid input: possible LDAP injection detected")
            return False

    # Check for XML injection patterns
    xml_injection_patterns = [
        re.compile(r'(<\?xml|<!DOCTYPE|<!ENTITY)', re.IGNORECASE)
    ]
    for pattern in xml_injection_patterns:
        if pattern.search(data):
            logger.warning("Invalid input: possible XML injection detected")
            raise ValidationError("Invalid input: possible XML injection detected")
            return False

    return True




def logMessage(username):
    logger.info("WARNING:sql_injection:SQL Injection attempt detected: {}".format(username))
    print("WARNING:sql_injection:SQL Injection attempt detected: {}".format(username))
