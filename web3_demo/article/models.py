from django.db import models


# Create your models here.
class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=False, unique=True)
    content = models.CharField(default="", max_length=200)
    is_use = models.BooleanField(default=True)

    def __str__(self):
        res = "{id:%s, title:%s, content:%s, is_use:%s}" % (
            self.id, self.title, self.content, self.is_use)
        return res

    class Meta:
        db_table = "zsh_article"