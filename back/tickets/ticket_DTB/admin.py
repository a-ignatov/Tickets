from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket_category', 'ticket_status', 'description',
                    'date_time_created', 'date_time_modified')
    search_fields = ('description', 'ticket_status')
    list_filter = (
        'ticket_status',
        'date_time_created',
        'date_time_modified',
        'ticket_category',
    )


admin.site.register(Ticket, TicketAdmin)
