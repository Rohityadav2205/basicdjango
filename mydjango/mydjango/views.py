from django. shortcuts import render ,HttpResponse

def home(request):
    return HttpResponse("jai ram ji ki")

def books(request):
    return render( request,"a.html")