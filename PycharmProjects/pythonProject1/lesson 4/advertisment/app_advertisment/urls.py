from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post,register,login,profile,oktotorp,debug
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name= "main-page"),
    path('topsellers',top_sellers,name="top-sellers"),
    path('advertisement',advertisement,name="advertisement"),
    path('advertisement-post',advertisement_post,name="advertisement-post"),
    path('register',register , name="register"),
    path('login',login , name="login"),
    path('profile',profile , name="profile"),
    path('oktotorp',oktotorp,name="oktotorp"),
    path('debug/',debug)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)




