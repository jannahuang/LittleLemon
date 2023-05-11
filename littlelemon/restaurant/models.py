from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.SmallIntegerField(default=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=6)

    def __str__(self): 
        return self.name
    
