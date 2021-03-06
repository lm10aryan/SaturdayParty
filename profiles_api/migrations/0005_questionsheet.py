# Generated by Django 2.2 on 2020-07-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_remove_farmer_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSheet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('past_question', models.CharField(max_length=255)),
                ('future_question', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('constraint', models.CharField(blank=True, default='', max_length=50)),
                ('options_text', models.CharField(blank=True, default='', max_length=300)),
                ('options_value', models.CharField(blank=True, default='', max_length=50)),
                ('question_tag', models.CharField(max_length=100)),
                ('past_condition', models.CharField(blank=True, default='', max_length=100)),
                ('future_condition', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
