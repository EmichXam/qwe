# Generated by Django 4.0.6 on 2022-08-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_test_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='test',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='test',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='test',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='test',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='test',
            name='question',
        ),
        migrations.AddField(
            model_name='test',
            name='answer1_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант1'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer1_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант1'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer1_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант1'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer1_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант1'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer1_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант1'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer2_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант2'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer2_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант2'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer2_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант2'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer2_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант2'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer2_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант2'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer3_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант3'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer3_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант3'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer3_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант3'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer3_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант3'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer3_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант3'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer4_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант4'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer4_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант4'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer4_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант4'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer4_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант4'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer4_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант4'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный вариант ответа'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный вариант ответа'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный вариант ответа'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный вариант ответа'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный вариант ответа'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_1',
            field=models.CharField(max_length=200, null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_2',
            field=models.CharField(max_length=200, null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_3',
            field=models.CharField(max_length=200, null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_4',
            field=models.CharField(max_length=200, null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вопрос'),
        ),
    ]
