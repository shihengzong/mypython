from django.db import models

# Create your models here.
 
class Person(models.Model):
    p_name = models.CharField(max_length=20, null=False, unique=True)
    p_age = models.IntegerField(default=10)
    p_sex = models.BooleanField(default=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.p_name

    class Meta:
        db_table = "zsh_person"