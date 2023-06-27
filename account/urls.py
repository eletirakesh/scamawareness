from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import Profilepageview,SignUpview,ProfileUpdatePage


urlpatterns=[
    path('signup/',SignUpview.as_view(),name='signup'),
    path('<int:pk>',Profilepageview.as_view(),name='profile'),
    path('<int:pk>/update',ProfileUpdatePage.as_view(),name='profile_update')
 
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
