
from django import forms  

from .models import Ticket  

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_status','description','ticket_category')
