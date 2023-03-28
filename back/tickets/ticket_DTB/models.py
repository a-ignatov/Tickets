from django.contrib.auth import get_user_model
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)
from django.db import models
import uuid

User = get_user_model()


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ADMIN = 'ADMIN'
    REPAIR = 'REPAIR'
    PRINTER = 'PRINTER'
    CLEANING = 'CLEANING'
    OTHER = 'OTHER'
    TICKET_CATEGORY_CHOICES = [
        (ADMIN, 'ADMIN'),
        (REPAIR, 'REPAIR'),
        (PRINTER, 'PRINTER'),
        (CLEANING, 'CLEANING'),
        (OTHER, 'OTHER'),
    ]
    ticket_category = models.CharField(
        choices=TICKET_CATEGORY_CHOICES,
        default=OTHER,
        max_length = 50
    )
    CREATED = 'CREATED'
    IN_PROGRESS = 'IN_PROGRESS'
    CLOSED = 'CLOSED'
    DECLINED = 'DECLINED'
    TICKET_STATUS_CHOICES = [
        (CREATED, 'CREATED'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (CLOSED, 'CLOSED'),
        (DECLINED, 'DECLINED'),
    ]
    ticket_status = models.CharField(
        choices=TICKET_STATUS_CHOICES,
        default=CREATED,
        max_length = 50
    )
    description = models.TextField(
        'Ticket verbose description',
        max_length=1500,
    )
    date_time_created = models.DateTimeField(
        'Ticket creation time',
        auto_now_add=True,
    )
    date_time_modified = models.DateTimeField(
        'Ticket modification time',
        auto_now=True,
    )

    class Meta:
        ordering = ('date_time_modified', )
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return self.description
