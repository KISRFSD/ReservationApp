from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.IntegerField()
    comments = models.TextField()

    def __unicode__(self):
        return u"{} {}".format(self.feedDate, self.name)
