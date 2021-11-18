from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
   name = models.CharField(max_length=100)
   capital = models.CharField(max_length=100)
   code = models.CharField(max_length = 100)
   currency_code = models.CharField(max_length = 100)
   flag = models.CharField(max_length = 200)

   # def __init__(self, name, capital, code, currency_code, flag):
   #    self.name = name
   #    self.capital = capital
   #    self.code = code
   #    self.currency_code = currency_code
   #    self.flag = flag


   
class PassportProfile(models.Model):
   traveler = models.OneToOneField(User, on_delete=models.CASCADE)

class Visit(models.Model):
   code = models.ForeignKey(Country, on_delete=models.CASCADE)
   visit_blurb = models.TextField()
   traveler_name = models.ForeignKey(PassportProfile, on_delete=models.CASCADE)


