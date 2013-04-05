from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)


class StudentGroup(models.Model):
    """Depending on the context, a representation of a educational level,
    class, or student group of some kind."""
    name = models.CharField(max_length=200)


class GroupNotebook(models.Model):
    """Notebook where the teacher sends lecture notes, materials, and
    other things that are meant to be read and edited by all students."""
    group = models.ForeignKey(StudentGroup)


class Student(models.Model):
    groups = models.ManyToManyField(StudentGroup)
    email = models.EmailField()
    evernote_user_id = models.CharField(max_length=200)


class StudentNotebook(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(StudentGroup)
    evernote_guid = models.CharField(max_length=200)


class GroupAssignment(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(StudentGroup)


class Assignment(models.Model):
    group_assignment = models.ForeignKey(GroupAssignment)
    student = models.ForeignKey(Student)
    evernote_note_guid = models.CharField(max_length=200)



