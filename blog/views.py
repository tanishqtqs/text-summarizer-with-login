from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse

def ping(request):
    return JsonResponse({'message': 'Server is running!'})
