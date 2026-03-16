from django.shortcuts import render

# Create your views here.
def main_t(request):
    return render(request,"home.html")

