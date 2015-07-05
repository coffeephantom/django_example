from django.db import models

# Create your models here.
#Example from django website

class Question(models.Model):
    """Question is somthing that needed to be polled."""
    #define the area to show the question, the max length is 200
    question_text = models.CharField(max_length=200)

    #define the day that the question was published
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    """Choice is for people to selected"""
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
        
