from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import  (
    Homepageview,
    Variousscamspageview,
    PostListView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    PostCreateView,
    CommentView,
    Aboutpageview,
    
 )



urlpatterns=[
    path('',PostListView.as_view(),name='home'),
    path('<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('<int:pk>/edit',PostUpdateView.as_view(),name='post_edit'),
    path('<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
    path('create/',PostCreateView.as_view(),name='post_create'),
    path('<int:pk>/comment',CommentView.as_view(),name='comment'),
    path('typesofscams/',Variousscamspageview.as_view(),name='typesofscams'),
    path('about/',Aboutpageview.as_view(),name='about'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)