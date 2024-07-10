from django.db.models import F
from django.http import HttpResponse,JsonResponse
from . models import Employee

# Create your views here.
def handleEmployee(request, fruitName):
    if request.method=='GET':
        manager = Employee.objects.filter(name=fruitName).values()
        Employees = list(manager)
    return JsonResponse(Employees,safe=False)

