from django.db import models

# Create your models here.
class Todo(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  cname = models.CharField(
    max_length=50,
  )

  EmailID = models.CharField(
    max_length=100,
  )


  class Meta:
    db_table = 'Todos'
