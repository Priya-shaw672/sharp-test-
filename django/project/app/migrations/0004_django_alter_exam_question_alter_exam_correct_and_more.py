# Generated by Django 5.0.1 on 2024-01-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_gk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=255)),
                ('option2', models.CharField(max_length=255)),
                ('option3', models.CharField(max_length=255)),
                ('option4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('marks', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='Question',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='correct',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='option3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='option4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='Question',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='correct',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='marks',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='option3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gk',
            name='option4',
            field=models.CharField(max_length=255),
        ),
    ]