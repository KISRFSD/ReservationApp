from django.db import models

# Create your models here.

class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    destination = models.CharField(max_length=100)
    event_status = models.BooleanField()
    instructor = models.TextField() #change to forign key feild
    gathering_point = models.CharField(max_length=100)
    max_seats = models.IntegerField()
    note = models.TextField()

    def __unicode__(self):
        return u"{}, {}".format(self.start_time, self.destination)