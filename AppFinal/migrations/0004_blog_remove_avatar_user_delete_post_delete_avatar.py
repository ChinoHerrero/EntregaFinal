# Generated by Django 4.1.5 on 2023-02-24 05:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0003_rename_content_post_body_post_image_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(default='test', upload_to='images/')),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
