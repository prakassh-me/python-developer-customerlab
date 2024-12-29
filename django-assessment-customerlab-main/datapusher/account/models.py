from django.db import models

# Create your models here.


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Accounts (models.Model):
    eml_id = models.CharField(max_length=50, unique=True)
    acc_id = models.CharField(max_length=50, primary_key=True, unique=True)
    acc_nme = models.CharField(max_length=255)
    acc_sec_tkn = models.TextField()
