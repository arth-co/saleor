from django.db import models
from django.utils.translation import ugettext
from datetime import datetime

class Weekday(models.Model):
    iso_number = models.PositiveSmallIntegerField(primary_key=True,editable=True)
    name = models.CharField(max_length=3,editable=True)
    verbose_name = models.CharField(max_length='20',editable=True)

    def __str__(self):
        return self.name

def populate_weekday_table():
    for i in range(0,7):
        dt = datetime(2015,10,5+i)
        iso_number = dt.isoweekday()
        name = ugettext(dt.strftime('%A'))[:3].upper()
        verbose_name = ugettext(dt.strftime('%A'))
        weekday = Weekday(iso_number=iso_number,
                          name=name,
                          verbose_name=verbose_name)
        weekday.save()



