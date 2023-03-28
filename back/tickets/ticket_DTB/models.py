from django.contrib.auth import get_user_model
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)
from django.db import models
import uuid
User = get_user_model()

    

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(
        'Brief name',
        max_length=150,
        unique=True,
    )
    description = models.TextField(
        'Unit of measure',
        max_length=150,
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique_ingredient')
        ]

    def __str__(self):
        return self.name
