from django.http import HttpResponse
# from django.http import render
 
def hello(request):
    # if request.method == "POST" and request.POST:
    return HttpResponse("Hello world ! ")