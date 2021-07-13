from django.db import models

# Create your models here.

class Train(models.Model):
    Train_name = models.CharField(max_length=20)
    train_id = models.AutoField(primary_key=True)
    maxSeats = models.IntegerField(default=100)

    def __str__(self):
        return self.Train_name

class Trip(models.Model):
    Trip_name = models.CharField(max_length=20)
    trip_id = models.AutoField(primary_key=True)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    reserved_seats = models.IntegerField(default=0)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.Trip_name
