# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def populate(apps, schema_editor):
    Category = apps.get_model("rango", "Category")
    Page = apps.get_model("rango", "Page")

    python_cat = Category(name='Python')
    python_cat.save()

    Page(category=python_cat,
         title="Official Python Tutorial",
         url="http://docs.python.org/2/tutorial/").save()

    Page(category=python_cat,
         title="How to Think like a Computer Scientist",
         url="http://www.greenteapress.com/thinkpython/").save()

    Page(category=python_cat,
         title="Learn Python in 10 Minutes",
         url="http://www.korokithakis.net/tutorials/python/").save()

    django_cat = Category(name="Django")
    django_cat.save()

    Page(category=django_cat,
         title="Official Django Tutorial",
         url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/").save()

    Page(category=django_cat,
         title="Django Rocks",
         url="http://www.djangorocks.com/").save()

    Page(category=django_cat,
         title="How to Tango with Django",
         url="http://www.tangowithdjango.com/").save()

    frame_cat = Category(name="Other Frameworks")
    frame_cat.save()

    Page(category=frame_cat,
         title="Bottle",
         url="http://bottlepy.org/docs/dev/").save()

    Page(category=frame_cat,
         title="Flask",
         url="http://flask.pocoo.org").save()


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]
