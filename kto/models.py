from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=5)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Task(models.Model):
    low = 0
    normal = 1
    high = 2
    priority_choices = (
        (low, 'Low'),
        (normal, 'Normal'),
        (high, 'High'),
    )
    task_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(default=normal, choices=priority_choices)

    def __str__(self):
        return self.task_name