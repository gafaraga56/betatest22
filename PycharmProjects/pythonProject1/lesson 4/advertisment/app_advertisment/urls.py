from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post,register,login,profile,oktotorp

urlpatterns = [
    path('', index, name= "main-page"),
    path('topsellers',top_sellers,name="top-sellers"),
    path('advertisement',advertisement,name="advertisement"),
    path('advertisement-post',advertisement_post,name="advertisement-post"),
    path('register',register , name="register"),
    path('login',login , name="login"),
    path('profile',profile , name="profile"),
    path('oktotorp',oktotorp,name="oktotorp"),

]

