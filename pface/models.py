import os.path
from django.db import models

class Prints(models.Model):
   file = models.ForeignKey('File')
   print_start = models.DateTimeField(auto_now_add=True)
   print_completed = models.DateTimeField()

class File(models.Model):
   gcode_file = models.FileField(upload_to=os.path.join(os.path.abspath('.'), 'gcode_uploads'))
   uploaded = models.DateTimeField(auto_now_add=True)
   
   # Overwrite delete
   def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.gcode_file.storage, self.gcode_file.path
        # Delete the model before the file
        super(File, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

class Printer(models.Model):
   printer_name = models.CharField(max_length=128)
   status = models.CharField(max_length=128)
   connection_dttm = models.DateTimeField()
   port = models.CharField(max_length=128)
   loaded_file = models.ForeignKey('File')
