# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations

def reverse(_apps, _schema_editor):
    pass

def populate(apps, schema_editor):
    Category = apps.get_model("rango", "Category")
    Page = apps.get_model("rango", "Page")

    python_cat, created = Category.objects.get_or_create(name='Python')

    Page.objects.get_or_create(category=python_cat.id,
         title="Official Python Tutorial",
         url="http://docs.python.org/2/tutorial/")

    Page.objects.get_or_create(category=python_cat,
         title="How to Think like a Computer Scientist",
         url="http://www.greenteapress.com/thinkpython/")

    Page.objects.get_or_create(category=python_cat,
         title="Learn Python in 10 Minutes",
         url="http://www.korokithakis.net/tutorials/python/")

    django_cat, created = Category.objects.get_or_create(name="Django")

    Page.objects.get_or_create(category=django_cat,
         title="Official Django Tutorial",
         url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    Page.objects.get_or_create(category=django_cat,
         title="Django Rocks",
         url="http://www.djangorocks.com/")

    Page.objects.get_or_create(category=django_cat,
         title="How to Tango with Django",
         url="http://www.tangowithdjango.com/")

    frame_cat, created = Category.objects.get_or_create(name="Other Frameworks")

    Page.objects.get_or_create(category=frame_cat,
         title="Bottle",
         url="http://bottlepy.org/docs/dev/")

    Page.objects.get_or_create(category=frame_cat,
         title="Flask",
         url="http://flask.pocoo.org")


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate, reverse_code=reverse)
    ]
