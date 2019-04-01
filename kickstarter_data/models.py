from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 1024)
    category = models.CharField(max_length = 1024)
    main_category = models.CharField(max_length = 1024)
    currency = models.CharField(max_length = 1024)
    deadline = models.CharField(max_length = 1024)
    goal = models.FloatField()
    launched = models.CharField(max_length = 1024)
    pledged = models.FloatField()
    state = models.CharField(max_length = 1024)
    backers = models.FloatField()
    country = models.CharField(max_length = 1024)
    usd_pledged = models.FloatField()

    def __str__(self):
        return 'Project: {}'.format(self.title)

    def __repr__(self):
        return '<Project: {}>'.format(self.title)
