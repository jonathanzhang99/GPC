from django.db import models


class Member(models.Model):
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

class Post(models.Model):
    author = models.ForeignKey(Member)
#    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.content