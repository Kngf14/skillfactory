# Generated by Django 4.1.5 on 2023-06-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sprint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesOfMountains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField()),
                ('title', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='other_title',
        ),
        migrations.AddField(
            model_name='mountain',
            name='other_titles',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='beauty_title',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='connect',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fam',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='otc',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='MountainImages',
        ),
        migrations.AddField(
            model_name='imagesofmountains',
            name='mountain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Sprint.mountain'),
        ),
    ]
