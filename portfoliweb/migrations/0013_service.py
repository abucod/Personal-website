# Generated by Django 4.2 on 2023-04-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliweb', '0012_delete_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='./images')),
                ('text', models.TextField()),
            ],
        ),
    ]