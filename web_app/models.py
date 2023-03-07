from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False, blank=True)
    roll = models.PositiveIntegerField(null=False,primary_key=True)
    course = models.CharField(max_length=150, null=True)
    stream = models.CharField( max_length=50, null=True)
    gender = models.CharField( max_length=30, null=True)
    year = models.PositiveSmallIntegerField(null=True)
    present_days = models.PositiveSmallIntegerField(default=1)
    total_days = models.PositiveBigIntegerField(default=1)


    def __str__(self):
        return  '%s %s %d %s %s %s %d %d %d'%(self.name, self.email, self.roll, self.course, self.stream, self.gender, self.year, self.present_days, self.total_days)

