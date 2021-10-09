from django import template
from .forms import  *
import urllib

register= template.Library()

@register.inclusion_tag("pages/base.html")
def search_box(request):
    query = request.GET.get("query",'')
    form = SearchForm({"query":query})
    return {"form":form}


@register.inclusion_tag("pages/pagination_links.html")
def paginatotion_links(request,paginator):
    raw_params= request.GET.copy()
    page=raw_params.get('page',1)
    p = paginator.page(page)

    try:
        del raw_params["page"]
    except KeyError:
        pass
    
    params= urllib.urlencode(raw_params)

    return {"request":request,"paginator":paginator,"p":p,"params":params}