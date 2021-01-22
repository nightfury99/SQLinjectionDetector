from django.http import HttpResponse
from django.shortcuts import render

def view(request):
    # return HttpResponse('hehehehehe')
    return render(request, 'homepage.html')