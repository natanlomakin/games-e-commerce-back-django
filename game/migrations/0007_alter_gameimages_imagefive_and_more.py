# Generated by Django 4.1 on 2022-09-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_gameimages_imagefive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameimages',
            name='imageFive',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gameimages',
            name='imageFour',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gameimages',
            name='imageOne',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gameimages',
            name='imageThree',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gameimages',
            name='imageTwo',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to='images/'),
        ),
    ]