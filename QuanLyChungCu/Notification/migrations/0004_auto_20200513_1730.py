# Generated by Django 3.0.6 on 2020-05-13 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notification', '0003_auto_20200513_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='manage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manage_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notify_user',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notify_user',
            name='notify_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_id', to='Notification.Notify'),
        ),
    ]