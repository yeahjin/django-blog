# Generated by Django 3.0.5 on 2020-05-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imge',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
