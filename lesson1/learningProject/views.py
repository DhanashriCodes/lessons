from django.http import HttpResponse,JsonResponse


animals=[{'animal_name':'Dog','animal_gender':'female','animal_color':'Brawon'},
        {'animal_name':'Elephent','animal_gender':'Male','animal_color':'Grey'},
        {'animal_name':'Cat','animal_gender':'female','animal_color':'White'},
        {'animal_name':'Monkey','animal_gender':'Male','animal_color':'Brawon'},

        ]
def handleAnimal(request):
    return JsonResponse(animals,safe=False)

def handleAnimalByGender(request,animal_gender=None  ):
    fillterdAnimal=[]
    if animal_gender is not None:
        for animal in animals:
            if (animal['animal_gender']== animal_gender):
                fillterdAnimal.append(animal)
        return JsonResponse(fillterdAnimal,safe=False)  

def handleAnimalByName(request,animal_name=None):
    fillteredName=[] 
    if(animal_name is not None):
        for animal in animals:
            if(animal['animal_name']==animal_name):
                fillteredName.append(animal)
        return JsonResponse(fillteredName,safe=False)         


# def handleAnimalByUnique(request):
    