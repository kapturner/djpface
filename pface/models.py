import os.path
from django.db import models

class Prints(models.Model):
   file = models.ForeignKey('File')
   print_start = models.DateTimeField(auto_now_add=True)
   print_completed = models.DateTimeField()

class File(models.Model):
   gcode_file = models.FileField(upload_to=os.path.join(os.path.abspath('.'), 'gcode_uploads'))
   uploaded = models.DateTimeField(auto_now_add=True)

class Printer(models.Model):
   printer_name = models.CharField(max_length=128)
   status = models.CharField(max_length=128)
   connection_dttm = models.DateTimeField()
   port = models.CharField(max_length=128)
   loaded_file = models.ForeignKey('File')
