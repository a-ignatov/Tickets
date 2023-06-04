from django.shortcuts import  render
from ticket_DTB . models import Ticket
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from tickets import settings





def paginate_page(request, tickets_list):
    paginator = Paginator(tickets_list, settings.PER_PAGE)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

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