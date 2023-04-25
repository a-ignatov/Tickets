from django.shortcuts import  render
from django.shortcuts import get_object_or_404
from ticket_DTB . models import Ticket
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from tickets import settings

User = get_user_model()




def main(request):
    tickets_list = Ticket.objects.all()
    paginator = Paginator(tickets_list, settings.PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page}
    )
