from django.shortcuts import  render
from ticket_DTB . models import Ticket
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.conf import settings

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import SingleObjectMixin
from ticket_DTB.forms import TicketForm
from .utils import paginate_page



def main(request):
    tickets_list = Ticket.objects.all()
    paginator = Paginator(tickets_list, settings.PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page_obj': paginate_page(request, tickets_list),
        'page': page
    }
    return render(
        request,
        'index.html',
        context
    )

class TicketChangeView(UpdateView,SingleObjectMixin):  
    model = Ticket
    template_name = "index.html"
    form_class = TicketForm
    def get_success_url(self):
        return ('/')