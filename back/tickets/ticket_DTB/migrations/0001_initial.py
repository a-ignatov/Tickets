# Generated by Django 4.1.7 on 2023-03-28 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ticket_category', models.CharField(choices=[('ADMIN', 'ADMIN'), ('REPAIR', 'REPAIR'), ('PRINTER', 'PRINTER'), ('CLEANING', 'CLEANING'), ('OTHER', 'OTHER')], default='OTHER', max_length=50)),
                ('ticket_status', models.CharField(choices=[('CREATED', 'CREATED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('CLOSED', 'CLOSED'), ('DECLINED', 'DECLINED')], default='CREATED', max_length=50)),
                ('description', models.TextField(max_length=1500, verbose_name='Ticket verbose description')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Ticket creation time')),
                ('date_time_modified', models.DateTimeField(auto_now=True, verbose_name='Ticket modification time')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ('date_time_modified',),
            },
        ),
    ]