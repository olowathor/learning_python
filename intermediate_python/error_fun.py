'''
try:
    a+b
except Exception as e:
    print(str(e))
'''

import sys
import logging

def error_handling():
    return ' {} - {} - on line {}'.format(sys.exc_info()[0].__name__,
                                                sys.exc_info()[1],
                                                sys.exc_info()[2].tb_lineno) 
try:
    a+b
except Exception:
    logging.error(error_handling())
    

