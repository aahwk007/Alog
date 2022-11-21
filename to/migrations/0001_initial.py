# Generated by Django 4.1.3 on 2022-11-19 17:16

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('WORKING', 'WORKING'), ('DONE', 'DONE'), ('OVERDUE', 'OVERDUE')], default='OPEN', max_length=20)),
                ('due_date', models.DateTimeField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
