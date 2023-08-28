from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# Create your views here.
def index(request):
    advertisment_list = Advertisement.objects.all()
    context = {"advertisements": advertisment_list}
    return render(request,'index.html', context=context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
def advertisement(request):
    return render(request, 'advertisement.html')
def advertisement_post(request):
    return render(request, 'advertisement-post.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def oktotorp(request):
    return render(request,"#.html")
def debug(request):
    obj_list = Advertisement.objects.all()
    print(obj_list)
    return HttpResponse("Yspeshno!")



