from django.db import models

# Create your models here.


class PredictMark (models.Model) :
    time_study = models.IntegerField(default=0)
    num_course = models.IntegerField(default=0)
    final_mark = models.IntegerField(default=0)
    def __str__(self):
        return f"Time Study: {self.time_study}, Number of Courses: {self.num_course}, Final Mark: {self.final_mark}"



