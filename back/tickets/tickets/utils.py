from django.conf import settings
from django.core.paginator import Paginator


def paginate_page(request, tickets_list):
    paginator = Paginator(tickets_list, settings.PER_PAGE)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)