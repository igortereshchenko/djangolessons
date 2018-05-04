from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from mainpage.models import Customer, PureCustomer


def index(request):
    return HttpResponse("<h3>Hello!</h3>")

def htmlload(request):
    return render(request, 'mainPage.html',{'variable':False,'list': range(10)})


def tryparameters(request):

    table='<table class="table table-hover">'
    customers = Customer.objects.raw('SELECT customer_id as id, name, email, age FROM customer')

    purecustomers = PureCustomer.objects.all()
    for p in customers:
        ...
        table += '<tr>'
        table += '<td>'+str('')+'</td><td>'+p.name+'</td>'
        table += '</tr>'
    table += '</table>'

    print(table)
    #table = '<table></table>'
    return render(request, 'tryparameters.html', {'values' : ['Mike', 'John', 'Kate'], 'table' : table, 'customers' : purecustomers})


def formload(request):
    return render(request, 'form.html')


def form_handler(request):

    print(request.POST["lastname"])

    return HttpResponse("Done!")


def check_name(request):

    print("Hi")
    print(request.GET)

    if request.GET:
        user = request.GET["name"]
        print(user)
        return JsonResponse({'foo':'bar'})
    else:
        pass