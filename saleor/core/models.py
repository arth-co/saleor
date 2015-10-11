from django.db import models
from django.utils.translation import ugettext
import datetime
class Weekday(models.Model):
    iso_number = models.PositiveSmallIntegerField(primary_key=True,editable=False)
    name = models.CharField(max_length=3,editable=False)
    verbose_name = models.CharField(max_length='20',editable=False)

    def __str__(self):
        return self.name

class DeliverySlot(models.Model):
    start_time = models.TimeField(editable=True, null=True)
    end_time = models.TimeField(editable=True, null= True)

    def __str__(self):
        return ugettext(self.start_time.strftime('%l:%M%p') + '-' + self.end_time.strftime('%l:%M%p'))




def populate_weekday_table():
    for i in range(0,7):
        dt = datetime.datetime(2015,10,5+i)
        iso_number = dt.isoweekday()
        name = ugettext(dt.strftime('%A'))[:3].upper()
        verbose_name = ugettext(dt.strftime('%A'))
        weekday = Weekday(iso_number=iso_number,
                          name=name,
                          verbose_name=verbose_name)
        weekday.save()

def populate_delivery_slots():

    delivery_slots = [(datetime.time(6,0),datetime.time(8,0)),(datetime.time(16,0),datetime.time(18,0))]

    for start_time,end_time in delivery_slots:
        delivery_slot = DeliverySlot(start_time=start_time, end_time=end_time)
        delivery_slot.save()


