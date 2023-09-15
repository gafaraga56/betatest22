from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from .forms  import AdvertisementForm
from django.shortcuts import render, redirect



def index(request):
    advertisment_list = Advertisement.objects.all()
    context = {"advertisements": advertisment_list}
    return render(request,'index.html', context=context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
def advertisement(request):
    return render(request, 'advertisement.html')
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv_objecte = Advertisement(**form.cleaned_data)
            adv_objecte.authors = request.user
            adv_objecte.save()

    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
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


