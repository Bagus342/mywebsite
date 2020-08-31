from django.shortcuts import render, HttpResponse

def Landing(request):
    return render(request, 'index.html')