from django.db import models
from django.contrib.auth.models import User

class Train(models.Model):
    trainNumber = models.IntegerField(primary_key = True, help_text= "Train number should be of 4-5 characters and should be unique")
    starts = models.CharField(max_length = 20)
    ends = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.trainNumber, self.starts, self.ends) 


class ReleasedTrain(models.Model):
    train = models.ForeignKey('Train', on_delete=models.CASCADE, related_query_name='released_trains', verbose_name = 'Train Number')
    departureDate = models.DateField()
    departureTime = models.TimeField()
    maxAC = models.IntegerField()
    maxSL = models.IntegerField()
    currAC = models.IntegerField()
    currSL = models.IntegerField()
    releasedDate = models.DateField()
    releasedTime = models.TimeField()

    def __str__(self):
        return "{} - {} - {}".format(self.train, self.departureDate, self.departureTime)


class BookingAgent(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"), 
        ("F", "Female"), 
        ("O", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 20)
    creditCardNo = models.BigIntegerField(unique=True)
    address = models.CharField(max_length  = 200)    
    age = models.IntegerField()
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 2, default = "O")
    email = models.EmailField(unique = True)
    

class Coach(models.Model):
    
    COACH_CHOICES = (
        ('SL', "Sleeper"), 
        ('AC', "AC"),
    )
    releasedTrain = models.ForeignKey('ReleasedTrain', on_delete=models.CASCADE)
    coachType = models.CharField(choices = COACH_CHOICES, max_length = 2)
    coachNumber = models.IntegerField()


class Berth(models.Model):

    COACH_CHOICES = (
        ('SL', "Sleeper"), 
        ('AC', "AC"),
    )

    BERTH_CHOICES = (
        ('LB', 'LB'),
        ('UB', 'UB'),
        ('MB', 'MB'),
        ('SL', 'SL'), 
        ('SU', 'SU'),
    )
    berthNumber = models.IntegerField()
    coachType = models.CharField(choices = COACH_CHOICES, max_length = 2)
    berthType = models.CharField(choices = BERTH_CHOICES, max_length = 2)


    def __str__(self):
        return "{} - {} - {}".format(self.coachType, self.berthType, self.berthNumber)


class Seat(models.Model):
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
    berth = models.ForeignKey('Berth', on_delete=models.CASCADE)


class Books(models.Model):
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    pnr = models.ForeignKey('Pnr', on_delete=models.CASCADE)


class Passenger(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"), 
        ("F", "Female"), 
        ("O", "Other"),
    )

    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 2, default = "O")


class Pnr(models.Model):
    bookingAgent = models.ForeignKey('BookingAgent', on_delete=models.CASCADE)



