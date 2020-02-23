from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    status = models.CharField(max_length=10, choices=[('S', 'Student'), ('P', 'Professor')], blank=False)

    class Meta(AbstractUser.Meta):
        pass


class Course(models.Model):
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    students = models.ManyToManyField(AdvUser, related_name='students_set')
    professors = models.ManyToManyField(AdvUser, related_name='professors_set')

    def __str__(self):
        return f'{self.name}'


class Lecture(models.Model):
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, blank=False)
    topic = models.CharField(max_length=100, blank=False)
    presentation = models.FileField(upload_to=None, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, related_name='lectures')

    def __str__(self):
        return f'{self.topic}'


class Homework(models.Model):
    task = models.TextField(blank=False)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{self.task}'


class FinishedHomework(models.Model):
    solution = models.TextField(blank=True)
    finished = models.BooleanField(blank=False, default=False)
    mark = models.SmallIntegerField(blank=True)
    owner = models.ForeignKey(AdvUser, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.solution}'


class Comment(models.Model):
    text = models.TextField(blank=False)
    owner = models.ForeignKey(AdvUser, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'