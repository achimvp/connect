from django.db import models
from django.contrib.gis.db.models import PointField
from django.db import models

# Create your models here.
#class Entry(models.Model):
#    point = PointField()
#
#    @property
#    def lat_lng(self):
#        return list(getattr(self.point, 'coords', [])[::-1])