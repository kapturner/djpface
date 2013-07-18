import subprocess
import sys
from django.http import HttpResponse
from django.conf import settings
from printrun.pronsole import pronsole

# PRONSOLE = subprocess.Popen(['python', settings.PRONSOLE_PATH],
#                          stdin=subprocess.PIPE)

PRONSOLE = pronsole()

def print_http_response(f):
    '''
        http://chase-seibert.github.io/blog/2010/08/06/redirect-console-output-to-a-django-httpresponse.html
        Wraps a python function that prints to the console, and 
        returns those results as a HttpResponse (HTML)
    '''
    
    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)     
    
    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__    
        return HttpResponse([c for c in printed.content ])         
    return new_f