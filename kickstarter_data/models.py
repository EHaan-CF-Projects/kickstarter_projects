from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 1024)
    category = models.CharField(max_length = 1024)
    main_category = models.CharField(max_length = 1024)
    currency = models.CharField(max_length = 1024)
    deadline = models.CharField(max_length = 1024)
    goal = models.FloatField(0.0)
    launched = models.CharField(max_length = 1024)
    pledged = models.FloatField(0.0)
    state = models.CharField(max_length = 1024)
    backers = models.FloatField(0.0)
    country = models.CharField(max_length = 1024)
    usd_pledged = models.FloatField(0.0)
    usd_pledged_real = models.FloatField(0.0)
    usd_goal_real = models.FloatField(0.0)

    def __str__(self):
        return 'Project: {}'.format(self.title)

    def __repr__(self):
        return '<Project: {}>'.format(self.title)
