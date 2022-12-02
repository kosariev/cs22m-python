from django.db import models


class Cars(models.Model):
    type = models.CharField(max_length=20)
    vendor = models.CharField(max_length=64)
    plate = models.CharField(max_length=8)

    class Meta:
        db_table = "cars"
        app_label = "coursework"
