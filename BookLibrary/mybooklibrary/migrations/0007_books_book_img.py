# Generated by Django 2.2 on 2019-04-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybooklibrary', '0006_users_user_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='book_img'),
        ),
    ]
