from django.shortcuts import render


# Create your views here.

# these views render to the html files
def index(request):
    return render(request, "BootstrapApp/index.html")

def page2(request):
    return render(request, 'BootstrapApp/page2.html')

def page3(request):
    return render(request, "BootstrapApp/page3.html")
