from django.shortcuts import render

# Create your views here.
def myHelloFunction(request):

    return render(request, 'hello.html', {'name': 'dhanashri', 'age':20})