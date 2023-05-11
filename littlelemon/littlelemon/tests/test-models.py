from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import date


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Julie", no_of_guests=2, booking_date=date.today())
        booking_date = date.today()
        self.assertEqual(str(item), f"booking date: {booking_date}")
