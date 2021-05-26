from django.http import JsonResponse
from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import TableForm


# Create your views here.

def paginate(queryset, page_number):
    paginator = Paginator(queryset, 5)
    page = page_number
    try:
        queryset = paginator.page(page)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    page_count = []
    for i in range(paginator.num_pages):
        page_count.append(i + 1)
    data = {
        "queryset": queryset, "page_count": page_count
    }
    return data


def index(request):
    query = Table.objects.all()
    query = paginate(query, 1)
    data = {"query": query.get("queryset"), "pages":query.get("page_count")}
    return render(request, 'index.html', data)


def pagination(request):
    query = Table.objects.all()
    if request.GET.get("is_ajax"):
        query = paginate(query, request.GET.get("current_page")).get("queryset").object_list
        data = []
        for q in query.values("date", "title", "count", "distance"):
            obj = {
                "date": q['date'],
                "title": q['title'],
                "count": q['count'],
                "distance": q['distance'],
            }
            data.append(obj)
        return JsonResponse({"data": data})
    return JsonResponse({"data": False})


def search_data(request):
    queryset = None
    if request.GET:
        option_name = request.GET.get("option")
        column_name = request.GET.get("column")
        query = request.GET.get("search")
        if option_name == "contains":
            if column_name == "title":
                queryset = Table.objects.filter(title__icontains=query).values("date", "title", "count",
                                                                               "distance")
            elif column_name == "count":
                queryset = Table.objects.filter(count__icontains=query).values("date", "title", "count",
                                                                               "distance")
            elif column_name == "distance":
                queryset = Table.objects.filter(distance__icontains=query).values("date", "title",
                                                                                  "count",
                                                                                  "distance")
        elif option_name == "equal":
            try:
                if column_name == "title":
                    queryset = Table.objects.filter(title=query).values("date", "title", "count",
                                                                        "distance")
                elif column_name == "count":
                    queryset = Table.objects.filter(count=query).all().values("date", "title", "count",
                                                                              "distance")
                elif column_name == "distance":
                    queryset = Table.objects.filter(distance=query).values("date", "title",
                                                                           "count",
                                                                           "distance")
            except ValueError:
                return JsonResponse({"data": False})
        elif option_name == "bigger":
            try:
                if column_name == "count":
                    queryset = Table.objects.filter(count__gte=query).values("date", "title", "count", "distance")
                elif column_name == "distance":
                    queryset = Table.objects.filter(distance__gte=query).values("date", "title", "count", "distance")
            except ValueError:
                return JsonResponse({"data": False})
        elif option_name == "lower":
            try:
                if column_name == "count":
                    queryset = Table.objects.filter(count__lte=query).values("date", "title", "count", "distance")
                elif column_name == "distance":
                    queryset = Table.objects.filter(distance__lte=query).values("date", "title", "count", "distance")
            except ValueError:
                return JsonResponse({"data": False})
        if not queryset:
            return JsonResponse({"data": False})
        data = []
        for q in queryset:
            obj = {
                "date": q['date'],
                "title": q['title'],
                "count": q['count'],
                "distance": q['distance'],
            }
            data.append(obj)
        print(data)
        return JsonResponse({"data": data})
    return JsonResponse({"data": False})


def sort_data(request):
    query = request.GET.get("sort_filters")
    if not query:
        return JsonResponse({'data': False})
    if query == "title":
        queryset = Table.objects.order_by(query).values('date', 'title', 'count', 'distance')
    elif query == "count":
        queryset = Table.objects.order_by(query).values('date', 'title', 'count', 'distance')
    elif query == "distance":
        queryset = Table.objects.order_by(query).values('date', 'title', 'count', 'distance')
    else:
        return JsonResponse({"data": "Error"})
    data = []
    for q in queryset:
        obj = {
            "date": q['date'],
            "title": q['title'],
            "count": q['count'],
            "distance": q['distance'],
        }
        data.append(obj)
    return JsonResponse({'data': data})


