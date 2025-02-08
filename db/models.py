from django.db import models

class FiringCurve(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    temp = models.FloatField()
    cover_state = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

class KilnData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    inside_temp = models.FloatField()
    cover_temp = models.FloatField()
    air_temp = models.FloatField()
    ir_temp = models.FloatField()
    expected_temp = models.FloatField()
    triack_on_time = models.FloatField()
    triack_off_time = models.FloatField()
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    weight = models.FloatField()
    cover_state = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"Data at {self.time}"