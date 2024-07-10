from django.http import HttpResponse, JsonResponse, HttpRequest
from . models import Student
from django.db.models import Q

# Create your views here.

def handlestudent(request: HttpRequest):

    if request.method == 'GET':
        manager = Student.objects.filter(Q(name__startswith='d') & Q(name__endswith='i')).order_by('name').values()
        return JsonResponse({
            'students': list(manager)
        })
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        id = request.POST.get('id')
        role = request.POST.get('role')

        student = None

        if id is None:
            student = Student()
            student.name = name
            student.email = email
            student.role = role
            student.save()

            return JsonResponse({'insertedStudent': student.id})
        
        student = Student.objects.get(id=id)
        student.name = name
        student.email = email
        student.save()


        # # student = Student.objects.create(name=name, email=email)
        # student = Student()
        # student.name = name
        # student.email = email
        # student.save()

        return JsonResponse({
            'studentName': student.name if student is not None else '',
            'studentEmail': student.email if student is not None else ''
        })
