from django.shortcuts import  render,redirect,get_object_or_404
from ticket_DTB . models import Ticket
from django.core.paginator import Paginator
from django.conf import settings
from ticket_DTB.forms import TicketForm
from .utils import paginate_page



def main(request):
    tickets_list = Ticket.objects.all().order_by("-date_time_modified")
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

def ticket_update(request, pk):
    original_ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketForm(request.POST or None,
                    instance=original_ticket)
    if request.method == "POST" and form.is_valid():
        ticket = form.save(commit=False)
        original_ticket.ticket_status = ticket.ticket_status
        original_ticket.save()
        return redirect('/',)
    return redirect('/',)

