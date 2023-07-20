from django.shortcuts import render
from django.http import HttpResponse

def top_page(request):

    return render(request, 'top_page.html') 