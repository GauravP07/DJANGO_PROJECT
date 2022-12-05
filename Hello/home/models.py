from django.db import models

# Create your models here.
# contact is a table in DataBase
# make migration - create change and store in a file
# migrate - apply the pending change created by makemigreations
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    