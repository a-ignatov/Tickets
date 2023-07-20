from django import forms

from ticket_DTB.models import Ticket  

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_category','description',)
