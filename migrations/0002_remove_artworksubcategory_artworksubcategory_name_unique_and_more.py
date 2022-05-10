# Generated by Django 4.0.4 on 2022-05-10 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arosenius', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='artworksubcategory',
            name='artworksubcategory_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='documentcategory',
            name='documentcategory_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='documentsubcategory',
            name='documentsubcategory_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='imagecontent',
            name='imagecontent_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='lettersubcategory',
            name='lettersubcategory_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='material',
            name='material_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='museum',
            name='museum_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='photographsubcategory',
            name='photographsubcategory_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='place',
            name='place_name_unique',
        ),
        migrations.RemoveConstraint(
            model_name='relicsubcategory',
            name='relicsubcategory_name_unique',
        ),
    ]
