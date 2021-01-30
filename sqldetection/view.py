from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings

def view(request):
    # return HttpResponse('hehehehehe')
    if request.method == "POST":
        detect = request.POST.get('detect')
        display = request.POST.get('display')
        if detect == "detect":
            content = [
                {
                    "type" : open('access_log.txt', 'r').read()[::],
                    "name" : "Access Log"
                },
                {
                    "type" : open('dataset_parse.txt', 'r').read()[::],
                    "name" : "Parsed Log"
                },
                {
                    "type" : open('detection_results.txt', 'r').read()[::],
                    "name" : "Result of Detection"
                }    
            ]

            CONTENT = {'data' : content}
        elif display == "display":
            content = [
                {
                    "type" : open('access_log.txt', 'r').read()[::],
                    "name" : "Access Log"
                },
                {
                    "type" : open('dataset_parse.txt', 'r').read()[::],
                    "name" : "Parsed Log"
                },
            {
                "type" : "",
                "name" : "Result of Detection"
            }   
            ]

            CONTENT = {'data' : content}
        
    else:
        content = [
            {
                "type" : "",
                "name" : "Malware Queries"
            },
            {
                "type" : "",
                "name" : "Benign Queries"
            },
            {
                "type" : "",
                "name" : "Result of Detection"
            }    
        ]

        CONTENT = {'data' : content}

    return render(request, 'homepage.html', CONTENT)
    # comments = [
    #     {'name' : 'John Smith',
    #     'username' : '@johnsmith',
    #     'text' : 'I agree!'},
    #     {'name' : 'Stacy Warner',
    #     'username' : '@stacy1994',
    #     'text' : 'OP, you are the best'}
    # ]

    # context = {'comments' : comments}
    # data = open(os.path.join(settings.BASE_DIR, 'mal.txt')) # mal.txt
    # data2 = open(os.path.join(settings.BASE_DIR, 'benign.txt')) # benign.txt

    # context = {"file": open('mal.txt', 'r').read()[::]}
    

