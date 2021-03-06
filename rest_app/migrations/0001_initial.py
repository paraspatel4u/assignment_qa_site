# Generated by Django 2.1.5 on 2019-04-13 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_content', models.TextField(max_length=50000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField(max_length=1000)),
                ('commented_by', models.TextField(max_length=20)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=100)),
                ('question_content', models.TextField(max_length=50000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.TextField(max_length=20)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.Question'),
        ),
    ]
