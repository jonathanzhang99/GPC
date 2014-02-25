from django.db import models


class member(models.Model):
    GRADES = [
        (9, 'Freshman'),
        (10, 'Sophomore'),
        (11, 'Junior'),
        (12, 'Senior'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grade = models.IntegerField(max_length=2, choices=GRADES)
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
