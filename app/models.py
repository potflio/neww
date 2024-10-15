from django.db import models

class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    from_place = models.CharField(max_length=20)
    to_place = models.CharField(max_length=20)
    from_place_tamil = models.CharField(max_length=20, null=True)
    to_place_tamil = models.CharField(max_length=20, null=True)
    
    class Meta:
        db_table = 'booking_table'
