from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_birth = models.DateField()
    password1 = models.CharField(max_length=20)
    weight = models.FloatField(blank=True)



# ['%d/%m/%Y']