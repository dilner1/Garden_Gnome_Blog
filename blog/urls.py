from blog import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import handler500


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='open_post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('update/<slug:slug>', views.UpdateView.as_view(), name='edit_post'),
    path('delete/<slug:slug>', views.DeleteView.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.LikeView.as_view(), name='like_post'),
    path('profile/', views.ProfilePage.as_view(), name='profile_page'),
]
