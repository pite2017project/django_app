# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Classes(models.Model):
    CLASSES = (
        ('MMF I', 'Matematyczne Metody Fizyki'),
        ('PP', 'Programowanie Proceduralne'),
        ('MI', 'Matematyka I')
    )
    classes = models.CharField(max_length=10, choices=CLASSES)

    def make_class(self):
        self.save()

    def __unicode__(self):
        return self.classes


class Field_of_study(models.Model):
    FIELD_OF_STUDY = (
        ('FT', 'Fizyka Techniczna'),
        ('FM', 'Fizyka Medyczna'),
        ('IS', 'Informatyka Stosowana')
    )
    fieldOfStudy = models.CharField(max_length=10, choices=FIELD_OF_STUDY)

    def make_field_of_study(self):
        self.save()

    def __unicode__(self):
        return self.fieldOfStudy


class Year(models.Model):
    YEARS = (
        ('I', 'year I'),
        ('II', 'year II'),
        ('III', 'year III'),
        ('IV', 'year IV'),
        ('V', 'year V')
    )
    year = models.CharField(max_length=5, choices=YEARS)

    def make_year(self):
        self.save()

    def __unicode__(self):
        return self.year



class Grades_group(models.Model):
    fieldOfStudy = models.ManyToManyField(Field_of_study)
    year = models.ManyToManyField(Year)
    classes = models.ManyToManyField(Classes)
    gradesGroup = str(fieldOfStudy) + " " + str(year)
    #user

    def make_grades_group(self):
        self.save()

    def __unicode__(self):
        return self.gradesGroup


# class Student(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fieldOfStudy = models.ForeignKey(Field_of_study, on_delete=models.CASCADE )
#     year = models.ForeignKey(Year, on_delete=models.CASCADE)
#     classes = models.ManyToManyField(Classes)
#
#     def make_student(self):
#         self.save()
#
#     def __unicode__(self):
#         return self.user
#
#
# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_student(sender, instance, **kwargs):
#     instance.user.save()
