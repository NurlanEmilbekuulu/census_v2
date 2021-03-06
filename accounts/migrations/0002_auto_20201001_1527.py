# Generated by Django 3.1.1 on 2020-10-01 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0007_auto_20201001_1527'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профилдер'},
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='census.district'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Администрация'), (2, 'Модератор')], default=1),
        ),
    ]
