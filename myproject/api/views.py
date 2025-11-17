from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
 
def hello_world(request):
    message = "ashish"
    html = f"""
    <div style="font-family: Arial; padding: 20px;">
        <h1 style="color: green;">{message}</h1>
    </div>
    """
    return HttpResponse(html, content_type="text/html")
